# AI Cat News Network - PowerShell Entry Point
# Multiple AI Video Generation Providers (MiniMax & Google Veo 3)

Write-Host "🐱 AI Cat News Network - Multi-Provider Video Generation Studio" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Green
Write-Host ""

# Function to check if Python is available
function Test-PythonAvailable {
    $pythonCommands = @("python", "python3", "py")
    foreach ($cmd in $pythonCommands) {
        try {
            $null = & $cmd --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                return $cmd
            }
        } catch {
            continue
        }
    }
    return $null
}

# Check for Python installation
$pythonCmd = Test-PythonAvailable
if (-not $pythonCmd) {
    Write-Host "❌ Python not found! Please install Python first:" -ForegroundColor Red
    Write-Host "   • Microsoft Store: Search 'Python' and install Python 3.11+" -ForegroundColor Yellow
    Write-Host "   • Or visit: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter after installing Python to continue"
    $pythonCmd = Test-PythonAvailable
    if (-not $pythonCmd) {
        Write-Host "❌ Python still not found. Exiting..." -ForegroundColor Red
        exit 1
    }
}

Write-Host "✅ Python found: $pythonCmd" -ForegroundColor Green

# Check if Python virtual environment exists
if (Test-Path ".venv") {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
    & .venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠️  Virtual environment not found. Creating one..." -ForegroundColor Yellow
    & $pythonCmd -m venv .venv
    & .venv\Scripts\Activate.ps1
    & $pythonCmd -m pip install -r requirements.txt
}

Write-Host ""
Write-Host "Available AI Video Generation Options:" -ForegroundColor Cyan
Write-Host "1. 🎬 MiniMax Video Generator Demo (Paid API)" -ForegroundColor White
Write-Host "2. 🆕 Google Veo 3 Video Generator Demo (Free Tier Available)" -ForegroundColor Green
Write-Host "3. 🔍 Compare Video Providers (MiniMax vs Veo 3)" -ForegroundColor Cyan
Write-Host "4. 📰 Quick Cat News Test (Text-based)" -ForegroundColor White  
Write-Host "5. 🧪 Test Groq AI Setup" -ForegroundColor White
Write-Host "6. 🎤 Test Voice Generation" -ForegroundColor White
Write-Host "7. 🚀 Full Production Demo - MiniMax (Real Video Generation)" -ForegroundColor White
Write-Host "8. 🚀 Full Production Demo - Veo 3 (Real Video Generation)" -ForegroundColor Green
Write-Host "9. 🧪 Integration Test (All Systems)" -ForegroundColor Cyan
Write-Host "10. 🔧 Test Individual Components (Modular Testing)" -ForegroundColor Yellow
Write-Host "11. 🧬 Test Agent Framework (Full Workflow with Outputs)" -ForegroundColor Magenta
Write-Host ""

$choice = Read-Host "Enter your choice (1-11)"

switch ($choice) {
    "1" {
        Write-Host "🎬 Running MiniMax Video Generator Demo..." -ForegroundColor Yellow
        & $pythonCmd scripts\ai_video_generator_demo.py
    }
    "2" {
        Write-Host "🆕 Running Google Veo 3 Video Generator Demo..." -ForegroundColor Green
        & $pythonCmd scripts\veo3_video_demo.py
    }
    "3" {
        Write-Host "🔍 Comparing Video Providers..." -ForegroundColor Cyan
        & $pythonCmd scripts\provider_comparison.py
    }
    "4" {
        Write-Host "📰 Running Quick Cat News Test..." -ForegroundColor Yellow  
        & $pythonCmd scripts\quick_cat_test.py
    }
    "5" {
        Write-Host "🧪 Testing Groq AI Setup..." -ForegroundColor Yellow
        & $pythonCmd scripts\test_groq_setup.py
    }
    "6" {
        Write-Host "🎤 Testing Voice Generation..." -ForegroundColor Yellow
        & $pythonCmd scripts\test_voice.py
    }
    "7" {
        Write-Host "🚀 Full MiniMax Production Demo (Generates Real Videos)..." -ForegroundColor Yellow
        & $pythonCmd scripts\ai_video_demo.py
    }
    "8" {
        Write-Host "🚀 Full Veo 3 Production Demo (Generates Real Videos)..." -ForegroundColor Green
        & $pythonCmd scripts\veo3_production_demo.py
    }
    "9" {
        Write-Host "🧪 Running Integration Test..." -ForegroundColor Cyan
        & $pythonCmd scripts\test_integration.py
    }
    "10" {
        Write-Host "🔧 Testing Individual Components..." -ForegroundColor Yellow
        & $pythonCmd scripts\test_components.py
    }
    "11" {
        Write-Host "🧬 Running Agent Framework Test..." -ForegroundColor Magenta
        & $pythonCmd scripts\test_agent_framework.py
    }
    default {
        Write-Host "❌ Invalid choice. Running component test..." -ForegroundColor Red
        & $pythonCmd scripts\test_components.py
    }
}

Write-Host ""
Write-Host "🎉 AI Cat News Network session completed!" -ForegroundColor Green
