"""
AI Video Generator for Cat News Network
Integrates with MiniMax API (HailuoAI) for real video generation
"""

import os
import json
import time
import requests
from typing import Dict, Any, List, Optional
from config.settings import get_setting

class MiniMaxVideoGenerator:
    """MiniMax API integration for text-to-video generation (HailuoAI)"""
    
    def __init__(self):
        self.api_key = get_setting("MINIMAX_API_KEY")
        self.base_url = "https://api.minimax.chat/v1/video_generation"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_video_from_prompt(self, prompt: str, duration: int = 5) -> Dict[str, Any]:
        """Generate video from text prompt using MiniMax API"""
        if not self.api_key:
            return {
                "status": "error",
                "message": "MiniMax API key not configured. Please add MINIMAX_API_KEY to your .env file",
                "mock_video": True,
                "prompt": prompt
            }
        
        # Create video generation request for MiniMax
        payload = {
            "model": "video-01",
            "prompt": prompt,
            "duration": duration,
            "resolution": "720p",
            "aspect_ratio": "9:16",  # Vertical format for social media
            "style": "realistic"
        }
        
        try:
            print(f"🎬 Sending request to MiniMax API for: {prompt[:50]}...")
            
            # Start generation
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                generation_data = response.json()
                task_id = generation_data.get("task_id")
                
                if task_id:
                    print(f"✅ Video generation started. Task ID: {task_id}")
                    # Wait for completion
                    return self._wait_for_completion(task_id)
                else:
                    return {
                        "status": "error",
                        "message": "No task ID returned from API",
                        "mock_video": True,
                        "prompt": prompt
                    }
            else:
                print(f"❌ API request failed with status {response.status_code}")
                return {
                    "status": "error",
                    "message": f"API request failed: {response.status_code} - {response.text}",
                    "mock_video": True,
                    "prompt": prompt
                }
                
        except Exception as e:
            print(f"❌ Error generating video: {str(e)}")
            return {
                "status": "error",
                "message": f"Error generating video: {str(e)}",
                "mock_video": True,
                "prompt": prompt
            }
    
    def _wait_for_completion(self, task_id: str, max_wait: int = 300) -> Dict[str, Any]:
        """Wait for video generation to complete"""
        start_time = time.time()
        check_url = f"{self.base_url}/{task_id}"
        
        print(f"⏳ Waiting for video generation to complete...")
        
        while time.time() - start_time < max_wait:
            try:
                response = requests.get(
                    check_url,
                    headers=self.headers,
                    timeout=15
                )
                
                if response.status_code == 200:
                    data = response.json()
                    status = data.get("status")
                    
                    if status == "completed":
                        video_url = data.get("video_url")
                        print(f"✅ Video generation completed! URL: {video_url}")
                        return {
                            "status": "success",
                            "video_url": video_url,
                            "task_id": task_id,
                            "duration": data.get("duration", 5)
                        }
                    elif status == "failed":
                        error_msg = data.get("error", "Unknown error")
                        print(f"❌ Video generation failed: {error_msg}")
                        return {
                            "status": "error",
                            "message": f"Video generation failed: {error_msg}",
                            "task_id": task_id
                        }
                    elif status in ["pending", "processing"]:
                        # Still processing
                        print(f"🔄 Status: {status}, waiting...")
                        time.sleep(10)
                        continue
                    else:
                        print(f"⚠️ Unknown status: {status}")
                        time.sleep(5)
                        continue
                else:
                    print(f"❌ Status check failed: {response.status_code}")
                    return {
                        "status": "error",
                        "message": f"Status check failed: {response.status_code}"
                    }
                    
            except Exception as e:
                print(f"❌ Error checking status: {str(e)}")
                return {
                    "status": "error",
                    "message": f"Error checking status: {str(e)}"
                }
        
        print(f"⏰ Video generation timed out after {max_wait} seconds")
        return {
            "status": "timeout",
            "message": "Video generation timed out"
        }

class AIVideoCreator:
    """Main class for creating AI-generated cat news videos using MiniMax"""
    
    def __init__(self):
        self.minimax = MiniMaxVideoGenerator()
        self.output_dir = "content/ai_videos"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_cat_news_video(self, news_topic: str, script: str) -> Dict[str, Any]:
        """Create a complete cat news video with AI-generated segments"""
        
        print("🐱 Starting MiniMax AI video generation...")
        
        # Break script into visual segments
        segments = self._create_video_segments(news_topic, script)
        
        video_results = []
        
        for i, segment in enumerate(segments):
            print(f"📹 Generating video segment {i+1}/{len(segments)}: {segment['description']}")
            
            # Generate video for this segment using MiniMax
            result = self.minimax.generate_video_from_prompt(
                segment['prompt'], 
                duration=segment['duration']
            )
            
            video_results.append({
                'segment_id': i + 1,
                'description': segment['description'],
                'prompt': segment['prompt'],
                'duration': segment['duration'],
                'result': result
            })
            
            # Brief pause between API calls to avoid rate limiting
            if i < len(segments) - 1:  # Don't pause after last segment
                print("⏸️ Pausing briefly to avoid rate limits...")
                time.sleep(3)
        
        # Create final package
        video_package = {
            'news_topic': news_topic,
            'script': script,
            'segments': video_results,
            'total_duration': sum(seg['duration'] for seg in segments),
            'creation_timestamp': time.time(),
            'provider': 'MiniMax (HailuoAI)',
            'status': 'completed' if all(r['result'].get('status') == 'success' for r in video_results) else 'partial'
        }
        
        # Save package
        safe_filename = news_topic.lower().replace(' ', '_').replace(':', '').replace(',', '')[:50]
        output_file = f"{self.output_dir}/{safe_filename}_minimax_video.json"
        
        with open(output_file, 'w') as f:
            json.dump(video_package, f, indent=2)
        
        print(f"📦 MiniMax video package saved: {output_file}")
        return video_package
    
    def _create_video_segments(self, news_topic: str, script: str) -> List[Dict[str, Any]]:
        """Break down the script into visual segments for video generation"""
        
        segments = []
        
        # Segment 1: Professional Cat News Anchor (0-5s)
        segments.append({
            'description': 'Professional cat news anchor opening',
            'prompt': f'Professional orange tabby cat news anchor wearing glasses and business suit, sitting at modern news desk with "Cat News Network" logo, studio lighting, serious expression, looking directly at camera, newsroom background, high quality, realistic',
            'duration': 5
        })
        
        # Segment 2: Story Visualization (5-15s)  
        segments.append({
            'description': 'Visual representation of the news story',
            'prompt': f'Cinematic scene illustrating: {news_topic}, multiple cats in professional business environment, dramatic lighting, documentary style, high quality realistic footage, cats wearing business attire',
            'duration': 10
        })
        
        # Segment 3: Cat Reactions (15-20s)
        segments.append({
            'description': 'Cats reacting to breaking news',
            'prompt': 'Multiple cats of different breeds (tabby, siamese, persian) looking surprised and engaged, sitting around modern conference table, business meeting atmosphere, professional lighting, realistic, high quality',
            'duration': 5
        })
        
        # Segment 4: News Anchor Sign-off (20-25s)
        segments.append({
            'description': 'Cat anchor professional conclusion',
            'prompt': 'Orange tabby cat news anchor nodding confidently, slight professional smile, raising paw in farewell gesture, modern news studio background, authoritative and trustworthy expression, high quality realistic',
            'duration': 5
        })
        
        return segments

# Export for use in other modules
__all__ = ['AIVideoCreator', 'MiniMaxVideoGenerator']
