#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

print("🎤 Testing ElevenLabs Voice Generation")

try:
    from elevenlabs import generate
    
    # Read the generated script
    with open("content/quick_test/cat_news_script.txt", "r") as f:
        content = f.read()
    
    # Extract just the dialogue
    script_text = """Breaking news, fellow felines! I've got the purr-fect scoop for you. The Cat Cafe has just launched an AI-powered 'Purr-fect Match' system! No more swiping left on the wrong kitty. This tech will sniff out your feline soulmate, ensuring a whisker-ific connection. It's the cat's meow! And that's the news. Now, if you'll excuse me, I have some catnapping to do."""
    
    print("🔄 Generating voice-over...")
    
    # Generate voice
    audio = generate(
        text=script_text,
        voice="Sarah",
        model="eleven_monolingual_v1"
    )
    
    # Save audio
    voice_path = "content/quick_test/cat_news_voice.mp3"
    with open(voice_path, 'wb') as f:
        f.write(audio)
    
    # Check file size
    size_kb = os.path.getsize(voice_path) / 1024
    print(f"✅ Voice-over created: {voice_path}")
    print(f"📊 Audio size: {size_kb:.1f} KB")
    print("🎬 Ready to combine with video!")
    
except ImportError:
    print("❌ ElevenLabs not installed")
except Exception as e:
    print(f"❌ Error: {e}")
