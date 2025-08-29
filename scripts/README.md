# AI Cat News Network - Production Scripts

This directory contains the core production scripts for generating cat news content.

## 🎬 Production Pipeline Scripts

### Essential Scripts
- **`quick_cat_test.py`**: Generate cat news scripts from real news with feline commentary
- **`test_voice.py`**: Create professional voice-overs using ElevenLabs API  
- **`create_video_veo3.py`**: Generate videos using Google Veo 3 AI
- **`content_browser.py`**: Browse and manage organized content structure

## 🚀 Production Workflow

1. **Generate Script**: `python scripts/quick_cat_test.py`
   - Selects random real news story
   - Creates cat commentary with professional format
   - Saves to `content/scripts/` with metadata

2. **Create Voice-Over**: `python scripts/test_voice.py` 
   - Automatically uses latest script
   - Generates professional voice-over with ElevenLabs
   - Saves to `content/audio/` with voice settings

3. **Generate Video**: `python scripts/create_video_veo3.py`
   - Uses latest script and audio files
   - Creates professional video prompt for Veo 3
   - Prepares complete video production package

4. **Browse Content**: `python scripts/content_browser.py`
   - Shows all content organized by type
   - Displays pipeline status and file counts
   - Tracks what's ready for next production stage

## 🎯 Streamlined & Clean

All test scripts, demos, and unused code have been removed for a clean, production-focused codebase. The PowerShell launcher (`AI-Cat-News-Studio.ps1`) provides easy access to all four essential functions.

## � Content Integration

All scripts use the organized content structure in `content/` with automatic:
- File linking across pipeline stages
- Metadata generation and tracking  
- Timestamp-based naming conventions
- Professional production organization

❌ **Removed Scripts** (redundant/outdated):
- advanced_cat_news.py
- cat_news_studio.py
- final_demo.py
- full_cat_video_test.py
- main.py
- simple_cat_news.py
- test_cat_news.py
- test_minimax_api.py
