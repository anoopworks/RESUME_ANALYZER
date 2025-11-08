# GitHub Repository Setup Instructions

## Prerequisites
1. Install Git from https://git-scm.com/download/win
2. Create a GitHub account at https://github.com (if you don't have one)
3. Install GitHub CLI (optional but recommended): https://cli.github.com/

## Steps to Push to GitHub

### Option 1: Using GitHub CLI (Recommended)

1. **Authenticate with GitHub:**
   ```bash
   gh auth login
   ```

2. **Initialize Git and create repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AI Resume Analyzer project"
   gh repo create AI_RESUME_RAG --public --source=. --remote=origin --push
   ```

### Option 2: Manual Setup

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `AI_RESUME_RAG` (or your preferred name)
   - Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license
   - Click "Create repository"

2. **Add remote and push (Git is already initialized and committed):**
   ```bash
   git remote add origin https://github.com/anoopworks/AI_RESUME_RAG.git
   git push -u origin main
   ```

## What's Excluded

The `.gitignore` file has been configured to exclude:
- `__pycache__/` directories
- `.env` files
- Virtual environments
- IDE files
- OS-specific files

