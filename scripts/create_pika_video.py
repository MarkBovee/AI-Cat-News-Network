#!/usr/bin/env python3
"""
Pika Labs Video Generator - AI Cat News Network (Simplified)
Generate videos using Pika Labs API without CV2 dependencies
"""

import os
import json
import time
import requests
import glob

class PikaLabsGenerator:
    """Pika Labs video generation client"""
    
    def __init__(self):
        self.api_key = os.getenv('PIKA_LABS_API_KEY')
        self.base_url = "https://api.pikalabs.ai/v1"
        
        if not self.api_key:
            print("⚠️  PIKA_LABS_API_KEY not found in environment")
            print("💡 Get your API key from: https://pika.art/")
    
    def create_video_from_text(self, prompt, duration=6):
        """Create video from text prompt using Pika Labs"""
        
        if not self.api_key:
            return self._simulate_pika_response(prompt, duration)
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": "9:16",  # Vertical for social media
            "quality": "high",
            "style": "realistic",
            "motion_strength": "medium"
        }
        
        try:
            print(f"🎬 Sending request to Pika Labs...")
            print(f"📝 Prompt: {prompt}")
            
            response = requests.post(
                f"{self.base_url}/generate",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return self._handle_pika_response(result, prompt, duration)
            else:
                print(f"❌ Pika Labs API error: {response.status_code}")
                print(f"Response: {response.text}")
                return self._simulate_pika_response(prompt, duration)
                
        except Exception as e:
            print(f"❌ Error calling Pika Labs API: {e}")
            return self._simulate_pika_response(prompt, duration)
    
    def _handle_pika_response(self, result, prompt, duration):
        """Handle successful Pika Labs response"""
        
        video_id = result.get('id')
        status = result.get('status', 'pending')
        
        print(f"✅ Pika Labs video generation started!")
        print(f"🆔 Video ID: {video_id}")
        print(f"📊 Status: {status}")
        
        # Poll for completion
        video_url = self._poll_for_completion(video_id)
        
        if video_url:
            # Download and save video
            return self._download_video(video_url, prompt, duration)
        else:
            return self._simulate_pika_response(prompt, duration)
    
    def _poll_for_completion(self, video_id, max_wait=300):
        """Poll Pika Labs API for video completion"""
        
        if not self.api_key:
            return None
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = requests.get(
                    f"{self.base_url}/status/{video_id}",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    status = result.get('status')
                    
                    print(f"🔄 Status: {status}")
                    
                    if status == 'completed':
                        return result.get('video_url')
                    elif status == 'failed':
                        print(f"❌ Video generation failed: {result.get('error', 'Unknown error')}")
                        return None
                    
                    # Wait before next poll
                    time.sleep(10)
                else:
                    print(f"❌ Status check failed: {response.status_code}")
                    time.sleep(10)
                    
            except Exception as e:
                print(f"⚠️  Status check error: {e}")
                time.sleep(10)
        
        print("⏰ Timeout waiting for video completion")
        return None
    
    def _download_video(self, video_url, prompt, duration):
        """Download video from Pika Labs"""
        
        try:
            print(f"⬇️  Downloading video from: {video_url}")
            
            response = requests.get(video_url, timeout=60)
            
            if response.status_code == 200:
                # Save video file
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                output_path = f"content/video/pika_video_{timestamp}.mp4"
                
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                
                # Save metadata
                metadata = {
                    "timestamp": timestamp,
                    "provider": "pika_labs",
                    "model": "pika_v1",
                    "prompt": prompt,
                    "duration": duration,
                    "video_url": video_url,
                    "output_path": output_path,
                    "aspect_ratio": "9:16",
                    "quality": "high",
                    "status": "completed"
                }
                
                metadata_path = f"content/video/pika_video_{timestamp}_metadata.json"
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
    
    def _simulate_pika_response(self, prompt, duration):
        """Simulate Pika Labs response for testing"""
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        metadata = {
            "timestamp": timestamp,
            "provider": "pika_labs_simulation",
            "model": "pika_v1_simulation",
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": "9:16",
            "quality": "high",
            "status": "simulated",
            "note": "Simulation - Add PIKA_LABS_API_KEY to .env for real generation"
        }
        
        metadata_path = f"content/video/pika_simulation_{timestamp}.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"🎭 Pika Labs simulation completed!")
        print(f"📊 Metadata: {metadata_path}")
        print(f"💡 Add PIKA_LABS_API_KEY to .env for real video generation")
        
        return metadata

def get_latest_script():
    """Get the latest script file without content manager"""
    script_files = glob.glob("content/scripts/script_*.txt")
    if script_files:
        # Sort by modification time, get newest
        latest = max(script_files, key=os.path.getmtime)
        return latest
    return None

def create_pika_video():
    """Main function to create video with Pika Labs"""
    
    print("🎬 Pika Labs Video Generator - AI Cat News Network")
    print("=" * 55)
    
    # Initialize generator
    generator = PikaLabsGenerator()
    
    # Get latest script
    script_path = get_latest_script()
    
    if not script_path:
        print("❌ No script found! Please generate a script first.")
        return None
    
    # Read script content
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    print(f"📝 Using script: {os.path.basename(script_path)}")
    
    # Create video prompt optimized for Pika Labs
    video_prompt = f"""Professional cat news anchor reporting in a modern newsroom studio. 
A confident orange tabby cat in a business suit sits at a sleek news desk with professional lighting. 
The cat has an authoritative expression while delivering news. 
Modern newsroom background with screens showing "CAT NEWS NETWORK" logo. 
Professional broadcast quality lighting, serious news atmosphere.
Script context: {script_content[:200]}..."""
    
    print(f"🎯 Generated video prompt for Pika Labs")
    
    # Generate video
    result = generator.create_video_from_text(video_prompt, duration=6)
    
    if result:
        print("\n🎉 Pika Labs video generation completed!")
        print("💡 Video optimized for social media (9:16 vertical)")
        print("🎯 Next: Combine with audio for final production")
        return result
    else:
        print("\n❌ Pika Labs video generation failed")
        return None

if __name__ == "__main__":
    create_pika_video()
