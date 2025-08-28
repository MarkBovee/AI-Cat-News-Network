#!/usr/bin/env python3
"""
Full AI Cat News Video Creator - With MoviePy
Creates complete videos with voice-over and visuals
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test if all required packages are available."""
    print("🔍 Testing imports...")
    
    try:
        from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip
        print("✅ MoviePy imported successfully")
    except ImportError as e:
        print(f"❌ MoviePy import failed: {e}")
        return False
    
    try:
        from elevenlabs import generate
        print("✅ ElevenLabs imported successfully")
    except ImportError as e:
        print(f"⚠️ ElevenLabs import failed: {e}")
        print("   Voice-over functionality will be disabled")
    
    try:
        from config.ai_provider import ai_provider
        print("✅ AI Provider imported successfully")
    except ImportError as e:
        print(f"❌ AI Provider import failed: {e}")
        return False
    
    return True

def create_simple_cat_video():
    """Create a simple cat news video with text and voice."""
    print("\n🎬 Creating Cat News Video...")
    
    # Import here to handle any issues
    try:
        from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip
        from config.ai_provider import ai_provider
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return
    
    # Generate cat news script
    print("📝 Generating cat news script...")
    prompt = """
    Create a short 20-second cat news script about "Breaking: Local cat discovers new napping spot"
    
    Format:
    INTRO: Cat anchor introduces the breaking news
    NEWS: Details about the amazing new napping spot
    OUTRO: Cat signs off and probably yawns
    
    Keep it funny and under 50 words total.
    """
    
    try:
        script = ai_provider.generate_content(prompt, max_tokens=200, temperature=0.8)
        print(f"✅ Script generated: {script[:100]}...")
    except Exception as e:
        print(f"❌ Script generation failed: {e}")
        script = "Breaking news: I'm Fluffy McWhiskers, and we've discovered the ultimate napping spot - a warm laptop keyboard. This changes everything for cat-kind. Now back to my important nap. *yawn*"
    
    # Create video segments
    print("🎥 Creating video segments...")
    
    try:
        # Create directories
        os.makedirs("content/videos", exist_ok=True)
        os.makedirs("content/temp", exist_ok=True)
        
        # Parse script into segments
        segments = [
            {"text": "🐱 CAT NEWS NETWORK 🐱", "duration": 3},
            {"text": script[:50] + "...", "duration": 8},
            {"text": "...MEOW FOR MORE NEWS! 😸", "duration": 3}
        ]
        
        # Create text clips
        clips = []
        for segment in segments:
            clip = TextClip(
                segment['text'],
                fontsize=50,
                color='white',
                bg_color='darkblue',
                size=(1080, 1920),  # Vertical format for shorts
                method='caption'
            ).set_duration(segment['duration'])
            
            clips.append(clip)
        
        # Combine clips
        final_video = concatenate_videoclips(clips)
        
        # Save video
        output_path = "content/videos/cat_news_demo.mp4"
        final_video.write_videofile(output_path, fps=24, verbose=False, logger=None)
        final_video.close()
        
        print(f"✅ Video created: {output_path}")
        
        # Check file size
        if os.path.exists(output_path):
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"📊 Video size: {size_mb:.2f} MB")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Video creation failed: {e}")
        return None

def test_voice_generation():
    """Test ElevenLabs voice generation."""
    print("\n🎤 Testing voice generation...")
    
    try:
        from elevenlabs import generate
        
        test_script = "Hello, I'm Whiskers reporting for Cat News Network. Breaking news: treats have been discovered in the kitchen cabinet!"
        
        print("🔄 Generating voice-over...")
        audio = generate(
            text=test_script,
            voice="Sarah",
            model="eleven_monolingual_v1"
        )
        
        # Save audio
        voice_path = "content/temp/test_voice.mp3"
        with open(voice_path, 'wb') as f:
            f.write(audio)
        
        print(f"✅ Voice-over created: {voice_path}")
        
        if os.path.exists(voice_path):
            size_kb = os.path.getsize(voice_path) / 1024
            print(f"📊 Audio size: {size_kb:.2f} KB")
        
        return voice_path
        
    except ImportError:
        print("⚠️ ElevenLabs not available - skipping voice test")
        return None
    except Exception as e:
        print(f"❌ Voice generation failed: {e}")
        return None

def main():
    print("🚀 Full AI Cat News Video Creator")
    print("=" * 50)
    
    # Check environment
    groq_key = os.getenv('GROQ_API_KEY')
    elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
    
    print(f"🔑 Groq API: {'✅' if groq_key else '❌'}")
    print(f"🔑 ElevenLabs API: {'✅' if elevenlabs_key else '❌'}")
    
    # Test imports
    if not test_imports():
        print("❌ Required packages not available")
        return
    
    print("\nChoose test:")
    print("1. 🎬 Create simple cat news video")
    print("2. 🎤 Test voice generation only")
    print("3. 🔄 Full test (video + voice)")
    
    choice = input("\nChoice (1-3): ").strip()
    
    if choice == "1":
        create_simple_cat_video()
    elif choice == "2":
        test_voice_generation()
    elif choice == "3":
        video_path = create_simple_cat_video()
        voice_path = test_voice_generation()
        
        if video_path and voice_path:
            print("\n🎉 Both video and voice created successfully!")
            print("Next step: Combine them into a complete video")
    else:
        print("Invalid choice, creating simple video...")
        create_simple_cat_video()
    
    # List all created files
    print("\n📁 Generated files:")
    for root, dirs, files in os.walk("content"):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"  - {file_path}")
    
    print("\n🏁 Test completed!")

if __name__ == "__main__":
    main()
