# Deployment Guide

## 🚀 Running Locally

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
FASTAPI_URL=http://localhost:8000
```

### Step 3: Run the Servers

#### Option A: Run Both Servers (Easiest)

Double-click `start_both.bat` or run:
```bash
start_both.bat
```

This will open two separate windows:
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:8501

#### Option B: Run Separately

**Backend:**
```bash
start_backend.bat
# Or manually:
cd backend
uvicorn main:app --reload --port 8000
```

**Frontend (in a new terminal):**
```bash
start_frontend.bat
# Or manually:
streamlit run frontend/app.py
```

## 🌐 Hosting Options

### ⚠️ Important: GitHub Pages Limitation

**GitHub Pages only hosts static websites** (HTML, CSS, JavaScript). It cannot run Python applications like Streamlit or FastAPI.

### Recommended Hosting Solutions

#### 1. Frontend (Streamlit) - Streamlit Cloud (FREE)

1. **Push your code to GitHub** (already done!)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository: `anoopworks/AI_RESUME_RAG` (or `RESUME_ANALYZER`)
6. Set the main file path: `frontend/app.py`
7. Add environment variables:
   - `FASTAPI_URL`: Your deployed backend URL (see below)
   - `GEMINI_API_KEY`: Your Gemini API key
8. Click "Deploy"

**Result**: Your Streamlit app will be live at `https://your-app-name.streamlit.app`

#### 2. Backend (FastAPI) - Render (FREE)

1. Go to [Render](https://render.com)
2. Sign up/Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: `ai-resume-analyzer-backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variable:
   - `GEMINI_API_KEY`: Your Gemini API key
7. Click "Create Web Service"

**Result**: Your backend will be live at `https://your-app-name.onrender.com`

#### Alternative Backend Hosting Options

**Railway** (FREE tier available):
- Connect GitHub repository
- Use `Procfile` for deployment
- Set environment variables

**Heroku** (Paid, but has free alternatives):
- Use `Procfile` for deployment
- Set config vars in dashboard

### 3. Update Frontend to Use Deployed Backend

After deploying the backend, update the `FASTAPI_URL` in Streamlit Cloud:
- Go to your Streamlit Cloud app settings
- Update `FASTAPI_URL` to your Render/Railway backend URL
- Example: `https://ai-resume-analyzer-backend.onrender.com`

## 📋 Deployment Checklist

- [ ] Install dependencies locally
- [ ] Test locally with `start_both.bat`
- [ ] Create `.env` file with API keys
- [ ] Push code to GitHub
- [ ] Deploy backend to Render/Railway
- [ ] Deploy frontend to Streamlit Cloud
- [ ] Update `FASTAPI_URL` in Streamlit Cloud
- [ ] Test deployed application

## 🔗 Quick Links

- **GitHub Repository**: https://github.com/anoopworks/AI_RESUME_RAG
- **Streamlit Cloud**: https://streamlit.io/cloud
- **Render**: https://render.com
- **Railway**: https://railway.app

## 🆘 Troubleshooting

### Backend not connecting?
- Check if backend is running: `http://localhost:8000/`
- Verify `FASTAPI_URL` in `.env` matches backend URL
- Check CORS settings if deploying

### Frontend not loading?
- Check if Streamlit is running: `http://localhost:8501`
- Verify all dependencies are installed
- Check browser console for errors

### Deployment issues?
- Ensure all environment variables are set
- Check build logs in hosting platform
- Verify Python version compatibility

