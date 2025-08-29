#!/usr/bin/env python3
"""
Google Vertex AI Model Discovery - AI Cat News Network
List all available models to find the correct video generation options
"""

import requests
import subprocess
import json

def get_access_token():
    """Get Google Cloud access token"""
    try:
        result = subprocess.run(
            [r'C:\Users\markb\scoop\shims\gcloud.cmd', 'auth', 'print-access-token'],
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Could not get access token: {e}")
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
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Could not get project ID: {e}")
        return None

def list_vertex_ai_models():
    """List all available Vertex AI models"""
    
    access_token = get_access_token()
    project_id = get_project_id()
    
    if not access_token or not project_id:
        return None
    
    print(f"🔍 Discovering Vertex AI models in project: {project_id}")
    print("=" * 60)
    
    # Try different API endpoints for model discovery
    endpoints = [
        f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models",
        f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/models"
    ]
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    for i, url in enumerate(endpoints, 1):
        print(f"\n🔍 Endpoint {i}: {url}")
        try:
            response = requests.get(url, headers=headers)
            print(f"📡 Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                models = data.get('models', [])
                
                print(f"✅ Found {len(models)} models")
                
                # Filter for video-related models
                video_models = []
                for model in models:
                    model_name = model.get('name', '').lower()
                    display_name = model.get('displayName', '')
                    
                    if any(keyword in model_name for keyword in ['veo', 'video', 'imagen']):
                        video_models.append({
                            'name': model.get('name', ''),
                            'displayName': display_name,
                            'description': model.get('description', ''),
                            'supportedActions': model.get('supportedActions', [])
                        })
                
                if video_models:
                    print(f"\n🎬 Video Generation Models Found ({len(video_models)}):")
                    print("-" * 50)
                    for model in video_models:
                        print(f"📹 {model['displayName']}")
                        print(f"   Name: {model['name']}")
                        print(f"   Description: {model['description'][:100]}...")
                        print(f"   Actions: {model['supportedActions']}")
                        print()
                else:
                    print("⚠️ No video models found in this endpoint")
                    
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
    
    # Also try the publishers endpoint specifically for Google models
    print(f"\n🔍 Checking Google Publisher Models...")
    publisher_url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models"
    
    try:
        response = requests.get(publisher_url, headers=headers)
        print(f"📡 Publisher Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Publisher response received")
            
            # Look for any models with video capabilities
            if 'models' in data:
                for model in data['models']:
                    model_id = model.get('name', '').split('/')[-1]
                    if 'veo' in model_id.lower() or 'video' in model_id.lower():
                        print(f"🎥 Found: {model_id}")
                        print(f"   Full name: {model.get('name', '')}")
                        print(f"   Version: {model.get('versionId', 'N/A')}")
                        print()
        else:
            print(f"❌ Publisher error: {response.status_code}")
            print(f"Response: {response.text[:300]}...")
            
    except Exception as e:
        print(f"❌ Publisher request failed: {e}")

if __name__ == "__main__":
    print("🌟 Google Vertex AI Model Discovery")
    print("Searching for available video generation models...")
    print()
    
    list_vertex_ai_models()
    
    print("\n" + "=" * 60)
    print("💡 Note: If no video models are found, they may need to be")
    print("   enabled in the Google Cloud Console first.")
    print("🔗 Visit: https://console.cloud.google.com/vertex-ai/models")
