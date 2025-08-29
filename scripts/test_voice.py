#!/usr/bin/env python3
"""
Voice Generation for AI Cat News Network
Creates professional voice-overs using ElevenLabs API from organized content
"""
import os
import sys
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

print("🎤 ElevenLabs Voice Generation - Professional Cat News")
print("=" * 50)
print(f"🔑 API Key loaded: {'✅' if os.getenv('ELEVENLABS_API_KEY') else '❌'}")

try:
    from elevenlabs import ElevenLabs
    
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))
    
    # Get the latest script from our organized structure
    latest_scripts = content_manager.get_latest_files("scripts", limit=1)
    if not latest_scripts:
        print("❌ No scripts found in content/scripts/")
        print("💡 Run the cat news script generator first (Option 1)")
        exit(1)
    
    script_filepath = latest_scripts[0]["filepath"]
    print(f"📄 Using latest script: {os.path.basename(script_filepath)}")
    
    # Read the script content
    with open(script_filepath, "r", encoding='utf-8') as f:
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
    
    # Join and create optimal version for social media (20+ seconds)
    full_script_text = ' '.join(script_lines)
    
    # Create a 20+ second version (target ~300-400 characters for 20-25 seconds)
    sentences = full_script_text.split('. ')
    script_parts = []
    char_count = 0
    
    for sentence in sentences:
        script_parts.append(sentence)
        char_count += len(sentence) + 2  # +2 for '. '
        
        # Continue until we reach minimum 20 seconds worth (~300 chars)
        if char_count >= 300:
            break
    
    script_text = '. '.join(script_parts)
    if not script_text.endswith('.'):
        script_text += '.'
    
    # If still too short, use the full script
    if len(script_text) < 250:
        script_text = full_script_text
    
    print(f"📝 Full script ({len(full_script_text)} chars): {full_script_text[:100]}...")
    print(f"🎯 Optimized script ({len(script_text)} chars): {script_text[:150]}...")
    print(f"⏱️  Target duration: ~{len(script_text) * 0.12:.0f} seconds (20+ second minimum)")
    
    if not script_text.strip():
        print("❌ No dialogue text extracted from script")
        exit(1)
    
    print("🔄 Generating voice-over...")
    
    # Generate voice using Veo 3 API
    audio_generator = client.text_to_speech.convert(
        text=script_text,
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice
        model_id="eleven_monolingual_v1"
    )
    
    # Convert generator to bytes
    audio_bytes = b''.join(audio_generator)
    
    # Save audio using content manager
    voice_settings = {
        "voice_id": "pNInz6obpgDQGcFmaJgB",
        "model_id": "eleven_monolingual_v1",
        "text_length": len(script_text)
    }
    
    audio_filepath = content_manager.save_audio(
        audio_data=audio_bytes,
        script_filepath=script_filepath,
        voice_settings=voice_settings
    )
    
    # Check file size
    size_kb = len(audio_bytes) / 1024
    print(f"✅ Voice-over created: {os.path.basename(audio_filepath)}")
    print(f"📊 Audio size: {size_kb:.1f} KB")
    print(f"📁 Saved in: content/audio/")
    print("🎬 Ready for video generation!")
    
    # Show content organization
    print(f"\n📋 Content Pipeline Status:")
    print(f"   📰 News Items: {len(content_manager.get_latest_files('newsitems'))}")
    print(f"   📝 Scripts: {len(content_manager.get_latest_files('scripts'))}")
    print(f"   🎤 Audio Files: {len(content_manager.get_latest_files('audio'))}")
    print(f"   🎬 Video Files: {len(content_manager.get_latest_files('video'))}")

except ImportError:
    print("❌ ElevenLabs not installed")
    print("💡 Install with: pip install elevenlabs")
except Exception as e:
    print(f"❌ Error: {e}")