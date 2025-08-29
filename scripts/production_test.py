#!/usr/bin/env python3
"""
Simple Cat News Generation Test
Tests the complete pipeline: AI generation + file creation
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add the parent directory to sys.path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from config.ai_provider import ai_provider

# Load environment variables
load_dotenv()

def main():
    print("🐱 AI Cat News Network - Production Test")
    print("=" * 50)
    
    # Check API configuration
    groq_key = os.getenv('GROQ_API_KEY')
    google_key = os.getenv('GOOGLE_API_KEY')
    minimax_key = os.getenv('MINIMAX_API_KEY')
    
    print("📋 API Configuration:")
    print(f"  🤖 Groq AI: {'✅ Set' if groq_key else '❌ Missing'}")
    print(f"  🎥 Google Veo: {'✅ Set' if google_key else '❌ Missing'}")
    print(f"  🎬 MiniMax: {'✅ Set' if minimax_key else '❌ Missing'}")
    print()
    
    # Test AI provider
    print("🧪 Testing AI Script Generation...")
    try:
        provider_info = ai_provider.get_provider_info()
        print(f"  Provider: {provider_info['provider']}")
        print(f"  Model: {provider_info['model']}")
        print(f"  Status: {provider_info['status']}")
        print("  ✅ AI Provider initialized successfully")
    except Exception as e:
        print(f"  ❌ AI Provider error: {e}")
        return
    
    # Generate multiple cat news stories
    topics = [
        "Breaking: Local cat elected as town mayor, promises more nap time for everyone",
        "Scientists discover cats have been secretly controlling the internet all along",
        "New study reveals cats understand human emotions better than humans understand cat emotions",
        "Breaking: Cat cafe chain announces IPO, stock expected to be very volatile (like cats)"
    ]
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("content") / "production_test" / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🎬 Generating {len(topics)} Cat News Stories...")
    print(f"📁 Output directory: {output_dir}")
    print()
    
    for i, topic in enumerate(topics, 1):
        print(f"📰 Story {i}/{len(topics)}: {topic[:50]}...")
        
        # Generate script
        prompt = f"""
Create a professional 30-second cat news script about: {topic}

Format as a TV news broadcast with:
[0-3s] HOOK: Attention-grabbing opening
[3-15s] STORY: Main news with cat perspective and subtle humor
[15-25s] IMPACT: Why this matters to viewers
[25-30s] SIGN-OFF: Professional closing with cat personality

Anchor: Whiskers Winston (professional news cat with dry humor)
Include timing cues and visual directions in brackets.
Keep it viral-worthy but professional.
"""
        
        try:
            script = ai_provider.generate_content(prompt, max_tokens=600, temperature=0.7)
            
            # Save script
            script_file = output_dir / f"story_{i:02d}_script.txt"
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(f"TOPIC: {topic}\n")
                f.write("=" * 60 + "\n\n")
                f.write(script)
            
            print(f"  ✅ Script generated and saved to {script_file.name}")
            
            # Show preview
            preview = script[:100].replace('\n', ' ') + "..."
            print(f"  📄 Preview: {preview}")
            print()
            
        except Exception as e:
            print(f"  ❌ Error generating script: {e}")
            continue
    
    print("🎉 Production Test Complete!")
    print(f"📁 All scripts saved to: {output_dir}")
    print("\n🚀 Next Steps:")
    print("  1. Review generated scripts")
    print("  2. Test video generation with Google Veo 3 or MiniMax")
    print("  3. Add voice generation with ElevenLabs")
    print("  4. Create complete video packages")

if __name__ == "__main__":
    main()
