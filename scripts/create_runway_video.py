#!/usr/bin/env python3
"""
Runway ML Gen-4 Video Generator for AI Cat News Network
Creates professional long-form videos using Runway ML's Gen-4 model
- Up to 90 seconds duration
- 4K resolution capability  
- Cinematic quality output
- Perfect for matching 21.5-second audio content
"""
import os
import sys
import json
import time
import requests
from dotenv import load_dotenv
from mutagen.mp3 import MP3

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def generate_runway_video():
    """Generate professional video using Runway ML Gen-4 model"""
    print("🎬 Runway ML Gen-4 Video Generator - AI Cat News Network")
    print("=" * 65)
    
    # Check for Runway API key
    runway_api_key = os.getenv('RUNWAY_API_KEY')
    if not runway_api_key or runway_api_key == 'your_runway_api_key_here':
        print("❌ RUNWAY_API_KEY not found or not configured")
        print("💡 Add your Runway ML API key to .env file")
        print("🔗 Get your key from: https://runwayml.com/account/api-keys")
        print("💰 Pricing: ~$10-15 per minute of video generated")
        print("🎯 Features: Up to 90 seconds, 4K resolution, cinematic quality")
        return False
    
    print(f"🔑 Runway API Key: ✅ Found")
    
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
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
        print("✅ Script loaded successfully")
    except Exception as e:
        print(f"❌ Failed to read script: {e}")
        return False
    
    # Get audio duration for video length optimization
    try:
        audio = MP3(audio_path)
        audio_duration = audio.info.length
        print(f"⏱️  Audio duration: {audio_duration:.1f} seconds")
    except Exception as e:
        audio_duration = 22  # Default fallback
        print(f"⚠️  Could not detect audio duration, using {audio_duration}s default")
    
    # Get configurable video settings from environment
    config_duration = int(os.getenv('VIDEO_DURATION', '10'))
    config_resolution = os.getenv('VIDEO_RESOLUTION', '1080p')
    config_aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    config_quality = os.getenv('VIDEO_QUALITY', 'high')
    
    print(f"🎛️  Configuration Settings:")
    print(f"    Duration: {config_duration}s (from .env VIDEO_DURATION)")
    print(f"    Resolution: {config_resolution} (from .env VIDEO_RESOLUTION)")
    print(f"    Aspect Ratio: {config_aspect_ratio} (from .env VIDEO_ASPECT_RATIO)")
    print(f"    Quality: {config_quality} (from .env VIDEO_QUALITY)")
    
    # Use configured duration instead of audio-based calculation
    runway_duration = config_duration
    
    # Validate duration constraints (Runway ML supports up to 90 seconds)
    if runway_duration > 90:
        print(f"⚠️  Duration {runway_duration}s exceeds Runway ML limit of 90s, using 90s")
        runway_duration = 90
    elif runway_duration < 5:
        print(f"⚠️  Duration {runway_duration}s too short, using minimum 5s")
        runway_duration = 5
    
    print(f"🎬 Generating {runway_duration}-second professional cat news video...")
    
    # Create professional cat news video prompt optimized for Runway ML
    video_prompt = f"""Professional news studio with orange tabby cat wearing suit and tie at news desk. 
Cat anchor speaking directly to camera with confident expression. Modern broadcast studio lighting, 
professional news graphics in background. Shot: Medium close-up of cat anchor, 4K cinematic quality, 
broadcast television lighting, shallow depth of field. Cat has expressive eyes and professional demeanor.
News studio environment with subtle animation - gentle camera movements, professional atmosphere.
Duration: {runway_duration} seconds. Style: Professional broadcast television quality."""
    
    # Runway ML API request (try turbo model)
    runway_request = {
        "promptText": video_prompt,
        "model": "turbo",  # Try simple turbo model
        "duration": runway_duration,
        "ratio": config_aspect_ratio,
        "seed": 42
    }
    
    print("📋 Runway ML Request Details:")
    print(f"📊 Model: Gen-3 Alpha Turbo (Available)")
    print(f"📊 Duration: {runway_duration} seconds (configured)")
    print(f"📊 Resolution: {config_resolution} ({config_aspect_ratio} aspect ratio)")
    print(f"📊 Quality: {config_quality}")
    print(f"💰 Estimated cost: ~${(runway_duration/60) * 12:.2f}")
    
    # Show cost comparison for different durations
    print(f"💡 Cost comparison:")
    print(f"    5s = ~${(5/60) * 12:.2f} | 10s = ~${(10/60) * 12:.2f} | 20s = ~${(20/60) * 12:.2f} | 30s = ~${(30/60) * 12:.2f}")
    
    # Create timestamp for unique filenames
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    try:
        print("\n🚀 Sending request to Runway ML Gen-3 Alpha Turbo...")
        
        # Runway ML API endpoint (updated to correct dev endpoint)
        url = "https://api.dev.runwayml.com/v1/text_to_video"
        
        headers = {
            "Authorization": f"Bearer {runway_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Runway-Version": "2024-11-06"
        }
        
        response = requests.post(url, json=runway_request, headers=headers, timeout=30)
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Video generation request submitted successfully!")
            
            # Save the API response
            metadata = {
                "timestamp": timestamp,
                "provider": "runway_ml_gen4",
                "model": "gen4",
                "prompt": video_prompt,
                "audio_duration": audio_duration,
                "video_duration": runway_duration,
                "resolution": config_resolution,
                "aspect_ratio": config_aspect_ratio,
                "quality": config_quality,
                "estimated_cost": round((runway_duration/60) * 12, 2),
                "config_settings": {
                    "VIDEO_DURATION": config_duration,
                    "VIDEO_RESOLUTION": config_resolution,
                    "VIDEO_ASPECT_RATIO": config_aspect_ratio,
                    "VIDEO_QUALITY": config_quality
                },
                "generation_id": result.get("id"),
                "status": result.get("status"),
                "api_response": result,
                "script_path": script_path,
                "audio_path": audio_path
            }
            
            # Save metadata
            metadata_path = f"content/video/runway_video_result_{timestamp}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            print(f"📄 Metadata saved: {metadata_path}")
            print(f"🆔 Generation ID: {result.get('id')}")
            print(f"📊 Status: {result.get('status')}")
            
            # Check generation status
            generation_id = result.get("id")
            if generation_id:
                print(f"\n⏳ Monitoring generation progress...")
                check_runway_generation_status(generation_id, runway_api_key, timestamp)
            
            return True
            
        else:
            print(f"❌ API request failed with status code: {response.status_code}")
            print(f"📄 Response: {response.text}")
            
            # Save error response for debugging
            error_metadata = {
                "timestamp": timestamp,
                "provider": "runway_ml_gen4",
                "error": True,
                "status_code": response.status_code,
                "response": response.text,
                "request": runway_request
            }
            
            error_path = f"content/video/runway_error_{timestamp}.json"
            with open(error_path, 'w', encoding='utf-8') as f:
                json.dump(error_metadata, f, indent=2, ensure_ascii=False)
            print(f"❌ Error details saved: {error_path}")
            
            return False
            
    except requests.exceptions.Timeout:
        print("⏰ Request timed out. Runway ML might be busy.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"🌐 Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_runway_generation_status(generation_id, api_key, timestamp):
    """Check the status of a Runway ML video generation"""
    print(f"🔍 Checking status for generation: {generation_id}")
    
    url = f"https://api.dev.runwayml.com/v1/tasks/{generation_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "X-Runway-Version": "2024-11-06"
    }
    
    max_attempts = 60  # Check for up to 10 minutes
    attempt = 0
    
    while attempt < max_attempts:
        try:
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                status_data = response.json()
                status = status_data.get("status")
                
                print(f"📊 Status: {status}")
                
                if status == "completed":
                    print("✅ Video generation completed!")
                    
                    # Save final result
                    final_metadata = {
                        "timestamp": timestamp,
                        "provider": "runway_ml_gen4",
                        "generation_id": generation_id,
                        "status": "completed",
                        "video_url": status_data.get("video_url"),
                        "final_response": status_data
                    }
                    
                    final_path = f"content/video/runway_final_{timestamp}.json"
                    with open(final_path, 'w', encoding='utf-8') as f:
                        json.dump(final_metadata, f, indent=2, ensure_ascii=False)
                    
                    print(f"🎬 Video URL: {status_data.get('video_url')}")
                    print(f"📄 Final metadata saved: {final_path}")
                    break
                    
                elif status == "failed":
                    print("❌ Video generation failed!")
                    break
                    
                elif status in ["pending", "processing"]:
                    print(f"⏳ Still processing... (attempt {attempt + 1}/{max_attempts})")
                    time.sleep(10)  # Wait 10 seconds before next check
                    
                else:
                    print(f"❓ Unknown status: {status}")
                    
            else:
                print(f"❌ Status check failed: {response.status_code}")
                break
                
        except Exception as e:
            print(f"❌ Error checking status: {e}")
            break
            
        attempt += 1
    
    if attempt >= max_attempts:
        print("⏰ Status check timed out. Generation may still be processing.")

if __name__ == "__main__":
    success = generate_runway_video()
    if success:
        print("\n🎉 Runway ML video generation initiated successfully!")
        print("💡 Check the content/video/ folder for results")
    else:
        print("\n❌ Runway ML video generation failed")
        sys.exit(1)
