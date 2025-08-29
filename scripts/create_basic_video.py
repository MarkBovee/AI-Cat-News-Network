#!/usr/bin/env python3
"""
Basic Video Generator - AI Cat News Network
Creates videos with audio and static images using just MoviePy
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

def create_basic_video():
    """Create a basic video with audio and static background"""
    
    print("🎬 Basic Video Generator - AI Cat News Network")
    print("=" * 55)
    
    # Load content manager
    content_manager = ContentManager()
    
    # Get latest script and audio files
    script_files = content_manager.get_latest_files("scripts", 3)
    audio_files = content_manager.get_latest_files("audio", 3)
    
    # Find valid files
    script_path = script_files[0]["filepath"] if script_files else None
    audio_path = None
    
    for audio_file in audio_files:
        if os.path.getsize(audio_file["filepath"]) > 0:
            audio_path = audio_file["filepath"]
            break
    
    if not script_path or not audio_path:
        print("❌ Missing valid script or audio files")
        return False
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    print(f"🎤 Using audio: {os.path.basename(audio_path)}")
    
    try:
        from moviepy.editor import AudioFileClip, ColorClip
        
        # Load audio
        audio_clip = AudioFileClip(audio_path)
        audio_duration = audio_clip.duration
        print(f"🎵 Audio duration: {audio_duration:.1f} seconds")
        
        # Create a simple solid color video (cat news studio blue)
        video_clip = ColorClip(size=(720, 1280), color=(25, 25, 112), duration=audio_duration)
        
        # Add audio to video
        video_with_audio = video_clip.set_audio(audio_clip)
        
        # Create output filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_path = f"content/video/basic_cat_news_{timestamp}.mp4"
        
        print(f"🎬 Creating video: {output_path}")
        print("⏳ Rendering...")
        
        # Write the video file
        video_with_audio.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            verbose=False,
            logger=None
        )
        
        # Clean up
        audio_clip.close()
        video_clip.close()
        video_with_audio.close()
        
        # Save metadata
        metadata = {
            "timestamp": timestamp,
            "provider": "basic_local",
            "model": "moviepy_basic",
            "audio_duration": audio_duration,
            "video_duration": audio_duration,
            "resolution": "720x1280",
            "format": "mp4",
            "script_path": script_path,
            "audio_path": audio_path,
            "video_path": output_path,
            "status": "completed"
        }
        
        metadata_path = f"content/video/basic_cat_news_{timestamp}_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Video created successfully!")
        print(f"📄 Video: {output_path}")
        print(f"📊 Metadata: {metadata_path}")
        print(f"🎵 Duration: {audio_duration:.1f} seconds")
        print(f"📐 Resolution: 720x1280 (9:16 vertical)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating video: {e}")
        return False

if __name__ == "__main__":
    success = create_basic_video()
    if success:
        print("\n🎉 Basic cat news video created successfully!")
        print("💡 Video saved in content/video/ folder")
        print("🎯 Next: Add HunyuanVideo or other AI video generation")
    else:
        print("\n❌ Video creation failed")
        sys.exit(1)
