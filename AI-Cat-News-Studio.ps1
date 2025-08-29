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
Write-Host "Available AI Cat News Network Options:" -ForegroundColor Cyan
Write-Host "1. 📰 Generate Cat News Script (Real News + Cat Commentary)" -ForegroundColor White  
Write-Host "2. 🎤 Generate Voice-Over (From Latest Script)" -ForegroundColor White
Write-Host "3. 🎬 Create Video with Veo 3 (Complete Production)" -ForegroundColor Green
Write-Host "4. 📁 Browse Content Structure (View All Content)" -ForegroundColor Blue
Write-Host ""

$choice = Read-Host "Enter your choice (1-4)"

switch ($choice) {
    "1" {
        Write-Host "📰 Generating Cat News Script..." -ForegroundColor Yellow
        & $pythonCmd scripts\quick_cat_test.py
    }
    "2" {
        Write-Host "🎤 Generating Voice-Over..." -ForegroundColor Yellow
        & $pythonCmd scripts\test_voice.py
    }
    "3" {
        Write-Host "🎬 Creating Video with Veo 3..." -ForegroundColor Green
        & $pythonCmd scripts\create_video_veo3.py
    }
    "4" {
        Write-Host "📁 Browsing Content Structure..." -ForegroundColor Blue
        & $pythonCmd scripts\content_browser.py
    }
    default {
        Write-Host "❌ Invalid choice. Showing content browser..." -ForegroundColor Red
        & $pythonCmd scripts\content_browser.py
    }
}

Write-Host ""
Write-Host "🎉 AI Cat News Network session completed!" -ForegroundColor Green
