#!/usr/bin/env python3
"""
Unified Quick Video Generator for AI Cat News Network
Creates script + voice + video with configurable text and duration
Usage: python create_quick_video.py "Your cat news text here" 6
"""
import os
import sys
import json
import time
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def create_quick_video(text, duration_seconds):
    """Create a complete video package with specified text and duration"""
    print(f"🎬 Quick Video Generator - {duration_seconds}s")
    print("=" * 50)
    
    # Validate inputs
    if not text or len(text.strip()) < 10:
        print("❌ Text must be at least 10 characters long")
        return False
    
    if duration_seconds < 3 or duration_seconds > 90:
        print("❌ Duration must be between 3 and 90 seconds")
        return False
    
    print(f"📝 Text: {text}")
    print(f"⏱️  Target duration: {duration_seconds} seconds")
    
    # Create timestamp for unique filenames
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    # Step 1: Create script file
    script_content = f"""**CAT NEWS QUICK UPDATE**
{text}
"""
    
    try:
        script_path = content_manager.save_script(script_content, script_type=f"quick_{duration_seconds}s")
        script_filename = os.path.basename(script_path)
        print(f"✅ Script saved: {script_filename}")
    except Exception as e:
        print(f"❌ Failed to save script: {e}")
        return False
    
    # Step 2: Generate voice-over
    print(f"\n🎤 Generating {duration_seconds}s voice-over...")
    
    # Check ElevenLabs configuration
    elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
    elevenlabs_voice_id = os.getenv('ELEVENLABS_VOICE_ID')
    
    if not elevenlabs_api_key:
        print("❌ ELEVENLABS_API_KEY not found in .env file")
        return False
    
    if not elevenlabs_voice_id:
        print("❌ ELEVENLABS_VOICE_ID not found in .env file")
        return False
    
    try:
        # Initialize ElevenLabs client
        client = ElevenLabs(api_key=elevenlabs_api_key)
        
        # Generate audio with ElevenLabs
        audio = client.text_to_speech.convert(
            voice_id=elevenlabs_voice_id,
            text=text,
            model_id="eleven_monolingual_v1"
        )
        
        # Save audio file
        audio_filename = f"audio_quick_{duration_seconds}s_{timestamp}.mp3"
        audio_path = f"content/audio/{audio_filename}"
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        
        # Save the audio (audio is bytes, write directly)
        with open(audio_path, 'wb') as f:
            for chunk in audio:
                f.write(chunk)
        print(f"✅ Audio saved: {audio_filename}")
        
        # Save audio metadata
        audio_metadata = {
            "timestamp": timestamp,
            "filename": audio_filename,
            "text": text,
            "target_duration": duration_seconds,
            "voice_id": elevenlabs_voice_id,
            "script_path": script_path
        }
        
        metadata_filename = f"audio_quick_{duration_seconds}s_{timestamp}_metadata.json"
        metadata_path = f"content/audio/{metadata_filename}"
        
        # Save metadata manually
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(audio_metadata, f, indent=2, ensure_ascii=False)
        
    except Exception as e:
        print(f"❌ Voice generation failed: {e}")
        return False
    
    # Step 3: Generate video based on configured provider
    video_provider = os.getenv('VIDEO_PROVIDER', 'hailuo')
    print(f"\n🎬 Generating video with {video_provider}...")
    
    if video_provider == 'hailuo':
        success = generate_hailuo_video(text, duration_seconds, timestamp, script_path, audio_path)
    elif video_provider == 'runway':
        success = generate_runway_video(text, duration_seconds, timestamp, script_path, audio_path)
    else:
        print(f"❌ Unsupported video provider: {video_provider}")
        return False
    
    if success:
        print(f"\n🎉 Quick video package created successfully!")
        print(f"📄 Script: {script_filename}")
        print(f"🎤 Audio: {audio_filename}")
        print(f"🎬 Video: Generation in progress...")
        return True
    else:
        print(f"\n❌ Video generation failed")
        return False

