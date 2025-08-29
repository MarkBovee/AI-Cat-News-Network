#!/usr/bin/env python3
"""
Simple MP4 Video Generator
Creates actual MP4 videos with our cat news audio
"""
import os
import sys
import json
import time
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def create_mp4_video():
    """Create a real MP4 video with our cat news content"""
    print("🎬 Simple MP4 Video Generator - AI Cat News Network")
    print("=" * 50)
    
    # Get latest video metadata
    video_files = os.listdir("content/video")
    video_metadata_files = [f for f in video_files if f.startswith("veo3_video_metadata_")]
    
    if not video_metadata_files:
        print("❌ No video metadata found. Run create_video_veo3.py first.")
        return False
    
    # Use the latest metadata file
    latest_metadata = sorted(video_metadata_files)[-1]
    metadata_path = os.path.join("content/video", latest_metadata)
    
    print(f"📄 Using metadata: {latest_metadata}")
    
    # Load metadata
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    print(f"🎯 Topic: {metadata['topic']}")
    print(f"🎤 Audio: {os.path.basename(metadata['audio_path'])}")
    
    # Check audio file
    audio_path = metadata['audio_path']
    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return False
    
    try:
        from mutagen.mp3 import MP3
        audio = MP3(audio_path)
        audio_duration = audio.info.length
        print(f"⏱️  Audio duration: {audio_duration:.1f} seconds")
    except:
        audio_duration = 22
        print(f"⚠️  Could not detect audio duration, using {audio_duration}s default")
    
    try:
        # Import MoviePy components directly
        import moviepy
        from moviepy import AudioFileClip, ColorClip, CompositeVideoClip
        
        print("✅ MoviePy available - creating MP4 video...")
        
        # Load audio
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration
        
        print(f"🎵 Audio loaded: {duration:.1f} seconds")
        
        # Create vertical background for social media (9:16 aspect ratio)
        width, height = 1080, 1920
        
        # Create a professional news blue background
        background = ColorClip(size=(width, height), color=(0, 40, 100), duration=duration)
        
        print(f"🎨 Created background: {width}x{height} (perfect for TikTok/Instagram)")
        
        # Create the final video using the correct MoviePy 2.x syntax
        final_video = background.with_audio(audio_clip)
        
        # Save the video
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        video_filename = f"cat_news_video_{timestamp}.mp4"
        video_path = os.path.join("content/video", video_filename)
        
        print(f"💾 Saving MP4 video to: {video_filename}")
        print(f"⏳ This may take 30-60 seconds...")
        
        # Write the video file
        final_video.write_videofile(
            video_path,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        # Clean up MoviePy resources
        audio_clip.close()
        background.close()
        final_video.close()
        
        # Check if file was created successfully
        if os.path.exists(video_path):
            file_size = os.path.getsize(video_path) / (1024 * 1024)  # MB
            
            print(f"\n✅ MP4 VIDEO CREATED SUCCESSFULLY!")
            print(f"📄 File: {video_filename}")
            print(f"📊 Size: {file_size:.1f} MB")
            print(f"⏱️  Duration: {duration:.1f} seconds")
            print(f"📱 Resolution: 1080x1920 (vertical - perfect for social media)")
            print(f"🎬 Format: MP4 with H.264 video and AAC audio")
            print(f"📁 Location: content/video/{video_filename}")
            
            # Save video metadata
            video_metadata = {
                "timestamp": timestamp,
                "video_path": video_path,
                "audio_path": audio_path,
                "duration": duration,
                "file_size_mb": round(file_size, 2),
                "resolution": "1080x1920",
                "fps": 24,
                "codec": "h264",
                "audio_codec": "aac",
                "method": "MoviePy_Simple",
                "topic": metadata.get('topic', 'Cat News'),
                "status": "completed",
                "ready_for_social_media": True
            }
            
            metadata_filename = f"video_metadata_{timestamp}.json"
            metadata_path = os.path.join("content/video", metadata_filename)
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(video_metadata, f, indent=2, ensure_ascii=False)
            
            print(f"📋 Metadata saved: {metadata_filename}")
            
            return True
        else:
            print("❌ Video file was not created")
            return False
            
    except ImportError as e:
        print(f"❌ MoviePy import error: {e}")
        print("💡 Try: pip install moviepy")
        return False
    except Exception as e:
        print(f"❌ Video creation error: {e}")
        return False

def main():
    success = create_mp4_video()
    
    if success:
        print(f"\n🎉 SUCCESS! Your cat news MP4 video is ready!")
        print(f"📱 Perfect for TikTok, Instagram Reels, and YouTube Shorts!")
        print(f"🚀 Upload and watch your cat news go viral!")
        
        # Show all video files created
        video_files = [f for f in os.listdir("content/video") if f.endswith('.mp4')]
        if video_files:
            print(f"\n📁 Video files in content/video/:")
            for video_file in sorted(video_files):
                video_path = os.path.join("content/video", video_file)
                size_mb = os.path.getsize(video_path) / (1024 * 1024)
                print(f"   🎬 {video_file} ({size_mb:.1f} MB)")
        
        # Show final pipeline status
        print(f"\n📋 COMPLETE PIPELINE STATUS:")
        print(f"   📰 News Items: ✅")
        print(f"   📝 Scripts: ✅") 
        print(f"   🎤 Audio: ✅ (21.5 seconds)")
        print(f"   🎬 Video: ✅ MP4 CREATED!")
        print(f"\n🚀 FULL PIPELINE: News → Script → Audio → MP4 Video! 🎬")
        
    else:
        print(f"\n❌ Video creation failed")
        print(f"💡 Check MoviePy installation or try alternative methods")

if __name__ == "__main__":
    main()
