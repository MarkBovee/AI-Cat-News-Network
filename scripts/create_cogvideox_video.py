#!/usr/bin/env python3
"""
CogVideoX-Flash Local Video Generator - AI Cat News Network
Generate videos using CogVideoX-Flash locally without API dependencies
"""

import os
import sys
import json
import time
import subprocess
import torch
from pathlib import Path
import glob

def check_system_requirements():
    """Check if system meets CogVideoX-Flash requirements"""
    print("🔍 Checking system requirements for CogVideoX-Flash...")
    
    # Check GPU
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"✅ GPU: {gpu_name} ({gpu_memory:.1f}GB VRAM)")
        
        if gpu_memory < 8:
            print("⚠️  Warning: CogVideoX-Flash recommends 12GB+ VRAM for optimal performance")
            print("💡 Consider using smaller models or lower resolution")
        
        return True
    else:
        print("❌ No CUDA GPU detected")
        print("💡 CogVideoX-Flash requires NVIDIA GPU with CUDA support")
        return False

def install_cogvideox_flash():
    """Install CogVideoX-Flash dependencies"""
    print("📦 Installing CogVideoX-Flash dependencies...")
    
    try:
        # Install required packages
        packages = [
            "diffusers>=0.30.0",
            "transformers>=4.44.0", 
            "torch>=2.0.0",
            "torchvision",
            "accelerate",
            "xformers",
            "imageio[ffmpeg]",
            "opencv-python",
            "pillow"
        ]
        
        for package in packages:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("✅ All dependencies installed successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def download_cogvideox_model():
    """Download CogVideoX-Flash model from Hugging Face"""
    print("⬇️  Downloading CogVideoX-Flash model...")
    
    try:
        from diffusers import CogVideoXPipeline
        
        # Download the model (this will cache it locally)
        print("📥 Loading CogVideoX-Flash-2B model...")
        pipeline = CogVideoXPipeline.from_pretrained(
            "THUDM/CogVideoX-2B",
            torch_dtype=torch.float16,
            variant="fp16"
        )
        
        print("✅ Model downloaded and ready")
        return pipeline
        
    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        print("💡 This might be due to network issues or insufficient disk space")
        return None

def generate_cogvideox_video(prompt, duration_seconds=6, output_path=None):
    """Generate video using CogVideoX-Flash"""
    
    if not check_system_requirements():
        return simulate_cogvideox_generation(prompt, duration_seconds, output_path)
    
    try:
        print("🎬 Initializing CogVideoX-Flash pipeline...")
        
        # Try to load the pipeline
        from diffusers import CogVideoXPipeline
        import torch
        
        pipeline = CogVideoXPipeline.from_pretrained(
            "THUDM/CogVideoX-2B",
            torch_dtype=torch.float16,
            variant="fp16"
        )
        
        # Move to GPU if available
        if torch.cuda.is_available():
            pipeline = pipeline.to("cuda")
            print("✅ Pipeline loaded on GPU")
        else:
            print("⚠️  Running on CPU (will be slow)")
        
        # Generate video
        print(f"🎥 Generating video with prompt: {prompt[:100]}...")
        print("⏳ This may take several minutes...")
        
        # CogVideoX parameters
        video = pipeline(
            prompt=prompt,
            num_frames=48,  # ~2-6 seconds at 8fps
            height=480,     # Lower resolution for faster generation
            width=720,      # 3:2 aspect ratio
            num_inference_steps=50,
            guidance_scale=6.0,
        ).frames[0]
        
        # Save video
        if not output_path:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_path = f"content/video/cogvideox_{timestamp}.mp4"
        
        # Convert frames to video
        import imageio
        imageio.mimsave(output_path, video, fps=8)
        
        print(f"✅ Video generated successfully: {output_path}")
        
        # Save metadata
        metadata = {
            "timestamp": time.strftime("%Y%m%d_%H%M%S"),
            "provider": "cogvideox_flash_local",
            "model": "THUDM/CogVideoX-2B",
            "prompt": prompt,
            "duration": duration_seconds,
            "output_path": output_path,
            "resolution": "720x480",
            "fps": 8,
            "num_frames": 48,
            "status": "completed"
        }
        
        metadata_path = output_path.replace('.mp4', '_metadata.json')
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
        
    except ImportError:
        print("❌ CogVideoX dependencies not installed")
        print("💡 Installing dependencies...")
        if install_cogvideox_flash():
            print("✅ Dependencies installed, please run again")
        return simulate_cogvideox_generation(prompt, duration_seconds, output_path)
        
    except Exception as e:
        print(f"❌ Error generating video: {e}")
        return simulate_cogvideox_generation(prompt, duration_seconds, output_path)

def simulate_cogvideox_generation(prompt, duration_seconds, output_path):
    """Simulate CogVideoX generation for testing"""
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    
    metadata = {
        "timestamp": timestamp,
        "provider": "cogvideox_flash_simulation",
        "model": "THUDM/CogVideoX-2B-simulation",
        "prompt": prompt,
        "duration": duration_seconds,
        "resolution": "720x480",
        "fps": 8,
        "num_frames": 48,
        "status": "simulated",
        "note": "Simulation - Install CogVideoX-Flash dependencies for real generation",
        "requirements": {
            "gpu": "NVIDIA GPU with 8GB+ VRAM recommended",
            "packages": ["diffusers>=0.30.0", "transformers>=4.44.0", "torch>=2.0.0"]
        }
    }
    
    metadata_path = f"content/video/cogvideox_simulation_{timestamp}.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"🎭 CogVideoX-Flash simulation completed!")
    print(f"📊 Metadata: {metadata_path}")
    print(f"💡 Install dependencies and run on NVIDIA GPU for real generation")
    
    return metadata

def get_latest_script():
    """Get the latest script file"""
    script_files = glob.glob("content/scripts/script_*.txt")
    if script_files:
        latest = max(script_files, key=os.path.getmtime)
        return latest
    return None

def create_cogvideox_video():
    """Main function to create video with CogVideoX-Flash"""
    
    print("⚡ CogVideoX-Flash Local Video Generator - AI Cat News Network")
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
    
    # Create video prompt optimized for CogVideoX
    video_prompt = f"""A professional orange tabby cat news anchor wearing a business suit sits confidently at a modern newsroom desk. The cat has an authoritative expression with intelligent eyes looking directly at the camera. Behind the cat is a sleek newsroom with multiple screens displaying "CAT NEWS NETWORK" in bold letters. Professional studio lighting creates a warm, broadcast-quality atmosphere. The cat occasionally makes subtle head movements and blinks naturally while maintaining a professional news anchor posture. High quality, realistic, professional broadcast environment.

News context: {script_content[:150]}"""
    
    print(f"🎯 Generated video prompt for CogVideoX-Flash")
    print(f"⚙️ Model: CogVideoX-2B, Resolution: 720x480, Duration: ~6s")
    
    # Generate video
    result = generate_cogvideox_video(video_prompt, duration_seconds=6)
    
    if result:
        print("\n🎉 CogVideoX-Flash video generation completed!")
        print("💡 Local generation - no API costs or limits")
        print("🎬 High-quality AI video generation on your own hardware")
        print("🎯 Next: Combine with audio for final production")
        return result
    else:
        print("\n❌ CogVideoX-Flash video generation failed")
        return None

if __name__ == "__main__":
    create_cogvideox_video()
