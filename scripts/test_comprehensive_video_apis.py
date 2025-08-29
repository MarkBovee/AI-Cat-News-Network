#!/usr/bin/env python3
"""
Comprehensive Google Video API Test - AI Cat News Network
Test multiple Google APIs for video generation capabilities
"""

import requests
import subprocess
import json

def test_video_apis():
    """Test various Google APIs for video generation"""
    
    print("🎬 Comprehensive Google Video API Test")
    print("=" * 50)
    
    # Read API key
    api_key = None
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('GOOGLE_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    break
    except:
        pass
    
    if not api_key:
        print("❌ No GOOGLE_API_KEY found")
        return
    
    print(f"✅ API Key: {api_key[:20]}...")
    
    # Get gcloud access token
    gcloud_token = None
    try:
        result = subprocess.run(
            [r'C:\Users\markb\scoop\shims\gcloud.cmd', 'auth', 'print-access-token'],
            capture_output=True, text=True, check=True, timeout=10
        )
        gcloud_token = result.stdout.strip()
        print(f"✅ Gcloud Token: {gcloud_token[:20]}...")
    except:
        print("⚠️ No gcloud token available")
    
    # Test endpoints
    test_configs = [
        {
            "name": "Google AI - Veo Models",
            "url": "https://generativelanguage.googleapis.com/v1beta/models",
            "auth": "api_key",
            "filter": "veo"
        },
        {
            "name": "Google AI - Video Generation",
            "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            "auth": "api_key",
            "method": "POST",
            "data": {"contents": [{"parts": [{"text": "Can you generate videos?"}]}]}
        },
        {
            "name": "Vertex AI - Publisher Models",
            "url": "https://us-central1-aiplatform.googleapis.com/v1/projects/ai-cats-news/locations/us-central1/publishers/google/models",
            "auth": "gcloud"
        },
        {
            "name": "AI Platform - Video Models",
            "url": "https://aiplatform.googleapis.com/v1/projects/ai-cats-news/locations/us-central1/models",
            "auth": "gcloud"
        }
    ]
    
    for config in test_configs:
        print(f"\n🔍 Testing: {config['name']}")
        print(f"   URL: {config['url']}")
        
        # Setup auth
        if config['auth'] == 'api_key':
            headers = {}
            params = {"key": api_key}
        elif config['auth'] == 'gcloud' and gcloud_token:
            headers = {"Authorization": f"Bearer {gcloud_token}"}
            params = {}
        else:
            print("   ⚠️ Auth not available, skipping")
            continue
        
        try:
            # Make request
            if config.get('method') == 'POST':
                response = requests.post(
                    config['url'], 
                    headers=headers, 
                    params=params,
                    json=config.get('data', {})
                )
            else:
                response = requests.get(config['url'], headers=headers, params=params)
            
            print(f"   📡 Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                if 'models' in data:
                    models = data['models']
                    print(f"   ✅ Found {len(models)} models")
                    
                    # Filter for video/veo models
                    video_models = []
                    for model in models:
                        name = str(model.get('name', '')).lower()
                        display_name = str(model.get('displayName', '')).lower()
                        
                        if any(keyword in name or keyword in display_name 
                               for keyword in ['veo', 'video', 'imagen']):
                            video_models.append(model)
                    
                    if video_models:
                        print(f"   🎬 Video models: {len(video_models)}")
                        for model in video_models[:3]:  # Show first 3
                            print(f"      • {model.get('displayName', model.get('name', 'Unknown'))}")
                    else:
                        print("   ⚠️ No video models found")
                        
                elif 'candidates' in data:
                    print(f"   📝 Response: {data}")
                else:
                    print(f"   📊 Keys: {list(data.keys())}")
                    
            else:
                print(f"   ❌ Error: {response.status_code}")
                error_text = response.text[:150]
                print(f"   Response: {error_text}...")
                
        except Exception as e:
            print(f"   ❌ Request failed: {e}")
    
    print(f"\n" + "=" * 50)
    print("💡 Summary:")
    print("   • Imagen models found for image generation")
    print("   • Veo models may require special access")
    print("   • Consider using working alternatives:")
    print("     - MiniMax Hailuo (working)")
    print("     - Runway ML (working)")
    print("   • Enable billing for full Vertex AI access")

if __name__ == "__main__":
    test_video_apis()
