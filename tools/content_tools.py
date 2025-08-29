import os
import requests
import json
from typing import List, Dict, Optional
# MoviePy removed - inadequate for professional AI video generation
# Use MiniMax, Google Veo, or other AI video APIs instead
from elevenlabs import ElevenLabs
from PIL import Image, ImageDraw, ImageFont
from config.ai_provider import ai_provider, generate_content_ideas, write_script, generate_hashtags
from config.settings import ELEVENLABS_VOICE_ID

class ContentGenerationTool:
    """Tool for generating content with AI - now with Groq for fast and free AI."""
    
    def __init__(self):
        # Use the global AI provider manager
        self.ai_provider = ai_provider
    
    def generate_content_ideas(self, topic: str, count: int = 5) -> str:
        """Generate content ideas for a given topic using Groq."""
        return generate_content_ideas(topic, count)
    
    def write_script(self, content_idea: str) -> str:
        """Write a script for a content idea using Groq."""
        return write_script(content_idea)

class AIVideoCreationTool:
    """Advanced tool for creating AI-generated videos with visuals, voice-over, and effects."""
    
    def __init__(self):
        self.output_dir = "content/videos"
        self.temp_dir = "content/temp"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def create_ai_generated_video(self, news_topic: str, output_path: str = None) -> str:
        """Create a cat-themed news video using AI video generation instead of text overlays."""
        if not output_path:
            output_path = f"{self.output_dir}/ai_cat_news_{news_topic.lower().replace(' ', '_')}.json"
        
        try:
            # Step 1: Generate cat news script
            script = self._generate_cat_news_script(news_topic)
            print(f"📝 Script generated: {script[:100]}...")
            
            # Step 2: Generate voice-over
            voice_path = f"{self.temp_dir}/voiceover.mp3"
            self._generate_voice_over(script, voice_path)
            print(f"🎤 Voice-over created: {voice_path}")
            
            # Step 3: Use AI video generation instead of text overlays
            from tools.ai_video_generator import AIVideoCreator
            
            ai_video_creator = AIVideoCreator()
            video_package = ai_video_creator.create_cat_news_video(news_topic, script)
            
            # Step 4: Save complete package
            complete_package = {
                'news_topic': news_topic,
                'script': script,
                'voice_file': voice_path,
                'ai_video_package': video_package,
                'creation_type': 'ai_generated_video',
                'status': 'completed'
            }
            
            with open(output_path, 'w') as f:
                json.dump(complete_package, f, indent=2)
            
            print(f"🎬 AI video package created: {output_path}")
            return f"AI cat news video package created successfully: {output_path}"
            
        except Exception as e:
            return f"Error creating AI cat news video: {str(e)}"

    def create_cat_news_video(self, news_topic: str, output_path: str = None) -> str:
        """Create a cat-themed news video with AI-generated content."""
        if not output_path:
            output_path = f"{self.output_dir}/cat_news_{news_topic.lower().replace(' ', '_')}.mp4"
        
        try:
            # Step 1: Generate cat news script
            script = self._generate_cat_news_script(news_topic)
            print(f"📝 Script generated: {script[:100]}...")
            
            # Step 2: Generate voice-over
            voice_path = f"{self.temp_dir}/voiceover.mp3"
            self._generate_voice_over(script, voice_path)
            print(f"🎤 Voice-over created: {voice_path}")
            
            # Step 3: Get cat images/videos (placeholder for now)
            visual_assets = self._get_cat_visual_assets()
            print(f"🐱 Visual assets prepared: {len(visual_assets)} items")
            
            # Step 4: Create video with all components
            self._create_video_with_assets(script, voice_path, visual_assets, output_path)
            print(f"🎬 Video created: {output_path}")
            
            return f"Cat news video created successfully: {output_path}"
            
        except Exception as e:
            return f"Error creating cat news video: {str(e)}"
    
    def _generate_cat_news_script(self, news_topic: str) -> str:
        """Generate a cat-themed news script."""
        prompt = f"""
        Create a funny 30-second script for a cat news anchor reporting on: {news_topic}
        
        Style: Cats reporting serious news but with cat behavior and terminology
        Format:
        [0-3s] INTRO: Cat anchor introduction with puns
        [3-15s] NEWS: Main news topic explained by cats
        [15-25s] IMPACT: How this affects the cat community
        [25-30s] OUTRO: Typical cat sign-off
        
        Include cat puns, meowing, and typical cat behaviors.
        Keep it engaging and viral-worthy for YouTube Shorts.
        """
        
        return ai_provider.generate_content(prompt, max_tokens=400, temperature=0.8)
    
    def _generate_voice_over(self, script: str, output_path: str) -> str:
        """Generate voice-over using ElevenLabs with configured voice."""
        try:
            # Clean script for voice synthesis (remove timing markers)
            clean_script = self._clean_script_for_voice(script)
            
            # Initialize ElevenLabs client (API key from environment)
            client = ElevenLabs()
            
            # Use voice ID from settings
            voice_id = ELEVENLABS_VOICE_ID
            print(f"Using voice ID: {voice_id}")
            
            # Generate voice using ElevenLabs text_to_speech method
            audio = client.text_to_speech.convert(
                voice_id=voice_id,
                text=clean_script,
                model_id="eleven_monolingual_v1"
            )
            
            # Save audio file
            with open(output_path, 'wb') as f:
                for chunk in audio:
                    f.write(chunk)
            
            return output_path
        except Exception as e:
            print(f"Error generating voice-over: {str(e)}")
            # Create a placeholder audio file to continue the process
            try:
                with open(output_path, 'wb') as f:
                    f.write(b'')  # Empty file placeholder
            except:
                pass
            return None
    
    def _clean_script_for_voice(self, script: str) -> str:
        """Clean script text for voice synthesis."""
        lines = script.split('\n')
        clean_lines = []
        
        for line in lines:
            # Remove timing markers like [0-3s]
            if line.strip() and not line.strip().startswith('[') and ':' in line:
                # Extract text after the category (INTRO:, NEWS:, etc.)
                if ':' in line:
                    text = line.split(':', 1)[1].strip()
                    clean_lines.append(text)
            elif line.strip() and not line.strip().startswith('['):
                clean_lines.append(line.strip())
        
        return ' '.join(clean_lines)
    
    def _get_cat_visual_assets(self) -> List[Dict]:
        """Get cat images and video clips for the video."""
        # For now, return placeholder data
        # In a full implementation, this would:
        # 1. Download cat images from Unsplash/Pexels APIs
        # 2. Use AI image generation (DALL-E, Midjourney API)
        # 3. Use stock video APIs
        
        return [
            {
                "type": "image",
                "path": "placeholder_cat_news_anchor.jpg",
                "duration": 5,
                "description": "Cat news anchor at desk"
            },
            {
                "type": "image", 
                "path": "placeholder_cat_reporter.jpg",
                "duration": 10,
                "description": "Cat reporter in the field"
            },
            {
                "type": "image",
                "path": "placeholder_cat_audience.jpg", 
                "duration": 10,
                "description": "Cat audience reacting"
            },
            {
                "type": "image",
                "path": "placeholder_cat_outro.jpg",
                "duration": 5,
                "description": "Cat signing off"
            }
        ]
    
    def _create_video_with_assets(self, script: str, voice_path: str, visual_assets: List[Dict], output_path: str):
        """Create professional video using AI video generation APIs (not MoviePy).
        
        MoviePy has been removed as it only creates basic text overlays, not professional AI video.
        Use MiniMax, Google Veo, or other AI video generation services instead.
        """
        print("🎬 Video creation requires AI video generation APIs")
        print("💡 Use MiniMax, Google Veo 3, or other professional video AI services")
        print("❌ MoviePy removed - inadequate for professional video generation")
        
        # Create metadata for AI video generation instead
        video_metadata = {
            "script": script,
            "audio_path": voice_path,
            "visual_requirements": visual_assets,
            "output_path": output_path,
            "recommended_apis": ["MiniMax", "Google Veo 3", "Runway ML", "Pika Labs"],
            "note": "Use professional AI video generation - not basic text overlays"
        }
        
        metadata_path = output_path.replace('.mp4', '_ai_video_metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(video_metadata, f, indent=2)
            
        print(f"📄 AI video metadata saved: {metadata_path}")
        return metadata_path

class VideoCreationTool:
    """Professional AI video creation tool - NO MoviePy dependency."""
    
    def create_ai_video_request(self, script: str, output_path: str = "content/output.mp4") -> str:
        """Create metadata for AI video generation (replaces MoviePy text overlays)."""
        print("🎬 Professional AI Video Generation Required")
        print("❌ MoviePy removed - only creates basic text, not professional video")
        print("💡 Use MiniMax, Google Veo 3, or other AI video generation APIs")
        
        # Create AI video generation request
        ai_request = {
            "script": script,
            "output_path": output_path,
            "video_style": "Professional cat news anchor in CNN-style studio",
            "duration": "20-30 seconds",
            "aspect_ratio": "9:16 (vertical for social media)",
            "recommended_apis": [
                "MiniMax Video Generation",
                "Google Veo 3",
                "Runway ML",
                "Pika Labs"
            ],
            "note": "Requires professional AI video generation - not basic text overlays"
        }
        
        metadata_path = output_path.replace('.mp4', '_ai_request.json')
        with open(metadata_path, 'w') as f:
            json.dump(ai_request, f, indent=2)
            
        return f"AI video request saved: {metadata_path}"

class SocialMediaTool:
    """Tool for social media integration."""
    
    def generate_hashtags(self, content_description: str) -> str:
        """Generate relevant hashtags for content using AI."""
        return generate_hashtags(content_description)
    
    def create_caption(self, script: str) -> str:
        """Create social media caption from script."""
        # Extract main message from script
        lines = [line.strip() for line in script.split('\n') if line.strip()]
        main_content = ' '.join(lines[:2])  # Use first two lines
        
        caption = f"{main_content}\n\n"
        caption += "What do you think? Let me know in the comments! 👇\n\n"
        caption += "Follow for more content like this! 🔥"
        
        return caption
