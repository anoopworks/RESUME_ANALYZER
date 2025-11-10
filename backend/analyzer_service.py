import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Pydantic Output Specification Model (Evaluation Parser) ---
# Defines the exact structure the model MUST return
class ResumeAnalysis(BaseModel):
    Overall_Score: int
    Strengths: list[str]
    Weaknesses: list[str]
    Suggestions: list[str]
    Summary: str

class AnalyzerService:
    def __init__(self):
        # Initialize Gemini Client
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it in a .env file.")
        self.client = genai.Client(api_key=api_key)
        self.model = 'gemini-2.5-flash' # Fast and capable model for this task

    def _get_system_prompt(self) -> str:
        """Constructs the domain-specific prompt for the Gemini model."""
        return (
            "You are an expert AI Resume Analyzer for Data Science and AI roles. "
            "Your task is to objectively evaluate the provided resume text. "
            "Strictly adhere to the required JSON output format. "
            "The Overall_Score must be between 0 and 100. "
            "Base your evaluation on relevance to Data Science, Machine Learning, and AI Engineering."
        )

    def analyze_resume(self, resume_text: str) -> dict:
        """
        Sends the resume text to the Gemini model for structured analysis.
        """
        try:
            # 1. Prompt Engineering Layer
            system_instruction = self._get_system_prompt()
            
            user_content = (
                f"Analyze the following resume text for a Data Scientist role:\n\n"
                f"--- RESUME CONTENT ---\n"
                f"{resume_text}\n"
                f"----------------------"
            )

            # 2. LLM Interaction Module
            response = self.client.models.generate_content(
                model=self.model,
                contents=[user_content],
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_mime_type="application/json",
                    response_schema=ResumeAnalysis,
                    temperature=0.2 # Lower temperature for objective analysis
                ),
            )

            # 3. Evaluation Parser: The model is instructed to return JSON matching ResumeAnalysis schema, 
            # so the response.text is already a valid JSON string.
            return json.loads(response.text)

        except Exception as e:
            print(f"Error during Gemini API call: {e}")
            return {
                "error": "Failed to analyze resume. Check API key and service status.", 
                "details": str(e)
            }
