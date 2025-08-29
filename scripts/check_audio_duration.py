#!/usr/bin/env python3
"""
Audio Duration Checker and Video Prompt Adjuster
Checks audio duration and adjusts video generation accordingly
"""
import os
import sys
from mutagen.mp3 import MP3

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

def check_audio_duration():
    """Check the duration of our latest audio file"""
    print("🎤 Audio Duration Analysis")
    print("=" * 30)
    
    # Get latest audio file
    latest_audio = content_manager.get_latest_files("audio", limit=1)
    if not latest_audio:
        print("❌ No audio files found")
        return None
    
    audio_path = latest_audio[0]["filepath"]
    print(f"📄 Audio file: {os.path.basename(audio_path)}")
    
    try:
        # Get audio duration using mutagen
        audio = MP3(audio_path)
        duration = audio.info.length
        
        print(f"⏱️  Duration: {duration:.1f} seconds")
        print(f"📊 Size: {os.path.getsize(audio_path) / 1024:.1f} KB")
        
        return duration, audio_path
        
    except Exception as e:
        print(f"❌ Error reading audio: {e}")
        return None

def suggest_adjustments(duration):
    """Suggest adjustments based on audio duration"""
    print(f"\n🎯 Recommendations for {duration:.1f}s audio:")
    
    if duration < 15:
        print("📝 Audio is quite short - perfect for punchy social media!")
        print("💡 Video prompt: Quick, snappy cat news delivery")
        return f"Duration: {duration:.0f} seconds - rapid-fire cat news perfect for TikTok and Instagram Reels."
    
    elif duration <= 25:
        print("📝 Audio length is ideal for social media (15-25s)")
        print("💡 Video prompt: Standard cat news format")
        return f"Duration: {duration:.0f} seconds perfect for social media."
    
    elif duration <= 35:
        print("📝 Audio is good for YouTube Shorts (under 35s)")
        print("💡 Video prompt: Extended cat news format")
        return f"Duration: {duration:.0f} seconds ideal for YouTube Shorts."
    
    else:
        print("⚠️  Audio is quite long for social media (over 35s)")
        print("💡 Consider trimming or use for longer format")
        return f"Duration: {duration:.0f} seconds - extended format content."

if __name__ == "__main__":
    result = check_audio_duration()
    if result:
        duration, audio_path = result
        video_duration_text = suggest_adjustments(duration)
        
        print(f"\n🎬 Updated Video Prompt Duration:")
        print(f"'{video_duration_text}'")
        
        # Show the exact duration for updating our video script
        print(f"\n🔧 For create_video_veo3.py, use:")
        print(f"Duration: {duration:.0f} seconds")
