import streamlit as st
import httpx # Used for making async HTTP requests to the FastAPI backend
import json
from io import BytesIO

# --- Configuration ---
FASTAPI_URL = "http://localhost:8000" # Update if FastAPI is hosted elsewhere

st.set_page_config(
    page_title="AI Resume Analyzer (Gemini-Powered)",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- UI Layout ---
st.title("🚀 AI Resume Analyzer")
st.markdown("Use Google Gemini to get structured, objective feedback on your resume for **Data Science & AI roles**.")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF Only)", 
    type="pdf",
    accept_multiple_files=False,
    help="Please upload a PDF document for analysis."
)

if uploaded_file is not None:
    st.info("File uploaded. Click 'Analyze Resume' to start the evaluation.")

    if st.button("✨ Analyze Resume", type="primary"):
        if uploaded_file is None:
            st.error("Please upload a PDF file first.")
        else:
            with st.spinner("Analyzing with Gemini... This may take a moment."):
                try:
                    # Prepare file for multipart form data
                    file_content = uploaded_file.read()
                    files = {
                        "file": (uploaded_file.name, file_content, "application/pdf")
                    }

                    # Send request to FastAPI backend
                    response = httpx.post(
                        f"{FASTAPI_URL}/analyze-resume", 
                        files=files,
                        timeout=120 # Allow up to 120 seconds for LLM response
                    )

                    # Check for successful response
                    if response.status_code == 200:
                        analysis_data = response.json()
                        
                        st.balloons()
                        st.subheader("✅ Analysis Complete")
                        
                        # --- Display Results (Frontend Display Interface) ---
                        
                        # 1. Overall Score
                        score = analysis_data.get("Overall_Score", 0)
                        
                        if score >= 80:
                            score_emoji = "🌟"
                        elif score >= 60:
                            score_emoji = "👍"
                        else:
                            score_emoji = "⚠️"
                            
                        st.metric(
                            label=f"Overall Resume Score {score_emoji}", 
                            value=f"{score}/100", 
                            delta_color="off"
                        )
                        st.markdown(f"**Professional Summary:** *{analysis_data.get('Summary', 'N/A')}*")
                        
                        st.divider()

                        # 2. Strengths and Weaknesses
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("💚 Strengths")
                            for item in analysis_data.get("Strengths", ["N/A"]):
                                st.markdown(f"* **{item}**")

                        with col2:
                            st.subheader("💔 Weaknesses")
                            for item in analysis_data.get("Weaknesses", ["N/A"]):
                                st.markdown(f"* **{item}**")

                        st.divider()

                        # 3. Improvement Suggestions
                        st.subheader("💡 Improvement Recommendations")
                        st.caption("Personalized tips to optimize your resume for target roles.")
                        for i, item in enumerate(analysis_data.get("Suggestions", ["N/A"])):
                            st.markdown(f"**{i+1}.** {item}")

                        # Optional: Show Raw JSON for debugging
                        with st.expander("View Raw JSON Output"):
                            st.code(json.dumps(analysis_data, indent=2), language="json")


                    else:
                        error_detail = response.json().get("detail", "Unknown error from backend.")
                        st.error(f"❌ Backend Error (Status Code: {response.status_code}): {error_detail}")

                except httpx.ConnectError:
                    st.error(f"⚠️ **Connection Error:** Could not connect to the FastAPI backend at `{FASTAPI_URL}`. Make sure it is running.")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

# To run the frontend:
# streamlit run frontend/app.py