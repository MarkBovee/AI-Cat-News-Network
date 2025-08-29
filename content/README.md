# AI Cat News Network - Content Organization

This directory contains all generated content organized by type and stage in the production pipeline.

## 📁 Directory Structure

```
content/
├── newsitems/    # Real news stories selected for cat commentary
├── ideas/        # Content ideas and concepts for future videos  
├── scripts/      # Generated cat news scripts with timing and dialogue
├── audio/        # Voice-over files generated from scripts
└── video/        # Final video productions ready for social media
```

## 🔄 Content Pipeline Flow

1. **News Selection** → `newsitems/`
   - Real news stories curated for cat commentary
   - Stored as JSON with metadata and source info

2. **Script Generation** → `scripts/` 
   - AI-generated cat news scripts with intro/main/outro
   - Professional format optimized for 20-30 second videos
   - Links back to original news item

3. **Voice Generation** → `audio/`
   - ElevenLabs AI voice-over from scripts
   - Professional news anchor voice with cat personality
   - Metadata includes voice settings and file info

4. **Video Production** → `video/`
   - Final MP4 videos combining script, voice, and visuals
   - Ready for upload to YouTube Shorts, Instagram Reels, TikTok
   - Complete packages with all assets

## 📊 File Naming Convention

- **Timestamp Format**: `YYYYMMDD_HHMMSS`
- **News Items**: `newsitem_YYYYMMDD_HHMMSS.json`
- **Scripts**: `script_[type]_YYYYMMDD_HHMMSS.txt`
- **Audio**: `audio_[script_name]_YYYYMMDD_HHMMSS.mp3`
- **Video**: `video_[audio_name]_YYYYMMDD_HHMMSS.mp4`
- **Metadata**: `[filename]_metadata.json`

## 🛠️ Content Management

Use the `ContentManager` class from `utils/content_manager.py` to:
- Automatically organize files in the correct directories
- Generate proper timestamps and metadata
- Link related files across the pipeline
- Track content creation workflow

## 📋 Content Browser

Run `scripts/content_browser.py` or use PowerShell menu option 12 to:
- View all content organized by type
- See the latest pipeline status
- Track file counts and sizes
- Identify what's ready for the next stage

## 🎯 Production Ready

This structure ensures:
- **Scalability**: Easy to manage hundreds of videos
- **Traceability**: Every file linked to its source
- **Organization**: Clear separation of content types
- **Automation**: Scripts automatically use the right directories
- **Metadata**: Complete information about generation settings
