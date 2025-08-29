#!/usr/bin/env python3
"""
Google Veo 3 Full Production Demo
Complete Cat News Network workflow with Google Veo 3 video generation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.unified_video_generator import UnifiedVideoGenerator
from config.ai_provider import ai_provider
from config.settings import get_setting
import json
import time
from datetime import datetime

def generate_cat_news_script(topic: str) -> dict:
    """Generate a complete cat news script using AI"""
    prompt = f"""
    Create a professional 30-second cat news script about: {topic}
    
    The script should be for a cat news anchor reporting this story with:
    - Professional news format
    - Cat personality and humor
    - Clear timing markers
    - Visual cues for video generation
    
    Format as JSON:
    {{
        "headline": "Catchy news headline",
        "anchor_name": "Cat anchor name",
        "script_segments": [
            {{"time": "0-5s", "text": "Opening hook", "visual_cue": "Visual description"}},
            {{"time": "5-15s", "text": "Main story", "visual_cue": "Visual description"}},
            {{"time": "15-25s", "text": "Key details", "visual_cue": "Visual description"}},
            {{"time": "25-30s", "text": "Cat sign-off", "visual_cue": "Visual description"}}
        ],
        "video_prompt": "Detailed prompt for video generation"
    }}
    """
    
    try:
        response = ai_provider.generate_content(prompt, max_tokens=800, temperature=0.7)
        
        # Try to parse as JSON, fallback to structured text
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback structured response
            return {
                "headline": f"Breaking: {topic}",
                "anchor_name": "Whiskers Winston",
                "script_segments": [
                    {"time": "0-5s", "text": f"Breaking news in the world of {topic}!", "visual_cue": "Professional cat anchor at news desk"},
                    {"time": "5-15s", "text": "This story is developing rapidly...", "visual_cue": "Cat looking seriously at camera"},
                    {"time": "15-25s", "text": "Our experts say this could change everything.", "visual_cue": "Cat with thoughtful expression"},
                    {"time": "25-30s", "text": "I'm Whiskers Winston, and that's the news. Meow!", "visual_cue": "Cat giving professional sign-off"}
                ],
                "video_prompt": f"A professional cat news anchor reporting on {topic}, sitting at a news desk, serious but charming expression"
            }
    except Exception as e:
        print(f"Warning: AI script generation failed: {str(e)}")
        return {
            "headline": f"Cat News: {topic}",
            "anchor_name": "Fluffy McDouglas", 
            "script_segments": [
                {"time": "0-5s", "text": f"Meow! Breaking news about {topic}!", "visual_cue": "Excited cat anchor"},
                {"time": "5-25s", "text": "This is a developing story that all cats should know about.", "visual_cue": "Serious cat reporter"},
                {"time": "25-30s", "text": "Stay tuned for more cat news updates!", "visual_cue": "Cat waving goodbye"}
            ],
            "video_prompt": f"A professional cat in business attire reporting news about {topic} from a newsroom"
        }

def main():
    print("🚀 Google Veo 3 Full Production Demo")
    print("====================================")
    print("Complete Cat News Network Production Workflow")
    print()
    
    # Check API configurations
    google_key = get_setting("GOOGLE_API_KEY")
    groq_key = get_setting("GROQ_API_KEY")
    
    print("🔧 API Configuration Check:")
    print(f"{'✅' if groq_key else '❌'} Groq API (Script Generation): {'Configured' if groq_key else 'Not configured'}")
    print(f"{'✅' if google_key else '❌'} Google API (Video Generation): {'Configured' if google_key else 'Not configured'}")
    print()
    
    if not groq_key:
        print("⚠️  Warning: Groq API not configured - using fallback script generation")
    if not google_key:
        print("⚠️  Warning: Google API not configured - will use mock video generation")
    print()
    
    # News topic selection
    sample_topics = [
        "New Study Shows Cats Understand Human Emotions Better Than Dogs",
        "Major Tech Company Announces Cat-Friendly Office Policies", 
        "Scientists Discover Cats Have Been Training Humans for Thousands of Years",
        "Breaking: Local Cat Becomes Mayor of Small Town",
        "Climate Change Affecting Catnip Growth Worldwide"
    ]
    
    print("📰 Available News Topics:")
    for i, topic in enumerate(sample_topics, 1):
        print(f"{i}. {topic}")
    print("6. Custom topic")
    print()
    
    # Get user choice
    try:
        choice = input("Choose a topic (1-6): ").strip()
        if choice == "6":
            topic = input("Enter your custom topic: ").strip()
            if not topic:
                topic = sample_topics[0]
        else:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(sample_topics):
                topic = sample_topics[choice_idx]
            else:
                topic = sample_topics[0]
    except (ValueError, IndexError):
        topic = sample_topics[0]
    
    print(f"📝 Selected Topic: {topic}")
    print()
    
    # Step 1: Generate Script
    print("🎬 Step 1: Generating Cat News Script...")
    script_data = generate_cat_news_script(topic)
    
    print(f"📰 Headline: {script_data['headline']}")
    print(f"🐱 Anchor: {script_data['anchor_name']}")
    print()
    print("📋 Script Breakdown:")
    for segment in script_data['script_segments']:
        print(f"  {segment['time']}: {segment['text']}")
        print(f"    Visual: {segment['visual_cue']}")
    print()
    
    # Step 2: Generate Video
    print("🎥 Step 2: Generating Video with Google Veo 3...")
    print(f"🎯 Video Prompt: {script_data['video_prompt']}")
    print()
    
    try:
        generator = UnifiedVideoGenerator("veo3")
        
        # Enhanced prompt for better results
        enhanced_prompt = f"""
        {script_data['video_prompt']}
        
        Additional requirements:
        - 30-second duration
        - 9:16 vertical aspect ratio for social media
        - Professional news broadcast setting
        - High-quality realistic visuals
        - Cat should appear professional and credible
        - Clear lighting and sharp focus
        - Newsroom or professional background
        """
        
        result = generator.generate_video_from_prompt(enhanced_prompt, duration=30)
        
        print("📊 Video Generation Result:")
        print(f"Status: {result['status']}")
        print(f"Provider: {result.get('provider', 'unknown')}")
        
        if result['status'] == 'completed':
            print(f"✅ Video generated successfully!")
            print(f"📁 Video path: {result.get('video_path', 'N/A')}")
            print(f"🔗 Video URL: {result.get('video_url', 'N/A')}")
            
            # Create production package
            package_data = {
                "title": script_data['headline'],
                "anchor": script_data['anchor_name'],
                "topic": topic,
                "script": script_data['script_segments'],
                "video": {
                    "path": result.get('video_path'),
                    "url": result.get('video_url'),
                    "duration": result.get('duration', 30),
                    "provider": "veo3"
                },
                "created_at": datetime.now().isoformat(),
                "production_ready": True
            }
            
            # Save package
            package_filename = f"output/veo3_cat_news_package_{int(time.time())}.json"
            os.makedirs("output", exist_ok=True)
            
            with open(package_filename, 'w', encoding='utf-8') as f:
                json.dump(package_data, f, indent=2)
            
            print(f"📦 Production package saved: {package_filename}")
            
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
    print("📈 Production Summary:")
    print(f"Topic: {topic}")
    print(f"Headline: {script_data['headline']}")
    print(f"Video Provider: Google Veo 3")
    print(f"Target Duration: 30 seconds")
    print(f"Format: 9:16 vertical for social media")
    print()
    print("🎯 Next Steps:")
    print("• Review generated video")
    print("• Add voice-over with ElevenLabs")
    print("• Add captions and graphics")
    print("• Upload to YouTube Shorts & Instagram Reels")
    print()
    print("✨ Production demo completed!")

if __name__ == "__main__":
    main()
