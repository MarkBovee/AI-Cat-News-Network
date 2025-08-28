# AI Cat News Network - PowerShell Entry Point
# Enhanced with MiniMax AI Video Generation (HailuoAI)

Write-Host "🐱 AI Cat News Network - MiniMax Video Generation Studio" -ForegroundColor Green
Write-Host "=======================================================" -ForegroundColor Green
Write-Host ""

# Check if Python virtual environment exists
if (Test-Path ".venv") {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
    & .venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠️  Virtual environment not found. Creating one..." -ForegroundColor Yellow
    python -m venv .venv
    & .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "Available MiniMax AI Video Generation Options:" -ForegroundColor Cyan
Write-Host "1. 🎬 MiniMax Video Generator Demo (Real API Integration)" -ForegroundColor White
Write-Host "2. 📰 Quick Cat News Test (Text-based)" -ForegroundColor White  
Write-Host "3. 🧪 Test Groq AI Setup" -ForegroundColor White
Write-Host "4. 🎤 Test Voice Generation" -ForegroundColor White
Write-Host "5. 🚀 Full MiniMax Production Demo (Real Video Generation)" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

switch ($choice) {
    "1" {
        Write-Host "🎬 Running MiniMax Video Generator Demo..." -ForegroundColor Yellow
        python scripts\ai_video_generator_demo.py
    }
    "2" {
        Write-Host "📰 Running Quick Cat News Test..." -ForegroundColor Yellow  
        python scripts\quick_cat_test.py
    }
    "3" {
        Write-Host "🧪 Testing Groq AI Setup..." -ForegroundColor Yellow
        python scripts\test_groq_setup.py
    }
    "4" {
        Write-Host "🎤 Testing Voice Generation..." -ForegroundColor Yellow
        python scripts\test_voice.py
    }
    "5" {
        Write-Host "🚀 Full MiniMax Production Demo (Generates Real Videos)..." -ForegroundColor Yellow
        python scripts\ai_video_demo.py
    }
    default {
        Write-Host "❌ Invalid choice. Running default MiniMax Demo..." -ForegroundColor Red
        python scripts\ai_video_generator_demo.py
    }
}

Write-Host ""
Write-Host "🎉 AI Cat News Network session completed!" -ForegroundColor Green
