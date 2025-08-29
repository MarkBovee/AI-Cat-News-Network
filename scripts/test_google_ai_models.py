#!/usr/bin/env python3
"""
Simple Google AI API Model Test - AI Cat News Network
Test what video models are available through Google AI API
"""

import requests
import subprocess
import json

def test_google_ai_api():
    """Test Google AI API for available video models"""
    
    print("🔍 Testing Google AI API for Video Models")
    print("=" * 50)
    
    # Read API key from .env
    api_key = None
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('GOOGLE_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    break
        
        if not api_key:
            print("❌ No GOOGLE_API_KEY found in .env")
            return
            
    except Exception as e:
        print(f"❌ Error reading .env: {e}")
        return
    
    print(f"✅ API Key found: {api_key[:20]}...")
    
    # Test different Google AI endpoints
    test_endpoints = [
        # Google AI API (ai.google.dev)
        "https://generativelanguage.googleapis.com/v1beta/models",
        # Vertex AI (cloud.google.com)
        "https://us-central1-aiplatform.googleapis.com/v1/projects/ai-cats-news/locations/us-central1/publishers/google/models"
    ]
    
    for i, endpoint in enumerate(test_endpoints, 1):
        print(f"\n🔍 Testing Endpoint {i}: {endpoint}")
        
        if "generativelanguage" in endpoint:
            # Google AI API
            params = {"key": api_key}
            headers = {}
        else:
            # Vertex AI
            headers = {"Authorization": f"Bearer {api_key}"}
            params = {}
        
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            print(f"📡 Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                models = data.get('models', [])
                
                print(f"✅ Found {len(models)} models")
                
                # Look for video models
                video_models = []
                for model in models:
                    name = model.get('name', '').lower()
                    display_name = model.get('displayName', '').lower()
                    
                    if any(keyword in name or keyword in display_name 
                           for keyword in ['veo', 'video', 'imagen']):
                        video_models.append({
                            'name': model.get('name', ''),
                            'displayName': model.get('displayName', ''),
                            'supportedMethods': model.get('supportedGenerationMethods', [])
                        })
                
                if video_models:
                    print(f"\n🎬 Video Models Found:")
                    for model in video_models:
                        print(f"   📹 {model['displayName']}")
                        print(f"      ID: {model['name']}")
                        print(f"      Methods: {model['supportedMethods']}")
                else:
                    print("⚠️ No video models found")
                    
                # Show first few models for reference
                print(f"\n📋 First 5 models (for reference):")
                for model in models[:5]:
                    print(f"   • {model.get('displayName', model.get('name', 'Unknown'))}")
                    
            else:
                print(f"❌ Error: {response.status_code}")
                error_text = response.text[:300]
                print(f"Response: {error_text}...")
                
        except Exception as e:
            print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    test_google_ai_api()
    
    print("\n" + "=" * 50)
    print("💡 Note: Google might have video models that require:")
    print("   • Billing enabled")
    print("   • Special API access")
    print("   • Different authentication")
    print("🔗 Check: https://ai.google.dev/ for latest models")
