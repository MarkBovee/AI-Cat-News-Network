#!/usr/bin/env python3
"""
Google Veo 3 Video Generator Demo
Demonstrates Google Veo 3 integration for AI Cat News Network
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.unified_video_generator import UnifiedVideoGenerator, list_video_providers
from config.settings import get_setting
import json

def main():
    print("🆕 Google Veo 3 Video Generator Demo")
    print("====================================")
    print()
    
    # Show provider information
    print("📋 Available Video Providers:")
    providers = list_video_providers()
    for provider in providers:
        status_emoji = "✅" if provider["status"] == "configured" else "❌"
        print(f"{status_emoji} {provider['name']} ({provider['provider']}) - {provider['pricing']}")
    print()
    
    # Check Google API key
    google_key = get_setting("GOOGLE_API_KEY")
    if not google_key:
        print("⚠️  Google API Key not found!")
        print("To use Google Veo 3, please:")
        print("1. Get a free API key from https://ai.google.dev/")
        print("2. Add GOOGLE_API_KEY=your_key_here to your .env file")
        print("3. Restart this demo")
        print()
        print("🔄 Running in demo mode with mock responses...")
        print()
    
    # Initialize Veo 3 generator
    try:
        generator = UnifiedVideoGenerator("veo3")
        provider_info = generator.get_provider_info()
        
        print(f"🎬 Using: {provider_info['name']}")
        print(f"📊 Status: {provider_info['status']}")
        print(f"💰 Pricing: {provider_info['pricing']}")
        print(f"🔧 Features: {', '.join(provider_info['features'])}")
        print()
        
    except Exception as e:
        print(f"❌ Error initializing Veo 3: {str(e)}")
        return
    
    # Cat news prompts for testing
    test_prompts = [
        "A professional orange tabby cat in a suit sitting at a news desk, reporting breaking news about a massive catnip shortage, serious expression, newsroom background",
        "A fluffy Persian cat meteorologist pointing at a weather map showing sunny conditions perfect for napping, wearing glasses and professional attire",
        "A sleek black cat financial expert explaining stock market trends with cat-themed charts and graphs in the background",
        "A maine coon cat sports anchor excitedly reporting on the latest cardboard box racing championship results"
    ]
    
    print("🎯 Available Cat News Scenarios:")
    for i, prompt in enumerate(test_prompts, 1):
        print(f"{i}. {prompt[:60]}...")
    print()
    
    # Get user choice
    try:
        choice = input("Choose a scenario (1-4) or press Enter for #1: ").strip()
        if not choice:
            choice = "1"
        choice_idx = int(choice) - 1
        
        if 0 <= choice_idx < len(test_prompts):
            selected_prompt = test_prompts[choice_idx]
        else:
            print("Invalid choice, using scenario 1")
            selected_prompt = test_prompts[0]
            
    except ValueError:
        print("Invalid input, using scenario 1")
        selected_prompt = test_prompts[0]
    
    print(f"🎬 Generating video with Google Veo 3...")
    print(f"📝 Prompt: {selected_prompt}")
    print()
    
    # Generate video
    try:
        result = generator.generate_video_from_prompt(selected_prompt, duration=5)
        
        print("📊 Generation Result:")
        print(f"Status: {result['status']}")
        print(f"Provider: {result.get('provider', 'unknown')}")
        
        if result['status'] == 'completed':
            print(f"✅ Video generated successfully!")
            print(f"📁 Video path: {result.get('video_path', 'N/A')}")
            print(f"🔗 Video URL: {result.get('video_url', 'N/A')}")
            print(f"⏱️  Duration: {result.get('duration', 5)} seconds")
            
        elif result['status'] == 'error':
            print(f"❌ Error: {result['message']}")
            if result.get('mock_video'):
                print("🎭 This was a mock response (API key not configured)")
                
        else:
            print(f"⏳ Status: {result['status']}")
            print(f"💬 Message: {result.get('message', 'Processing...')}")
            
    except Exception as e:
        print(f"❌ Error during video generation: {str(e)}")
    
    print()
    print("🔍 Veo 3 Features:")
    print("• Free tier available through Google AI Studio")
    print("• High-quality video generation")
    print("• 9:16 aspect ratio support for social media")
    print("• Integrated with Google's Gemini ecosystem")
    print("• Professional-grade results")
    print()
    print("🚀 To get started with Google Veo 3:")
    print("1. Visit https://ai.google.dev/")
    print("2. Sign up for a free account")
    print("3. Get your API key")
    print("4. Add it to your .env file as GOOGLE_API_KEY")
    print()
    print("✨ Demo completed!")

if __name__ == "__main__":
    main()
