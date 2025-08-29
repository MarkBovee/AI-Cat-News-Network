# AI Cat News Network - PowerShell Entry Point
# Multiple AI Video Generation Providers (MiniMax & Google Veo 3)
# Usage: .\AI-Cat-News-Studio.ps1 [option] [-clean]
# Examples:
#   .\AI-Cat-News-Studio.ps1 1        # Generate script
#   .\AI-Cat-News-Studio.ps1 4        # Browse content
#   .\AI-Cat-News-Studio.ps1 -clean   # Clean old content
#   .\AI-Cat-News-Studio.ps1 2 -clean # Generate voice then clean

param(
    [Parameter(Position=0)]
    [string]$Option = $null,
    
    [Parameter()]
    [switch]$Clean = $false,
    
    [Parameter()]
    [switch]$Help = $false
)

# Show help if requested
if ($Help) {
    Write-Host "🐱 AI Cat News Network - Command Line Options" -ForegroundColor Green
    Write-Host "=============================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\AI-Cat-News-Studio.ps1 [option] [-clean] [-help]" -ForegroundColor White
    Write-Host ""
    Write-Host "Options:" -ForegroundColor Cyan
    Write-Host "  1     📰 Generate Cat News Script (Real News + Cat Commentary)" -ForegroundColor White
    Write-Host "  2     🎤 Generate Voice-Over (From Latest Script)" -ForegroundColor White
    Write-Host "  3     🎬 Create Video Metadata with Veo 3 (Preparation)" -ForegroundColor Green
    Write-Host "  4     🎥 Generate REAL Video with Veo 3 (API Call)" -ForegroundColor Magenta
    Write-Host "  5     📁 Browse Content Structure (View All Content)" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Flags:" -ForegroundColor Cyan
    Write-Host "  -clean    🧹 Clean old content files after operation" -ForegroundColor Yellow
    Write-Host "  -help     ❓ Show this help message" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Cyan
    Write-Host "  .\AI-Cat-News-Studio.ps1 1        # Generate script only" -ForegroundColor Gray
    Write-Host "  .\AI-Cat-News-Studio.ps1 5        # Browse content only" -ForegroundColor Gray
    Write-Host "  .\AI-Cat-News-Studio.ps1 4 -clean # Generate real video then clean" -ForegroundColor Gray
    Write-Host "  .\AI-Cat-News-Studio.ps1 -clean   # Clean content only" -ForegroundColor Gray
    Write-Host ""
    exit 0
}

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

# Function to clean old content files
function Invoke-ContentClean {
    Write-Host "🧹 Cleaning old content files..." -ForegroundColor Yellow
    Write-Host ""
    
    $contentDirs = @("content\audio", "content\video", "content\scripts", "content\newsitems", "content\ideas")
    $totalCleaned = 0
    
    foreach ($dir in $contentDirs) {
        if (Test-Path $dir) {
            $files = Get-ChildItem $dir -File
            $fileCount = $files.Count
            
            if ($fileCount -gt 0) {
                Write-Host "📁 $dir ($fileCount files)" -ForegroundColor Cyan
                
                # Keep only the latest 3 files, clean the rest
                $filesToKeep = $files | Sort-Object LastWriteTime -Descending | Select-Object -First 3
                $filesToDelete = $files | Where-Object { $_.Name -notin $filesToKeep.Name }
                
                foreach ($file in $filesToDelete) {
                    Remove-Item $file.FullName -Force
                    Write-Host "   🗑️  Removed: $($file.Name)" -ForegroundColor Gray
                    $totalCleaned++
                }
                
                if ($filesToDelete.Count -eq 0) {
                    Write-Host "   ✅ No cleanup needed (3 or fewer files)" -ForegroundColor Green
                }
            } else {
                Write-Host "📁 $dir (empty)" -ForegroundColor Gray
            }
        }
    }
    
    Write-Host ""
    if ($totalCleaned -gt 0) {
        Write-Host "✅ Cleaned $totalCleaned old files (kept latest 3 in each category)" -ForegroundColor Green
    } else {
        Write-Host "✅ No cleanup needed - all directories have 3 or fewer files" -ForegroundColor Green
    }
    Write-Host ""
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

# Handle clean-only operation
if ($Clean -and $Option -eq "") {
    Invoke-ContentClean
    Write-Host "🎉 Content cleanup completed!" -ForegroundColor Green
    exit 0
}

# If no option provided, show interactive menu
if ($Option -eq $null -or $Option -eq "") {
    Write-Host "Available AI Cat News Network Options:" -ForegroundColor Cyan
    Write-Host "1. 📰 Generate Cat News Script (Real News + Cat Commentary)" -ForegroundColor White  
    Write-Host "2. 🎤 Generate Voice-Over (From Latest Script)" -ForegroundColor White
    Write-Host "3. 🎬 Create Video with Veo 3 (Metadata Preparation)" -ForegroundColor Green
    Write-Host "4. 🎥 Generate REAL Video with Veo 3 (API Call)" -ForegroundColor Magenta
    Write-Host "5. 📁 Browse Content Structure (View All Content)" -ForegroundColor Blue
    Write-Host ""
    Write-Host "💡 Tip: Use parameters for automation! Example: .\AI-Cat-News-Studio.ps1 5" -ForegroundColor Yellow
    Write-Host ""

    $Option = Read-Host "Enter your choice (1-5)"
}

# Execute the chosen option
switch ($Option) {
    "1" {
        Write-Host "📰 Generating Cat News Script..." -ForegroundColor Yellow
        & $pythonCmd scripts\quick_cat_test.py
    }
    "2" {
        Write-Host "🎤 Generating Voice-Over..." -ForegroundColor Yellow
        & $pythonCmd scripts\test_voice.py
    }
    "3" {
        Write-Host "🎬 Creating Video Metadata with Veo 3..." -ForegroundColor Green
        & $pythonCmd scripts\create_video_veo3.py
    }
    "4" {
        Write-Host "🎥 Generating REAL Video with Veo 3..." -ForegroundColor Magenta
        & $pythonCmd scripts\create_real_veo3_video.py
    }
    "5" {
        Write-Host "📁 Browsing Content Structure..." -ForegroundColor Blue
        & $pythonCmd scripts\content_browser.py
    }
    default {
        Write-Host "❌ Invalid choice '$Option'. Valid options: 1, 2, 3, 4, 5" -ForegroundColor Red
        Write-Host "💡 Use -help for usage information" -ForegroundColor Yellow
        exit 1
    }
}

# Clean content if requested
if ($Clean) {
    Write-Host ""
    Invoke-ContentClean
}

Write-Host ""
Write-Host "🎉 AI Cat News Network session completed!" -ForegroundColor Green
