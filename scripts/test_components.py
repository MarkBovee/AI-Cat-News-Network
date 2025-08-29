#!/usr/bin/env python3
"""
Individual Component Tester
Quick tests for individual components with output inspection
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.ai_provider import ai_provider
from config.settings import get_setting
from tools.unified_video_generator import UnifiedVideoGenerator

def test_script_component():
    """Test just the script generation component"""
    print("📝 Testing Script Generation Component")
    print("=" * 40)
    
    # Create output directory
    output_dir = Path("component_tests/script_generation")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    topic = "Breaking: Scientists Discover Cats Have Been Running Secret Government"
    
    try:
        # Check configuration
        groq_key = get_setting("GROQ_API_KEY")
        print(f"Groq API: {'✅ Configured' if groq_key else '❌ Missing'}")
        
        if not groq_key:
            print("⚠️  Add GROQ_API_KEY to .env file to test script generation")
            return
        
        # Generate script
        prompt = f"""
        Create a 30-second cat news script about: {topic}
        
        Include:
        - Catchy headline
        - Professional cat anchor name
        - 4 time segments (0-5s, 5-15s, 15-25s, 25-30s)
        - Visual cues for each segment
        - Video generation prompt
        """
        
        print(f"Topic: {topic}")
        print("Generating script...")
        
        response = ai_provider.generate_content(prompt, max_tokens=600, temperature=0.7)
        
        # Save raw response
        timestamp = datetime.now().strftime("%H%M%S")
        raw_file = output_dir / f"raw_response_{timestamp}.txt"
        with open(raw_file, 'w', encoding='utf-8') as f:
            f.write(response)
        
        # Save structured data
        structured_data = {
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "raw_response": response,
            "word_count": len(response.split()),
            "character_count": len(response)
        }
        
        json_file = output_dir / f"script_data_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(structured_data, f, indent=2)
        
        print(f"✅ Script generated!")
        print(f"📁 Raw response: {raw_file}")
        print(f"📁 Structured data: {json_file}")
        print(f"📊 Words: {structured_data['word_count']}, Characters: {structured_data['character_count']}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_video_component():
    """Test just the video generation component"""
    print("🎥 Testing Video Generation Component")
    print("=" * 40)
    
    # Create output directory
    output_dir = Path("component_tests/video_generation")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    prompt = "A professional orange tabby cat in a business suit sitting at a news desk, serious expression, newsroom background with graphics"
    
    try:
        # Test both providers
        providers = ["veo3", "minimax"]
        
        for provider in providers:
            print(f"\n🎬 Testing {provider.upper()}...")
            
            generator = UnifiedVideoGenerator(provider)
            info = generator.get_provider_info()
            
            print(f"Status: {info['status']}")
            print(f"Features: {', '.join(info['features'])}")
            
            # Test generation
            result = generator.generate_video_from_prompt(prompt, duration=5)
            
            # Save result
            timestamp = datetime.now().strftime("%H%M%S")
            result_file = output_dir / f"{provider}_result_{timestamp}.json"
            with open(result_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            
            print(f"Result: {result['status']}")
            print(f"📁 Saved to: {result_file}")
            
            if result['status'] == 'error' and result.get('mock_video'):
                print("💡 This is expected if API key not configured")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_voice_component():
    """Test just the voice generation component"""
    print("🎤 Testing Voice Generation Component")
    print("=" * 40)
    
    # Create output directory
    output_dir = Path("component_tests/voice_generation")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    script_text = "Good evening, I'm Whiskers Winston with breaking cat news. Scientists have discovered that cats have been secretly running the government all along. More on this purr-fect story after these messages."
    
    try:
        # Check ElevenLabs configuration
        elevenlabs_key = get_setting("ELEVENLABS_API_KEY")
        voice_id = get_setting("ELEVENLABS_VOICE_ID", "2ajXGJNYBR0iNHpS4VZb")
        
        print(f"ElevenLabs API: {'✅ Configured' if elevenlabs_key else '❌ Missing'}")
        print(f"Voice ID: {voice_id}")
        print(f"Script length: {len(script_text)} characters")
        
        # Save script text
        timestamp = datetime.now().strftime("%H%M%S")
        script_file = output_dir / f"script_text_{timestamp}.txt"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_text)
        
        # Voice configuration data
        voice_data = {
            "script_text": script_text,
            "voice_id": voice_id,
            "elevenlabs_configured": bool(elevenlabs_key),
            "script_stats": {
                "characters": len(script_text),
                "words": len(script_text.split()),
                "estimated_duration": len(script_text.split()) * 0.5
            },
            "timestamp": datetime.now().isoformat()
        }
        
        config_file = output_dir / f"voice_config_{timestamp}.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(voice_data, f, indent=2)
        
        print(f"📁 Script saved: {script_file}")
        print(f"📁 Config saved: {config_file}")
        
        if elevenlabs_key:
            print("✅ Ready for voice generation!")
        else:
            print("⚠️  Add ELEVENLABS_API_KEY to .env file for voice generation")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_integration_component():
    """Test component integration"""
    print("🔗 Testing Component Integration")
    print("=" * 40)
    
    # Create output directory
    output_dir = Path("component_tests/integration")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Check all configurations
        configs = {
            "Groq API (Script)": get_setting("GROQ_API_KEY"),
            "Google API (Video)": get_setting("GOOGLE_API_KEY"),
            "MiniMax API (Video Alt)": get_setting("MINIMAX_API_KEY"),
            "ElevenLabs API (Voice)": get_setting("ELEVENLABS_API_KEY"),
        }
        
        print("Configuration Status:")
        ready_components = 0
        for name, key in configs.items():
            status = "✅ Ready" if key else "❌ Missing"
            print(f"  {name}: {status}")
            if key:
                ready_components += 1
        
        # Integration readiness
        readiness = {
            "total_components": len(configs),
            "ready_components": ready_components,
            "readiness_percentage": (ready_components / len(configs)) * 100,
            "can_generate_scripts": bool(configs["Groq API (Script)"]),
            "can_generate_videos": bool(configs["Google API (Video)"] or configs["MiniMax API (Video Alt)"]),
            "can_generate_voice": bool(configs["ElevenLabs API (Voice)"]),
            "timestamp": datetime.now().isoformat()
        }
        
        # Save integration report
        timestamp = datetime.now().strftime("%H%M%S")
        report_file = output_dir / f"integration_report_{timestamp}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(readiness, f, indent=2)
        
        print(f"\n📊 Integration Readiness: {readiness['readiness_percentage']:.0f}%")
        print(f"📁 Report saved: {report_file}")
        
        if readiness['readiness_percentage'] >= 50:
            print("🎉 Good integration level - can test most components!")
        else:
            print("⚠️  Low integration - add more API keys for better testing")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """Component testing menu"""
    print("🧪 AI Cat News Network - Component Tester")
    print("=" * 50)
    print()
    print("Test individual components:")
    print("1. 📝 Script Generation Component")
    print("2. 🎥 Video Generation Component")
    print("3. 🎤 Voice Generation Component")
    print("4. 🔗 Integration Check")
    print("5. 🚀 Test All Components")
    print()
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        test_script_component()
    elif choice == "2":
        test_video_component()
    elif choice == "3":
        test_voice_component()
    elif choice == "4":
        test_integration_component()
    elif choice == "5":
        print("🚀 Running all component tests...\n")
        test_script_component()
        print("\n" + "="*50 + "\n")
        test_video_component()
        print("\n" + "="*50 + "\n")
        test_voice_component()
        print("\n" + "="*50 + "\n")
        test_integration_component()
    else:
        print("❌ Invalid choice. Running integration check...")
        test_integration_component()
    
    print(f"\n📁 All component test outputs saved to: component_tests/")
    print("🔍 Check the folders to inspect individual component results")

if __name__ == "__main__":
    main()
