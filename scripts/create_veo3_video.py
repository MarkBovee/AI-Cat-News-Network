#!/usr/bin/env python3
"""
Google Veo 2 Video Generator - AI Cat News Network
Generate professional videos using Google's Veo 2 API via Vertex AI
"""

import os
import time
import json
import requests
from pathlib import Path
from datetime import datetime
import subprocess

def load_env_config():
    """Load configuration from .env file"""
    config = {}
    env_path = Path(".env")
    
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    
    return config

def get_access_token():
    """Get Google Cloud access token using gcloud CLI"""
    try:
        result = subprocess.run(
            [r'C:\Users\markb\scoop\shims\gcloud.cmd', 'auth', 'print-access-token'],
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )
        token = result.stdout.strip()
        print(f"✅ Using gcloud access token: {token[:20]}...")
        return token
        
    except Exception as e:
        print(f"❌ Could not get gcloud access token: {e}")
        return None

def get_project_id():
    """Get Google Cloud project ID"""
    try:
        result = subprocess.run(
            [r'C:\Users\markb\scoop\shims\gcloud.cmd', 'config', 'get-value', 'project'],
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )
        project_id = result.stdout.strip()
        print(f"📋 Using project: {project_id}")
        return project_id
        
    except Exception as e:
        print(f"❌ Could not get project ID: {e}")
        return None

def create_veo_video(prompt, access_token, project_id, model_id="veo-2"):
    """Generate video using Google Veo 2 API via Vertex AI"""
    
    if not access_token or not project_id:
        return None
    
    # API endpoint
    url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models/{model_id}:predictLongRunning"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    payload = {
        "instances": [
            {
                "prompt": prompt
            }
        ],
        "parameters": {
            "aspectRatio": "9:16",
            "durationSeconds": 8,
            "resolution": "1080p",
            "sampleCount": 1,
            "enhancePrompt": True,
            "generateAudio": True,
            "personGeneration": "allow_adult"
        }
    }
    
    print(f"🚀 Sending request to Veo 3.0...")
    print(f"📝 Prompt: {prompt[:100]}...")
    print(f"⚙️ Model: {model_id}")
    print(f"📐 Format: 9:16 vertical, 1080p, 8 seconds")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            operation_data = response.json()
            operation_name = operation_data.get("name")
            
            if operation_name:
                print(f"✅ Request accepted. Operation: {operation_name}")
                print("⏳ Video generation started. This typically takes 5-10 minutes...")
                
                # Save operation info
                metadata = {
                    "timestamp": timestamp,
                    "provider": "google_veo3",
                    "model": model_id,
                    "prompt": prompt,
                    "operation_name": operation_name,
                    "project_id": project_id,
                    "status": "started",
                    "check_command": f"gcloud ai operations describe {operation_name} --region=us-central1"
                }
                
                output_dir = Path("output")
                output_dir.mkdir(exist_ok=True)
                
                metadata_path = f"output/veo3_operation_{timestamp}.json"
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2)
                
                print(f"📊 Operation info saved: {metadata_path}")
                print("🔍 You can check status with:")
                print(f"   gcloud ai operations describe {operation_name} --region=us-central1")
                
                return metadata
            else:
                print("❌ No operation name returned")
                return None
        else:
            print(f"❌ API request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return None

def get_latest_script():
    """Get the latest script file"""
    script_dir = Path("content/scripts")
    if not script_dir.exists():
        return None
    
    script_files = list(script_dir.glob("*.txt"))
    if script_files:
        latest = max(script_files, key=lambda x: x.stat().st_mtime)
        return latest
    return None

def create_veo3_cat_news():
    """Main function to create Cat News video with Veo 3.0"""
    
    print("🌟 Google Veo 3.0 - AI Cat News Video Generator")
    print("=" * 55)
    
    # Get access token from gcloud
    access_token = get_access_token()
    if not access_token:
        print("❌ Could not get Google Cloud access token")
        return None
    
    # Get project ID
    project_id = get_project_id()
    if not project_id:
        print("❌ Could not get Google Cloud project ID")
        return None
    
    # Get script content
    script_path = get_latest_script()
    if not script_path:
        print("❌ No script found. Creating default content...")
        script_content = "Breaking Cat News: Local tabby discovers ultimate napping spot"
    else:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
        print(f"📝 Using script: {script_path.name}")
    
    # Create professional cat news prompt for Veo 3.0
    video_prompt = f"""Professional orange tabby cat news anchor wearing a navy blue business suit and red tie, sitting at a modern television news desk in a high-tech broadcast studio. The cat has intelligent amber eyes, perfectly groomed fur, and an authoritative yet friendly expression. Behind the cat are multiple large HD screens displaying "CAT NEWS NETWORK" in bold letters with breaking news graphics. The studio has warm, professional lighting with subtle blue and red accent colors. Modern broadcast equipment and cameras are visible in the background. The cat occasionally gestures with paws while delivering the news. Cinematic quality, broadcast television production value, professional news anchor presentation.

News Story: {script_content[:200]}"""
    
    print(f"🎯 Generated professional prompt for Veo 3.0")
    print(f"📺 Theme: Professional cat news broadcast")
    print(f"🎬 Quality: Cinematic, broadcast-grade")
    
    # Generate video
    result = create_veo_video(video_prompt, access_token, project_id)
    
    if result:
        print("\n🎉 Veo 3.0 Cat News Video Generation Started!")
        print("🎬 Professional AI-generated cat news broadcast")
        print("📱 Optimized for social media (9:16 vertical)")
        print("🔊 Audio generation included")
        print("🎯 Broadcast quality for Cat News Network")
        print("\n💡 Video will be ready in 5-10 minutes. Check status with the gcloud command above.")
        return result
    else:
        print("\n❌ Video generation failed")
        return None

if __name__ == "__main__":
    create_veo3_cat_news()
