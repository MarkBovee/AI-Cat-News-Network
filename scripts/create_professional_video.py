#!/usr/bin/env python3
"""
Professional Quick Video Generator for AI Cat News Network
Creates complete video packages with professional scripts optimized for AI video generation
"""
import os
import sys
import json
import time
import subprocess
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def create_professional_video_package(news_text, duration_seconds):
    """Create a complete professional video package with optimized script"""
    print(f"🎬 Professional Video Package Generator - {duration_seconds}s")
    print("=" * 60)
    
    # Validate inputs
    if not news_text or len(news_text.strip()) < 10:
        print("❌ News text must be at least 10 characters long")
        return False
    
    if duration_seconds < 3 or duration_seconds > 30:
        print("❌ Duration must be between 3 and 30 seconds")
        return False
    
    print(f"📰 News: {news_text}")
    print(f"⏱️  Duration: {duration_seconds} seconds")
    
    # Step 1: Generate professional script
    print(f"\n📝 Step 1: Creating professional video script...")
    try:
        result = subprocess.run([
            sys.executable, 
            "scripts/create_professional_script.py", 
            news_text, 
            str(duration_seconds)
        ], capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode != 0:
            print(f"❌ Script generation failed: {result.stderr}")
            return False
        
        print("✅ Professional script created")
        
    except Exception as e:
        print(f"❌ Script generation error: {e}")
        return False
    
    # Step 2: Get the latest script
    latest_scripts = content_manager.get_latest_files("scripts", limit=1)
    if not latest_scripts:
        print("❌ No script found after generation")
        return False
    
    script_path = latest_scripts[0]["filepath"]
    script_filename = os.path.basename(script_path)
    print(f"📄 Using script: {script_filename}")
    
    # Step 3: Generate video based on configured provider
    video_provider = os.getenv('VIDEO_PROVIDER', 'hailuo')
    print(f"\n🎬 Step 2: Generating video with {video_provider}...")
    
    if video_provider == 'hailuo':
        success = generate_hailuo_video_from_script(script_path, duration_seconds)
    elif video_provider == 'runway':
        success = generate_runway_video_from_script(script_path, duration_seconds)
    else:
        print(f"❌ Unsupported video provider: {video_provider}")
        return False
    
    if success:
        print(f"\n🎉 Professional video package created successfully!")
        print(f"📄 Script: {script_filename}")
        print(f"🎬 Video: Generation completed/in progress")
        print(f"💡 Check content/video/ for results")
        return True
    else:
        print(f"\n❌ Video generation failed")
        return False

def generate_hailuo_video_from_script(script_path, duration_seconds):
    """Generate video using MiniMax Hailuo with professional script"""
    import requests
    
    # Check API key
    minimax_api_key = os.getenv('MINIMAX_API_KEY')
    if not minimax_api_key:
        print("❌ MINIMAX_API_KEY not found")
        return False
    
    # Read the professional script
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except Exception as e:
        print(f"❌ Failed to read script: {e}")
        return False
    
    # Extract visual description for video prompt (use the detailed script as prompt)
    video_prompt = script_content
    
    # Get video settings
    resolution = os.getenv('VIDEO_RESOLUTION', '768P')
    aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    
    # MiniMax is limited to 6 seconds max
    hailuo_duration = min(duration_seconds, 6)
    
    # API request with professional script
    hailuo_request = {
        "model": "video-01",
        "prompt": video_prompt,
        "duration": hailuo_duration
    }
    
    print(f"📊 MiniMax Hailuo Professional Settings:")
    print(f"    Duration: {hailuo_duration}s")
    print(f"    Resolution: {resolution}")
    print(f"    Script length: {len(video_prompt)} characters")
    print(f"    Cost: ~$0.10")
    
    try:
        url = "https://api.minimax.io/v1/video_generation"
        headers = {
            "Authorization": f"Bearer {minimax_api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=hailuo_request, headers=headers, timeout=30)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Professional Hailuo video generation started!")
            
            # Save metadata
            video_metadata = {
                "timestamp": timestamp,
                "provider": "minimax_hailuo_professional",
                "script_path": script_path,
                "duration": hailuo_duration,
                "resolution": resolution,
                "professional_script": True,
                "generation_id": result.get("id"),
                "api_response": result
            }
            
            metadata_path = f"content/video/hailuo_professional_{duration_seconds}s_{timestamp}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(video_metadata, f, indent=2, ensure_ascii=False)
            
            print(f"🆔 Generation ID: {result.get('id')}")
            print(f"📄 Metadata: {os.path.basename(metadata_path)}")
            return True
        else:
            print(f"❌ Hailuo API error: {response.status_code}")
            print(f"Response: {response.text}")
            
            # Save error for debugging
            error_metadata = {
                "timestamp": timestamp,
                "provider": "minimax_hailuo_professional",
                "error": True,
                "status_code": response.status_code,
                "response": response.text,
                "script_path": script_path
            }
            
            error_path = f"content/video/hailuo_error_{timestamp}.json"
            with open(error_path, 'w', encoding='utf-8') as f:
                json.dump(error_metadata, f, indent=2, ensure_ascii=False)
            
            return False
            
    except Exception as e:
        print(f"❌ Hailuo generation error: {e}")
        return False

def generate_runway_video_from_script(script_path, duration_seconds):
    """Generate video using Runway ML with professional script"""
    import requests
    
    # Check API key
    runway_api_key = os.getenv('RUNWAY_API_KEY')
    if not runway_api_key or runway_api_key == 'your_runway_api_key_here':
        print("❌ RUNWAY_API_KEY not configured")
        return False
    
    # Read the professional script
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except Exception as e:
        print(f"❌ Failed to read script: {e}")
        return False
    
    # Use the professional script as video prompt
    video_prompt = script_content
    
    # Get video settings
    resolution = os.getenv('VIDEO_RESOLUTION', '1080p')
    aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
    quality = os.getenv('VIDEO_QUALITY', 'high')
    
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
    print(f"📊 Runway ML Professional Settings:")
    print(f"    Duration: {duration_seconds}s")
    print(f"    Resolution: {resolution}")
    print(f"    Quality: {quality}")
    print(f"    Script length: {len(video_prompt)} characters")
    print(f"    Cost: ~${cost_estimate:.2f}")
    
    try:
        url = "https://api.runwayml.com/v1/videos/generations"
        headers = {
            "Authorization": f"Bearer {runway_api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=runway_request, headers=headers, timeout=30)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Professional Runway video generation started!")
            
            # Save metadata
            video_metadata = {
                "timestamp": timestamp,
                "provider": "runway_ml_professional",
                "script_path": script_path,
                "duration": duration_seconds,
                "resolution": resolution,
                "quality": quality,
                "professional_script": True,
                "estimated_cost": cost_estimate,
                "generation_id": result.get("id"),
                "api_response": result
            }
            
            metadata_path = f"content/video/runway_professional_{duration_seconds}s_{timestamp}.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(video_metadata, f, indent=2, ensure_ascii=False)
            
            print(f"🆔 Generation ID: {result.get('id')}")
            print(f"📄 Metadata: {os.path.basename(metadata_path)}")
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
        print("Usage: python create_professional_video.py \"News text here\" duration_seconds")
        print("Example: python create_professional_video.py \"Breaking: Cats demand more treats!\" 6")
        sys.exit(1)
    
    news_text = sys.argv[1]
    try:
        duration = int(sys.argv[2])
    except ValueError:
        print("Duration must be a number")
        sys.exit(1)
    
    success = create_professional_video_package(news_text, duration)
    if not success:
        sys.exit(1)
