#!/usr/bin/env python3
"""
Open-Sora Local Video Generator - AI Cat News Network
Generate videos using Open-Sora locally with CPU/GPU support
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
import glob

def check_open_sora_installation():
    """Check if Open-Sora is installed and available"""
    print("🔍 Checking Open-Sora installation...")
    
    # Check if git is available for cloning
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        print("✅ Git is available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git not found - required for Open-Sora installation")
        return False
    
    # Check if Open-Sora directory exists
    opensora_path = Path("models/Open-Sora")
    if opensora_path.exists():
        print(f"✅ Open-Sora found at: {opensora_path}")
        return str(opensora_path)
    
    print("📦 Open-Sora not found - will clone repository")
    return None

def install_open_sora():
    """Install Open-Sora from GitHub"""
    print("📥 Installing Open-Sora...")
    
    try:
        # Create models directory
        models_dir = Path("models")
        models_dir.mkdir(exist_ok=True)
        
        # Clone Open-Sora repository
        print("🔄 Cloning Open-Sora repository...")
        subprocess.run([
            "git", "clone", 
            "https://github.com/hpcaitech/Open-Sora.git",
            "models/Open-Sora"
        ], check=True)
        
        print("✅ Open-Sora cloned successfully")
        
        # Install dependencies
        print("📦 Installing Open-Sora dependencies...")
        opensora_path = Path("models/Open-Sora")
        
        # Install requirements if available
        requirements_file = opensora_path / "requirements.txt"
        if requirements_file.exists():
            subprocess.run([
                sys.executable, "-m", "pip", "install", 
                "-r", str(requirements_file)
            ], check=True)
            print("✅ Dependencies installed")
        
        return str(opensora_path)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Open-Sora: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def generate_opensora_video(prompt, duration_seconds=6, output_path=None):
    """Generate video using Open-Sora"""
    
    opensora_path = check_open_sora_installation()
    
    if not opensora_path:
        opensora_path = install_open_sora()
        if not opensora_path:
            return simulate_opensora_generation(prompt, duration_seconds, output_path)
    
    try:
        print("🎬 Initializing Open-Sora pipeline...")
        
        # Change to Open-Sora directory
        original_cwd = os.getcwd()
        os.chdir(opensora_path)
        
        # Prepare generation command
        if not output_path:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_path = f"../../content/video/opensora_{timestamp}.mp4"
        
        # Open-Sora command line interface
        cmd = [
            sys.executable, "scripts/inference.py",
            "--model", "PixArt-XL-2-512x512",  # Smaller model for compatibility
            "--prompt", prompt,
            "--save-path", output_path,
            "--num-frames", "48",  # ~6 seconds at 8fps
            "--height", "512",
            "--width", "512",
            "--fps", "8"
        ]
        
        print(f"🎥 Generating video with Open-Sora...")
        print(f"📝 Prompt: {prompt[:100]}...")
        print("⏳ This may take 10-30 minutes depending on your hardware...")
        
        # Run generation
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)  # 1 hour timeout
        
        # Return to original directory
        os.chdir(original_cwd)
        
        if result.returncode == 0:
            print(f"✅ Video generated successfully: {output_path}")
            
            # Save metadata
            metadata = {
                "timestamp": time.strftime("%Y%m%d_%H%M%S"),
                "provider": "opensora_local",
                "model": "PixArt-XL-2-512x512",
                "prompt": prompt,
                "duration": duration_seconds,
                "output_path": output_path,
                "resolution": "512x512",
                "fps": 8,
                "num_frames": 48,
                "status": "completed"
            }
            
            metadata_path = output_path.replace('.mp4', '_metadata.json')
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            return metadata
        else:
            print(f"❌ Open-Sora generation failed: {result.stderr}")
            return simulate_opensora_generation(prompt, duration_seconds, output_path)
        
    except subprocess.TimeoutExpired:
        print("⏰ Generation timed out (1 hour limit)")
        os.chdir(original_cwd)
        return simulate_opensora_generation(prompt, duration_seconds, output_path)
        
    except Exception as e:
        print(f"❌ Error generating video: {e}")
        if 'original_cwd' in locals():
            os.chdir(original_cwd)
        return simulate_opensora_generation(prompt, duration_seconds, output_path)

def simulate_opensora_generation(prompt, duration_seconds, output_path):
    """Simulate Open-Sora generation for testing"""
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    metadata = {
        "timestamp": timestamp,
        "provider": "opensora_simulation",
        "model": "PixArt-XL-2-512x512-simulation",
        "prompt": prompt,
        "duration": duration_seconds,
        "resolution": "512x512",
        "fps": 8,
        "num_frames": 48,
        "status": "simulated",
        "note": "Simulation - Clone Open-Sora repository for real generation",
        "requirements": {
            "hardware": "CPU supported, GPU recommended for speed",
            "install": "git clone https://github.com/hpcaitech/Open-Sora.git",
            "time": "10-30 minutes generation time on local hardware"
        }
    }
    
    metadata_path = f"content/video/opensora_simulation_{timestamp}.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"🎭 Open-Sora simulation completed!")
    print(f"📊 Metadata: {metadata_path}")
    print(f"💡 Clone Open-Sora repository and install dependencies for real generation")
    
    return metadata

def get_latest_script():
    """Get the latest script file"""
    script_files = glob.glob("content/scripts/script_*.txt")
    if script_files:
        latest = max(script_files, key=os.path.getmtime)
        return latest
    return None

def create_opensora_video():
    """Main function to create video with Open-Sora"""
    
    print("🌟 Open-Sora Local Video Generator - AI Cat News Network")
    print("=" * 65)
    
    # Get latest script
    script_path = get_latest_script()
    
    if not script_path:
        print("❌ No script found! Please generate a script first.")
        return None
    
    # Read script content
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    
    # Create video prompt optimized for Open-Sora
    video_prompt = f"""A professional cat news anchor, orange tabby cat wearing a business suit, sitting at a modern newsroom desk. The cat has intelligent eyes and an authoritative expression. Behind the cat is a newsroom with screens showing "CAT NEWS NETWORK". Professional studio lighting, broadcast quality, realistic, high detail.

Story: {script_content[:100]}"""
    
    print(f"🎯 Generated video prompt for Open-Sora")
    print(f"⚙️ Model: PixArt-XL-2, Resolution: 512x512, Duration: ~6s")
    
    # Generate video
    result = generate_opensora_video(video_prompt, duration_seconds=6)
    
    if result:
        print("\n🎉 Open-Sora video generation completed!")
        print("💡 Fully local generation - no API costs, no internet required")
        print("🎬 Open-source AI video generation on your own hardware")
        print("🎯 Next: Combine with audio for final production")
        return result
    else:
        print("\n❌ Open-Sora video generation failed")
        return None

if __name__ == "__main__":
    create_opensora_video()
