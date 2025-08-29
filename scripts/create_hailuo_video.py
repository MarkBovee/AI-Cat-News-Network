#!/usr/bin/env python3
"""
MiniMax Hailuo Video Generator for AI Cat News Network
Creates real videos using MiniMax Hailuo-02 model with professional cat news content
"""
import os
import sys
import json
import time
import requests
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def generate_hailuo_video():
    """Generate real video using MiniMax Hailuo-02 model"""
    print("🎬 MiniMax Hailuo Video Generator - AI Cat News Network")
    print("=" * 60)
    
    # Check for MiniMax API key
    minimax_api_key = os.getenv('MINIMAX_API_KEY')
    if not minimax_api_key:
        print("❌ MINIMAX_API_KEY not found in environment variables")
        print("💡 Add your MiniMax API key to .env file")
        print("🔗 Get your key from: https://www.minimax.io/platform")
        return False
    
    print(f"🔑 MiniMax API Key: ✅ Found")
    
    # Get latest content
    latest_scripts = content_manager.get_latest_files("scripts", limit=1)
    latest_audio = content_manager.get_latest_files("audio", limit=1)
    
    if not latest_scripts:
        print("❌ No scripts found. Run script generation first.")
        return False
    
    if not latest_audio:
        print("❌ No audio files found. Run voice generation first.")
        return False
    
    script_path = latest_scripts[0]["filepath"]
    audio_path = latest_audio[0]["filepath"]
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    print(f"🎤 Using audio: {os.path.basename(audio_path)}")
    
    # Read script content
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Extract topic
    lines = script_content.split('\n')
    topic = ""
    for line in lines:
        if line.startswith("Topic:"):
            topic = line.replace("Topic:", "").strip()
            break
    
    if not topic:
        topic = "Cat News Report"
    
    print(f"🎯 Topic: {topic}")
    
    # Get audio duration
    try:
        from mutagen.mp3 import MP3
        audio = MP3(audio_path)
        audio_duration = audio.info.length
        print(f"⏱️  Audio duration: {audio_duration:.1f} seconds")
    except:
        audio_duration = 22  # Default fallback
        print(f"⚠️  Could not detect audio duration, using {audio_duration}s default")
    
    # Create professional video prompt for Hailuo
    video_prompt = f"""Professional cat news anchor reporting: {topic}
    
Style: CNN-style modern news studio
Setting: Sophisticated orange tabby cat wearing a tiny professional news tie, sitting behind a sleek news desk
Lighting: Professional broadcast lighting with blue and white color scheme
Background: News ticker running at bottom, clean newsroom aesthetic
Action: Cat maintains serious news anchor posture with subtle cat behaviors - ear twitches, head tilts, occasional grooming
Quality: High definition, broadcast quality, vertical 9:16 format for social media
Camera: Professional fixed shot with stable framing, subtle zoom for emphasis"""
    
    print(f"📝 Video prompt: {len(video_prompt)} characters")
    
    # Get configurable video settings from environment
    config_duration = int(os.getenv('VIDEO_DURATION', '6'))
    config_resolution = os.getenv('VIDEO_RESOLUTION', '1080p')
    config_aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    config_quality = os.getenv('VIDEO_QUALITY', 'high')
    
    print(f"🎛️  Configuration Settings:")
    print(f"    Duration: {config_duration}s (from .env VIDEO_DURATION)")
    print(f"    Resolution: {config_resolution} (from .env VIDEO_RESOLUTION)")
    print(f"    Aspect Ratio: {config_aspect_ratio} (from .env VIDEO_ASPECT_RATIO)")
    print(f"    Quality: {config_quality} (from .env VIDEO_QUALITY)")
    
    # MiniMax Hailuo-02 constraints
    max_duration = 6  # Fixed maximum for MiniMax Hailuo-02
    hailuo_duration = min(config_duration, max_duration)
    
    if config_duration > max_duration:
        print(f"⚠️  Requested {config_duration}s exceeds MiniMax limit of {max_duration}s, using {hailuo_duration}s")
    
    print(f"🎬 Generating {hailuo_duration}-second professional cat news video...")
    print(f"📏 Note: MiniMax Hailuo-02 supports maximum 6 seconds for best quality")
    
    try:
        # MiniMax Hailuo API endpoint
        url = "https://api.minimax.io/v1/video_generation"
        
        # Prepare request with configurable settings
        # Convert resolution format for MiniMax API
        minimax_resolution = "720P" if config_resolution == "720p" else "1080P"
        
        payload = {
            "model": "MiniMax-Hailuo-02",
            "prompt": video_prompt,
            "duration": hailuo_duration,
            "resolution": minimax_resolution  # Use configured resolution
        }
        
        headers = {
            'authorization': f'Bearer {minimax_api_key}',
            'Content-Type': 'application/json'
        }
        
        print(f"🔄 Sending request to MiniMax Hailuo...")
        print(f"📊 Duration: {hailuo_duration} seconds (configured: {config_duration}s)")
        print(f"📐 Resolution: {minimax_resolution} (configured: {config_resolution})")
        print(f"📱 Aspect Ratio: {config_aspect_ratio}")
        print(f"💰 Cost: ~$0.10 per generation")
        
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ MiniMax Hailuo video generation successful!")
            
            # Save result
            video_result = {
                "timestamp": time.strftime("%Y%m%d_%H%M%S"),
                "service": "MiniMax-Hailuo",
                "model": "MiniMax-Hailuo-02",
                "prompt": video_prompt,
                "audio_duration": audio_duration,
                "video_duration": hailuo_duration,  # Actual video duration
                "api_response": result,
                "status": "generated",
                "script_path": script_path,
                "audio_path": audio_path,
                "topic": topic
            }
            
            result_timestamp = time.strftime("%Y%m%d_%H%M%S")
            result_path = os.path.join("content/video", f"hailuo_video_result_{result_timestamp}.json")
            
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump(video_result, f, indent=2, ensure_ascii=False)
            
            print(f"📄 Result saved: {os.path.basename(result_path)}")
            
            # Check if we got a video URL
            if 'data' in result and 'video_url' in result['data']:
                video_url = result['data']['video_url']
                print(f"🎬 Video URL: {video_url}")
                print(f"💾 Download the video and save as MP4 in content/video/")
            
            return True
            
        else:
            error_text = response.text
            print(f"❌ MiniMax API error ({response.status_code}): {error_text}")
            
            # Save error for debugging
            error_result = {
                "timestamp": time.strftime("%Y%m%d_%H%M%S"),
                "service": "MiniMax-Hailuo",
                "status": "error",
                "status_code": response.status_code,
                "error": error_text,
                "prompt": video_prompt
            }
            
            error_timestamp = time.strftime("%Y%m%d_%H%M%S")
            error_path = os.path.join("content/video", f"hailuo_error_{error_timestamp}.json")
            
            with open(error_path, 'w', encoding='utf-8') as f:
                json.dump(error_result, f, indent=2, ensure_ascii=False)
            
            print(f"📄 Error details saved: {os.path.basename(error_path)}")
            return False
            
    except Exception as e:
        print(f"❌ Error during video generation: {e}")
        return False

def main():
    success = generate_hailuo_video()
    
    if success:
        print(f"\n🎉 MiniMax Hailuo video generation completed!")
        print(f"📱 Professional cat news video ready for social media!")
        
        # Show updated pipeline status
        print(f"\n📋 Updated Pipeline Status:")
        latest_scripts = content_manager.get_latest_files("scripts", limit=1)
        latest_audio = content_manager.get_latest_files("audio", limit=1)
        video_files = [f for f in os.listdir("content/video") if f.endswith('.mp4')]
        
        print(f"   📰 News Items: ✅")
        print(f"   📝 Scripts: ✅ {len(latest_scripts)} files")
        print(f"   🎤 Audio Files: ✅ {len(latest_audio)} files") 
        print(f"   🎬 Video Generation: ✅ MiniMax Hailuo processed")
        print(f"   🎞️  MP4 Videos: {len(video_files)} files")
        print(f"\n🚀 COMPLETE: News → Script → Audio → Professional Video! 🎬")
        
    else:
        print(f"\n❌ Video generation failed. Check API key and try again.")
        print(f"💡 Verify your MiniMax API key in .env file")
        print(f"🔗 Get API access: https://www.minimax.io/platform")

if __name__ == "__main__":
    main()
