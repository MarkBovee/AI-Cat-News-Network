#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

print("🎤 Testing ElevenLabs Voice Generation")
print(f"🔑 API Key loaded: {'✅' if os.getenv('ELEVENLABS_API_KEY') else '❌'}")

try:
    from elevenlabs import ElevenLabs
    import os
    
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))
    
    # Read the generated script
    script_file = "content/quick_test/cat_news_script.txt"
    if not os.path.exists(script_file):
        print(f"❌ Script file not found: {script_file}")
        exit(1)
        
    with open(script_file, "r") as f:
        content = f.read()
    
    print(f"📄 Script content loaded ({len(content)} chars)")
    
    # Extract just the dialogue (remove stage directions and formatting)
    lines = content.split('\n')
    script_lines = []
    for line in lines:
        line = line.strip()
        # Skip empty lines, topic line, and stage directions in parentheses
        if line and not line.startswith('Topic:') and not line.startswith('**') and not line.startswith('('):
            # Remove quotes if present
            line = line.strip('"')
            script_lines.append(line)
    
    script_text = ' '.join(script_lines)
    print(f"📝 Script to voice ({len(script_text)} chars): {script_text[:100]}...")
    
    if not script_text.strip():
        print("❌ No dialogue text extracted from script")
        exit(1)
    
    print("🔄 Generating voice-over...")
    
    # Generate voice using new API
    audio_generator = client.text_to_speech.convert(
        text=script_text,
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice
        model_id="eleven_monolingual_v1"
    )
    
    # Convert generator to bytes
    audio_bytes = b''.join(audio_generator)
    
    # Save audio
    voice_path = "content/quick_test/cat_news_voice.mp3"
    with open(voice_path, 'wb') as f:
        f.write(audio_bytes)
    
    # Check file size
    size_kb = os.path.getsize(voice_path) / 1024
    print(f"✅ Voice-over created: {voice_path}")
    print(f"📊 Audio size: {size_kb:.1f} KB")
    print("🎬 Ready to combine with video!")
    
except ImportError:
    print("❌ ElevenLabs not installed")
except Exception as e:
    print(f"❌ Error: {e}")
