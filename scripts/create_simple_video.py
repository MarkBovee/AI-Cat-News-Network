#!/usr/bin/env python3
"""
Simple Local Video Generator - AI Cat News Network
Creates basic cat news videos using MoviePy without complex AI dependencies
"""

import os
import sys
import json
import time
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from utils.content_manager import ContentManager

def create_simple_cat_video():
    """Create a simple cat news video with static images and audio"""
    
    print("🎬 Simple Local Video Generator - AI Cat News Network")
    print("=" * 60)
    
    # Load content manager
    content_manager = ContentManager()
    
    # Get latest script and audio files
    script_files = content_manager.get_latest_files("scripts", 3)  # Get more options
    audio_files = content_manager.get_latest_files("audio", 3)     # Get more options
    
    # Find the first valid audio file (non-zero size)
    script_path = script_files[0]["filepath"] if script_files else None
    audio_path = None
    
    for audio_file in audio_files:
        if os.path.getsize(audio_file["filepath"]) > 0:
            audio_path = audio_file["filepath"]
            break
    
    if not script_path or not audio_path:
        print("❌ Missing script or audio files")
        print("💡 Generate content first with create_quick_video.py")
        return False
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    print(f"🎤 Using audio: {os.path.basename(audio_path)}")
    
    # Load script content
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read().strip()
        print("✅ Script loaded successfully")
    except Exception as e:
        print(f"❌ Error reading script: {e}")
        return False
    
    # Create timestamp for output
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    try:
        print("🎬 Creating simple cat news video...")
        
        # Import MoviePy here to avoid issues if not installed
        from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ColorClip
        
        # Get audio duration
        audio_clip = AudioFileClip(audio_path)
        audio_duration = audio_clip.duration
        print(f"🎵 Audio duration: {audio_duration:.1f} seconds")
        
        # Create a simple colored background (news studio blue)
        background = ColorClip(size=(720, 1280), color=(20, 50, 100), duration=audio_duration)
        
        # Create title text
        title_text = TextClip("🐱 CAT NEWS NETWORK", 
                            fontsize=50, 
                            color='white', 
                            font='Arial-Bold',
                            size=(700, None))
        title_text = title_text.set_position(('center', 100)).set_duration(audio_duration)
        
        # Create news text (first part of script)
        news_text = script_content[:200] + "..." if len(script_content) > 200 else script_content
        content_text = TextClip(news_text,
                              fontsize=24,
                              color='white',
                              font='Arial',
                              size=(600, None),
                              method='caption')
        content_text = content_text.set_position(('center', 300)).set_duration(audio_duration)
        
        # Create anchor text
        anchor_text = TextClip("🐾 WHISKERS WINSTON, CAT NEWS ANCHOR",
                             fontsize=30,
                             color='yellow',
                             font='Arial-Bold',
                             size=(650, None))
        anchor_text = anchor_text.set_position(('center', 1000)).set_duration(audio_duration)
        
        # Composite all elements
        video = CompositeVideoClip([background, title_text, content_text, anchor_text])
        
        # Add audio
        video = video.set_audio(audio_clip)
        
        # Output path
        output_path = f"content/video/simple_cat_news_{timestamp}.mp4"
        
        print(f"🎬 Rendering video to: {output_path}")
        print("⏳ This may take a moment...")
        
        # Write video file
        video.write_videofile(output_path, 
                            fps=24,
                            codec='libx264',
                            audio_codec='aac',
                            temp_audiofile='temp-audio.m4a',
                            remove_temp=True,
                            verbose=False,
                            logger=None)
        
        # Clean up
        audio_clip.close()
        video.close()
        
        # Save metadata
        metadata = {
            "timestamp": timestamp,
            "provider": "simple_local",
            "model": "moviepy_text_video",
            "script_content": script_content,
            "audio_duration": audio_duration,
            "video_duration": audio_duration,
            "resolution": "720x1280",
            "format": "mp4",
            "script_path": script_path,
            "audio_path": audio_path,
            "video_path": output_path,
            "status": "completed"
        }
        
        metadata_path = f"content/video/simple_cat_news_{timestamp}_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Video created successfully!")
        print(f"📄 Video saved: {output_path}")
        print(f"📊 Metadata saved: {metadata_path}")
        print(f"🎵 Duration: {audio_duration:.1f} seconds")
        print(f"📐 Resolution: 720x1280 (9:16 vertical)")
        
        return True
        
    except ImportError as e:
        print(f"❌ MoviePy import error: {e}")
        print("💡 Make sure MoviePy is installed: pip install moviepy")
        return False
    except Exception as e:
        print(f"❌ Error creating video: {e}")
        return False

if __name__ == "__main__":
    success = create_simple_cat_video()
    if success:
        print("\n🎉 Simple cat news video created successfully!")
        print("💡 Check content/video/ folder for the MP4 file")
    else:
        print("\n❌ Video creation failed")
        sys.exit(1)
