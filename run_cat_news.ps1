#!/usr/bin/env pwsh
# Cat News Network - AI Video Creator
# Single Entry Point for Cat News Video Generation

Write-Host "🐱 Welcome to Cat News Network - AI Video Creator! 🐱" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "❌ Virtual environment not found. Creating one..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "✅ Virtual environment created!" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Blue
& ".venv\Scripts\Activate.ps1"

# Check if requirements are installed
Write-Host "📦 Checking dependencies..." -ForegroundColor Blue
try {
    python -c "import crewai, groq; print('Core dependencies available')"
    Write-Host "✅ Core dependencies found!" -ForegroundColor Green
} catch {
    Write-Host "❌ Dependencies missing. Installing..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed!" -ForegroundColor Green
}

# Check API keys
Write-Host "🔑 Checking API configuration..." -ForegroundColor Blue
$envFile = ".env"
if (Test-Path $envFile) {
    Write-Host "✅ Environment file found!" -ForegroundColor Green
} else {
    Write-Host "⚠️  No .env file found. Creating template..." -ForegroundColor Yellow
    @"
# Cat News Network API Keys
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here

# Optional APIs
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
"@ | Out-File -FilePath $envFile -Encoding UTF8
    Write-Host "📝 Created .env template. Please add your API keys!" -ForegroundColor Yellow
}

# Show menu options
Write-Host ""
Write-Host "🎬 What would you like to do?" -ForegroundColor Cyan
Write-Host "1. Generate a Cat News Video Package (Recommended)" -ForegroundColor White
Write-Host "2. Test API Connections" -ForegroundColor White  
Write-Host "3. Run Quick Demo" -ForegroundColor White
Write-Host "4. View Project Settings" -ForegroundColor White
Write-Host "5. Exit" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

switch ($choice) {
    "1" {
        Write-Host "🎥 Generating Cat News Video Package..." -ForegroundColor Green
        python final_demo.py
    }
    "2" {
        Write-Host "🔧 Testing API connections..." -ForegroundColor Blue
        python test_groq_setup.py
    }
    "3" {
        Write-Host "⚡ Running quick demo..." -ForegroundColor Blue
        python -c "
import sys
sys.path.append('.')
from tools.content_tools import AIVideoCreationTool

tool = AIVideoCreationTool()
result = tool.create_cat_news_video('AI breakthrough in autonomous vehicles')
print('🎉 Demo completed!')
print(f'📝 Script length: {len(result.get(\"script\", \"\"))} characters')
print(f'📊 Generated content: {\"script\" in result and \"metadata\" in result}')
"
    }
    "4" {
        Write-Host "⚙️  Project Settings:" -ForegroundColor Blue
        python -c "
import sys
sys.path.append('.')
from config.settings import PROJECT_CONCEPT, CAT_ANCHORS
print(f'📺 Project: {PROJECT_CONCEPT[\"name\"]}')
print(f'📝 Description: {PROJECT_CONCEPT[\"description\"]}')
print(f'🎭 Available Cat Anchors: {list(CAT_ANCHORS.keys())}')
"
    }
    "5" {
        Write-Host "👋 Goodbye! Keep making viral cat content! 🐱" -ForegroundColor Cyan
        exit
    }
    default {
        Write-Host "❌ Invalid choice. Please run the script again." -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🎉 Task completed! Check the output/ folder for generated content." -ForegroundColor Green
Write-Host "📺 Ready to create viral cat news videos! 🐱📰" -ForegroundColor Cyan
