#!/usr/bin/env python3
"""
Content Browser for AI Cat News Network
Shows organized content structure and recent files
"""
import os
import sys
from datetime import datetime

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

def format_timestamp(timestamp):
    """Convert timestamp to readable format"""
    try:
        dt = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return timestamp

def show_content_overview():
    """Display overview of all content"""
    print("🐱 AI Cat News Network - Content Browser")
    print("=" * 50)
    
    content_types = ["newsitems", "scripts", "audio", "video", "ideas"]
    
    for content_type in content_types:
        icon_map = {
            "newsitems": "📰",
            "scripts": "📝", 
            "audio": "🎤",
            "video": "🎬",
            "ideas": "💡"
        }
        
        icon = icon_map.get(content_type, "📁")
        files = content_manager.get_latest_files(content_type, limit=10)
        
        print(f"\n{icon} {content_type.upper()} ({len(files)} files)")
        print("-" * 30)
        
        if not files:
            print("   (no files yet)")
        else:
            for i, file_info in enumerate(files, 1):
                filename = file_info["filename"]
                modified = datetime.fromtimestamp(file_info["modified"])
                print(f"   {i:2d}. {filename}")
                print(f"       {modified.strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Show file size for media files
                if content_type in ["audio", "video"]:
                    try:
                        size_kb = os.path.getsize(file_info["filepath"]) / 1024
                        print(f"       {size_kb:.1f} KB")
                    except:
                        pass

def show_latest_pipeline():
    """Show the latest complete pipeline"""
    print(f"\n🔄 LATEST CONTENT PIPELINE")
    print("=" * 50)
    
    latest_news = content_manager.get_latest_files("newsitems", limit=1)
    latest_script = content_manager.get_latest_files("scripts", limit=1)
    latest_audio = content_manager.get_latest_files("audio", limit=1)
    latest_video = content_manager.get_latest_files("video", limit=1)
    
    if latest_news:
        print(f"📰 Latest News: {latest_news[0]['filename']}")
    if latest_script:
        print(f"📝 Latest Script: {latest_script[0]['filename']}")
    if latest_audio:
        print(f"🎤 Latest Audio: {latest_audio[0]['filename']}")
    if latest_video:
        print(f"🎬 Latest Video: {latest_video[0]['filename']}")
    else:
        print("🎬 No videos generated yet")
    
    # Calculate completion status
    pipeline_status = []
    if latest_news: pipeline_status.append("News ✅")
    if latest_script: pipeline_status.append("Script ✅") 
    if latest_audio: pipeline_status.append("Audio ✅")
    if latest_video: pipeline_status.append("Video ✅")
    
    print(f"\n📊 Pipeline Status: {' → '.join(pipeline_status)}")
    
    if not latest_video and latest_audio:
        print("💡 Ready for video generation!")

if __name__ == "__main__":
    show_content_overview()
    show_latest_pipeline()
    
    print(f"\n📁 Content Structure:")
    print(f"   content/")
    print(f"   ├── newsitems/    # Real news stories to cover")
    print(f"   ├── ideas/        # Content ideas and concepts") 
    print(f"   ├── scripts/      # Generated cat news scripts")
    print(f"   ├── audio/        # Voice-over files")
    print(f"   └── video/        # Final video productions")
