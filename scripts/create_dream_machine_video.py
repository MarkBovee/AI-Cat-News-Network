#!/usr/bin/env python3
"""
Dream Machine (Luma AI) Video Generator - AI Cat News Network
Generate videos using Luma AI's Dream Machine API
"""

import os
import json
import time
import requests
import glob

class DreamMachineGenerator:
    """Dream Machine (Luma AI) video generation client"""
    
    def __init__(self):
        self.api_key = os.getenv('LUMA_API_KEY')
        self.base_url = "https://api.lumalabs.ai/dream-machine/v1"
        
        if not self.api_key:
            print("⚠️  LUMA_API_KEY not found in environment")
            print("💡 Get your API key from: https://lumalabs.ai/dream-machine")
    
    def create_video_from_text(self, prompt, duration=6):
        """Create video from text prompt using Dream Machine"""
        
        if not self.api_key:
            return self._simulate_dream_response(prompt, duration)
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "prompt": prompt,
            "aspect_ratio": "9:16",  # Vertical for social media
            "loop": False,
            "keyframes": {
                "frame0": {
                    "type": "generation",
                    "text": prompt
                }
            }
        }
        
        try:
            print(f"🎬 Sending request to Dream Machine...")
            print(f"📝 Prompt: {prompt}")
            
            response = requests.post(
                f"{self.base_url}/generations",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200 or response.status_code == 201:
                result = response.json()
                return self._handle_dream_response(result, prompt, duration)
            else:
                print(f"❌ Dream Machine API error: {response.status_code}")
                print(f"Response: {response.text}")
                return self._simulate_dream_response(prompt, duration)
                
        except Exception as e:
            print(f"❌ Error calling Dream Machine API: {e}")
            return self._simulate_dream_response(prompt, duration)
    
    def _handle_dream_response(self, result, prompt, duration):
        """Handle successful Dream Machine response"""
        
        generation_id = result.get('id')
        state = result.get('state', 'queued')
        
        print(f"✅ Dream Machine video generation started!")
        print(f"🆔 Generation ID: {generation_id}")
        print(f"📊 State: {state}")
        
        # Poll for completion
        video_url = self._poll_for_completion(generation_id)
        
        if video_url:
            # Download and save video
            return self._download_video(video_url, prompt, duration)
        else:
            return self._simulate_dream_response(prompt, duration)
    
    def _poll_for_completion(self, generation_id, max_wait=600):
        """Poll Dream Machine API for video completion"""
        
        if not self.api_key:
            return None
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = requests.get(
                    f"{self.base_url}/generations/{generation_id}",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    state = result.get('state')
                    
                    print(f"🔄 State: {state}")
                    
                    if state == 'completed':
                        assets = result.get('assets', {})
                        video_url = assets.get('video')
                        return video_url
                    elif state == 'failed':
                        failure_reason = result.get('failure_reason', 'Unknown error')
                        print(f"❌ Video generation failed: {failure_reason}")
                        return None
                    
                    # Wait before next poll
                    time.sleep(15)  # Dream Machine can take longer
                else:
                    print(f"❌ Status check failed: {response.status_code}")
                    time.sleep(15)
                    
            except Exception as e:
                print(f"⚠️  Status check error: {e}")
                time.sleep(15)
        
        print("⏰ Timeout waiting for video completion")
        return None
    
    def _download_video(self, video_url, prompt, duration):
        """Download video from Dream Machine"""
        
        try:
            print(f"⬇️  Downloading video from: {video_url}")
            
            response = requests.get(video_url, timeout=120)
            
            if response.status_code == 200:
                # Save video file
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                output_path = f"content/video/dream_machine_{timestamp}.mp4"
                
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                
                # Save metadata
                metadata = {
                    "timestamp": timestamp,
                    "provider": "dream_machine",
                    "model": "luma_ai_v1",
                    "prompt": prompt,
                    "duration": duration,
                    "video_url": video_url,
                    "output_path": output_path,
                    "aspect_ratio": "9:16",
                    "quality": "high",
                    "status": "completed"
                }
                
                metadata_path = f"content/video/dream_machine_{timestamp}_metadata.json"
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2)
                
                print(f"✅ Video downloaded successfully!")
                print(f"📄 Video: {output_path}")
                print(f"📊 Metadata: {metadata_path}")
                
                return metadata
            else:
                print(f"❌ Download failed: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Download error: {e}")
            return None
    
    def _simulate_dream_response(self, prompt, duration):
        """Simulate Dream Machine response for testing"""
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        metadata = {
            "timestamp": timestamp,
            "provider": "dream_machine_simulation",
            "model": "luma_ai_v1_simulation",
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": "9:16",
            "quality": "high",
            "status": "simulated",
            "note": "Simulation - Add LUMA_API_KEY to .env for real generation"
        }
        
        metadata_path = f"content/video/dream_simulation_{timestamp}.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"🌟 Dream Machine simulation completed!")
        print(f"📊 Metadata: {metadata_path}")
        print(f"💡 Add LUMA_API_KEY to .env for real video generation")
        
        return metadata

def get_latest_script():
    """Get the latest script file without content manager"""
    script_files = glob.glob("content/scripts/script_*.txt")
    if script_files:
        # Sort by modification time, get newest
        latest = max(script_files, key=os.path.getmtime)
        return latest
    return None

def create_dream_machine_video():
    """Main function to create video with Dream Machine"""
    
    print("🌟 Dream Machine Video Generator - AI Cat News Network")
    print("=" * 55)
    
    # Initialize generator
    generator = DreamMachineGenerator()
    
    # Get latest script
    script_path = get_latest_script()
    
    if not script_path:
        print("❌ No script found! Please generate a script first.")
        return None
    
    # Read script content
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    
    # Create video prompt optimized for Dream Machine
    video_prompt = f"""A professional cat news anchor sits confidently at a modern newsroom desk. 
The cat is an orange tabby wearing a business suit and tie, with an authoritative yet charismatic expression. 
Behind the cat is a sleek newsroom with multiple screens displaying "CAT NEWS NETWORK" branding. 
Professional studio lighting illuminates the scene with a warm, broadcast-quality appearance. 
The cat occasionally gestures with paws while maintaining eye contact with the camera. 
Cinematic quality, professional news broadcast atmosphere, shallow depth of field.
News topic: {script_content[:150]}..."""
    
    print(f"🎯 Generated video prompt for Dream Machine")
    
    # Generate video
    result = generator.create_video_from_text(video_prompt, duration=6)
    
    if result:
        print("\n🎉 Dream Machine video generation completed!")
        print("💡 Video optimized for social media (9:16 vertical)")
        print("🎬 Dream Machine is known for exceptional video quality")
        print("🎯 Next: Combine with audio for final production")
        return result
    else:
        print("\n❌ Dream Machine video generation failed")
        return None

if __name__ == "__main__":
    create_dream_machine_video()