def generate_hailuo_video(text, duration_seconds, timestamp, script_path, audio_path):
    """Generate video using MiniMax Hailuo"""
    import requests
    
    # Check API key
    minimax_api_key = os.getenv('MINIMAX_API_KEY')
    if not minimax_api_key:
        print("❌ MINIMAX_API_KEY not found")
        return False
    
    # Get video settings
    resolution = os.getenv('VIDEO_RESOLUTION', '720p')
    aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    quality = os.getenv('VIDEO_QUALITY', 'high')
    
    # MiniMax is limited to 6 seconds max
    hailuo_duration = min(duration_seconds, 6)
    
    # Create cat news prompt
    video_prompt = f"""Professional cat news anchor in studio. Orange tabby cat in business suit at news desk. 
{text} Cat has serious expression, professional lighting, broadcast quality. {hailuo_duration} seconds."""
    
    # API request
    hailuo_request = {
        "model": "video-01",
        "prompt": video_prompt,
        "duration": hailuo_duration
    }
    
    print(f"📊 MiniMax Hailuo Settings:")
    print(f"    Duration: {hailuo_duration}s (max 6s)")
    print(f"    Resolution: {resolution}")
    print(f"    Quality: {quality}")
    print(f"    Cost: ~$0.10")
    
    try:
        url = "https://api.minimax.io/v1/video_generation"
        headers = {
            "Authorization": f"Bearer {minimax_api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=hailuo_request, headers=headers, timeout=30)
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Hailuo video generation started!")
            
            # Save metadata
            video_metadata = {
                "timestamp": timestamp,
                "provider": "minimax_hailuo",
                "text": text,
                "duration": hailuo_duration,
                "resolution": resolution,
                "quality": quality,
                "generation_id": result.get("id"),
                "api_response": result,
                "script_path": script_path,
                "audio_path": audio_path
            }
            
            metadata_path = f"content/video/hailuo_quick_{duration_seconds}s_{timestamp}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(video_metadata, f, indent=2, ensure_ascii=False)
            
            print(f"🆔 Generation ID: {result.get('id')}")
            return True
        else:
            print(f"❌ Hailuo API error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Hailuo generation error: {e}")
        return False

def generate_runway_video(text, duration_seconds, timestamp, script_path, audio_path):
    """Generate video using Runway ML"""
    import requests
    
    # Check API key
    runway_api_key = os.getenv('RUNWAY_API_KEY')
    if not runway_api_key or runway_api_key == 'your_runway_api_key_here':
        print("❌ RUNWAY_API_KEY not configured")
        return False
    
    # Get video settings
    resolution = os.getenv('VIDEO_RESOLUTION', '1080p')
    aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    quality = os.getenv('VIDEO_QUALITY', 'high')
    
    # Create cat news prompt
    video_prompt = f"""Professional cat news anchor in broadcast studio. Orange tabby cat in suit at news desk.
{text} Professional lighting, news graphics, {duration_seconds} seconds, 4K quality."""
    
    # API request
    runway_request = {
        "prompt": video_prompt,
        "model": "gen4",
        "duration": duration_seconds,
        "resolution": resolution,
        "aspect_ratio": aspect_ratio,
        "quality": quality
    }
    
    cost_estimate = (duration_seconds / 60) * 12
    print(f"📊 Runway ML Settings:")
    print(f"    Duration: {duration_seconds}s")
    print(f"    Resolution: {resolution}")
    print(f"    Quality: {quality}")
    print(f"    Cost: ~${cost_estimate:.2f}")
    
    try:
        url = "https://api.runwayml.com/v1/videos/generations"
        headers = {
            "Authorization": f"Bearer {runway_api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=runway_request, headers=headers, timeout=30)
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Runway video generation started!")
            
            # Save metadata
            video_metadata = {
                "timestamp": timestamp,
                "provider": "runway_ml",
                "text": text,
                "duration": duration_seconds,
                "resolution": resolution,
                "quality": quality,
                "estimated_cost": cost_estimate,
                "generation_id": result.get("id"),
                "api_response": result,
                "script_path": script_path,
                "audio_path": audio_path
            }
            
            metadata_path = f"content/video/runway_quick_{duration_seconds}s_{timestamp}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(video_metadata, f, indent=2, ensure_ascii=False)
            
            print(f"🆔 Generation ID: {result.get('id')}")
            return True
        else:
            print(f"❌ Runway API error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Runway generation error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_quick_video.py \"Your text here\" duration_seconds")
        print("Example: python create_quick_video.py \"Breaking: Cats demand more treats!\" 6")
        sys.exit(1)
    
    text = sys.argv[1]
    try:
        duration = int(sys.argv[2])
    except ValueError:
        print("Duration must be a number")
        sys.exit(1)
    
    success = create_quick_video(text, duration)
    if not success:
        sys.exit(1)
