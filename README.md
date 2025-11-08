# AI Resume Analyzer (Gemini-Powered)

A full-stack application that analyzes resumes using Google Gemini AI, providing structured feedback for Data Science and AI roles.

## 🏗️ Architecture

- **Backend**: FastAPI (Python) - Handles PDF parsing and AI analysis
- **Frontend**: Streamlit (Python) - User interface for uploading resumes
- **AI Model**: Google Gemini 2.5 Flash

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/anoopworks/AI_RESUME_RAG.git
cd AI_RESUME_RAG
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
FASTAPI_URL=http://localhost:8000
```

### 4. Run the Application

#### Option A: Run Both Servers (Recommended)

Double-click `start_both.bat` or run:
```bash
start_both.bat
```

#### Option B: Run Servers Separately

**Terminal 1 - Backend:**
```bash
start_backend.bat
# Or manually:
cd backend
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
start_frontend.bat
# Or manually:
streamlit run frontend/app.py
```

### 5. Access the Application

- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🌐 Deployment

### Backend Deployment (Render/Railway/Heroku)

1. **Render** (Recommended):
   - Push code to GitHub
   - Connect repository to Render
   - Use `render.yaml` configuration
   - Set `GEMINI_API_KEY` environment variable

2. **Railway**:
   - Connect GitHub repository
   - Use `Procfile` for deployment
   - Set environment variables

3. **Heroku**:
   - Use `Procfile` for deployment
   - Set config vars in Heroku dashboard

### Frontend Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Set environment variables:
   - `FASTAPI_URL`: Your deployed backend URL
   - `GEMINI_API_KEY`: Your Gemini API key
5. Deploy!

### Important Notes

⚠️ **GitHub Pages Limitation**: GitHub Pages only hosts static websites. For Python applications:
- Use **Streamlit Cloud** for the frontend (free)
- Use **Render/Railway** for the backend (free tiers available)

## 📁 Project Structure

```
AI_RESUME_RAG/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── analyzer_service.py  # Gemini AI integration
│   ├── requirements.txt     # Backend dependencies
│   └── utils/
│       └── pdf_parser.py   # PDF text extraction
├── frontend/
│   └── app.py              # Streamlit UI
├── uploaded_resumes/       # Temporary file storage
├── requirements.txt        # All dependencies
├── start_backend.bat      # Backend startup script
├── start_frontend.bat     # Frontend startup script
├── start_both.bat         # Start both servers
├── Procfile               # Heroku/Railway config
├── render.yaml            # Render deployment config
└── README.md              # This file
```

## 🔧 Configuration

### Backend Configuration

The backend runs on port 8000 by default. To change:
```bash
uvicorn backend.main:app --reload --port YOUR_PORT
```

### Frontend Configuration

Update `FASTAPI_URL` in `.env` or environment variables to point to your deployed backend.

## 📝 API Endpoints

- `GET /` - Health check
- `POST /analyze-resume` - Upload PDF and get analysis
  - **Request**: Multipart form data with PDF file
  - **Response**: JSON with analysis results

## 🛠️ Development

### Running Tests

```bash
# Test backend
curl http://localhost:8000/

# Test API endpoint
curl -X POST "http://localhost:8000/analyze-resume" \
  -F "file=@path/to/resume.pdf"
```

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or issues, please open an issue on GitHub.
