# setup-dev.ps1

Write-Host "🔧 Setting up local Python environment" -ForegroundColor Cyan

# Check Python installation
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed or not in PATH. Please install Python 3.10+ first." -ForegroundColor Red
    exit
}

Write-Host "📦 Creating virtual environment (.venv)"
python -m venv .venv

Write-Host "✅ Activating virtual environment"
.\\.venv\\Scripts\\activate.ps1


Write-Host "⬆️ Upgrading pip"
python -m pip install --upgrade pip

Write-Host "📥 Installing dependencies from requirements.txt"
pip install -r requirements.txt

Write-Host "🚀 Starting the Streamlit app..."
streamlit run app.py
