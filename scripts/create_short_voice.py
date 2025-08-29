#!/usr/bin/env python3
"""
Short Voice Generator for 6-Second Videos
Creates ultra-short voice-over optimized for 6-second videos
"""
import os
import sys
import time
from dotenv import load_dotenv
from elevenlabs import VoiceSettings, generate, set_api_key

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def generate_short_voice():
    """Generate short voice-over for 6-second videos"""
    print("🎤 Ultra-Short Voice Generator (6-Second Optimized)")
    print("=" * 55)
    
    # Get API keys
    elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
    voice_id = os.getenv('ELEVENLABS_VOICE_ID', '2ajXGJNYBR0iNHpS4VZb')
    
    if not elevenlabs_api_key:
        print("❌ ELEVENLABS_API_KEY not found in environment variables")
        return False
    
    # Get latest short script
    latest_scripts = content_manager.get_latest_files("scripts", limit=5)
    short_script = None
    
    for script in latest_scripts:
        if "short" in script["filename"].lower() or "6s" in script["filename"].lower():
            short_script = script
            break
    
    if not short_script:
        print("❌ No short script found. Please run create_short_script.py first")
        return False
    
    script_path = short_script["filepath"]
    print(f"📄 Using script: {os.path.basename(script_path)}")
    
    # Read and optimize script for voice
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            full_script = f.read()
        
        # Extract only the spoken dialogue (remove stage directions)
        lines = full_script.split('\n')
        spoken_text = ""
        
        for line in lines:
            line = line.strip()
            # Skip empty lines, stage directions, and metadata
            if (line and 
                not line.startswith('*') and 
                not line.startswith('**') and 
                not line.startswith('---') and 
                not line.startswith('VOICE') and
                not line.startswith('VIDEO') and
                not line.startswith('CAT') and
                not line.startswith('#')):
                # Remove quotes if present
                line = line.strip('"').strip("'")
                if line:
                    spoken_text += line + " "
        
        spoken_text = spoken_text.strip()
        print(f"📝 Extracted spoken text: \"{spoken_text}\"")
        print(f"📊 Character count: {len(spoken_text)} (optimized for 5-6 seconds)")
        
        if len(spoken_text) > 150:
            print("⚠️  Text might be too long for 6-second video. Trimming...")
            spoken_text = spoken_text[:150] + "..."
        
    except Exception as e:
        print(f"❌ Failed to read script: {e}")
        return False
    
    # Generate voice with faster settings for short content
    try:
        print("🔄 Generating ultra-short voice-over...")
        
        # Initialize ElevenLabs client
        from elevenlabs import generate, set_api_key
        set_api_key(elevenlabs_api_key)
        
        # Voice settings optimized for quick delivery
        voice_settings = VoiceSettings(
            stability=0.7,
            similarity_boost=0.8,
            style=0.3,  # Less dramatic for quick delivery
            use_speaker_boost=True
        )
        
        # Generate audio
        audio = generate(
            text=spoken_text,
            voice=voice_id,
            voice_settings=voice_settings,
            model="eleven_multilingual_v2"
        )
        
        # Save audio
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        script_base = os.path.splitext(os.path.basename(script_path))[0]
        audio_filename = f"audio_{script_base}_{timestamp}.mp3"
        audio_path = f"content/audio/{audio_filename}"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        
        # Save audio file
        with open(audio_path, 'wb') as f:
            f.write(audio)
        
        # Get file size
        file_size = os.path.getsize(audio_path)
        file_size_kb = file_size / 1024
        
        print(f"✅ Ultra-short voice-over created: {audio_filename}")
        print(f"📊 Audio size: {file_size_kb:.1f} KB")
        print(f"📁 Saved in: content/audio/")
        print(f"🎯 Optimized for: 6-second video generation")
        
        # Save metadata
        metadata = {
            "timestamp": timestamp,
            "script_path": script_path,
            "audio_path": audio_path,
            "spoken_text": spoken_text,
            "character_count": len(spoken_text),
            "target_duration": "5-6 seconds",
            "optimized_for": "6-second video",
            "voice_settings": {
                "stability": 0.7,
                "similarity_boost": 0.8,
                "style": 0.3
            }
        }
        
        metadata_path = f"content/audio/{script_base}_{timestamp}_metadata.json"
        import json
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Metadata saved: {os.path.basename(metadata_path)}")
        print(f"🎬 Ready for 6-second video generation!")
        
        return True
        
    except Exception as e:
        print(f"❌ Voice generation failed: {e}")
        return False

if __name__ == "__main__":
    success = generate_short_voice()
    if success:
        print("\n🎉 Short voice generation completed!")
        print("💡 Next: Run .\\AI-Cat-News-Studio.ps1 4 for MiniMax video")
    else:
        print("\n❌ Short voice generation failed")
    
    input("\nPress Enter to continue...")
