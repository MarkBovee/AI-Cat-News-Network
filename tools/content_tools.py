import os
import requests
import json
from typing import List, Dict, Optional
from moviepy.editor import TextClip, concatenate_videoclips, CompositeVideoClip, VideoFileClip, AudioFileClip, ImageClip
from elevenlabs import generate, voices
from PIL import Image, ImageDraw, ImageFont
from config.ai_provider import ai_provider, generate_content_ideas, write_script, generate_hashtags

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
        """Generate voice-over using ElevenLabs with a friendly voice."""
        try:
            # Clean script for voice synthesis (remove timing markers)
            clean_script = self._clean_script_for_voice(script)
            
            # Generate voice using ElevenLabs
            audio = generate(
                text=clean_script,
                voice="Sarah",  # Friendly female voice for cat news
                model="eleven_monolingual_v1"
            )
            
            # Save audio file
            with open(output_path, 'wb') as f:
                f.write(audio)
            
            return output_path
        except Exception as e:
            print(f"Error generating voice-over: {str(e)}")
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
        """Create the final video combining all assets."""
        try:
            # For now, create a simple text-based video with voice-over
            # This is a placeholder until MoviePy dependencies are resolved
            
            segments = self._parse_script(script)
            clips = []
            
            for i, segment in enumerate(segments):
                # Create styled text clip
                clip = TextClip(
                    segment['text'],
                    fontsize=60,
                    color='white',
                    bg_color='navy',
                    size=(1080, 1920),  # Vertical format for shorts
                    method='caption'
                ).set_duration(segment['duration'])
                
                clips.append(clip)
            
            # Concatenate clips
            if clips:
                final_video = concatenate_videoclips(clips)
                
                # Add voice-over if available
                if voice_path and os.path.exists(voice_path):
                    try:
                        audio = AudioFileClip(voice_path)
                        final_video = final_video.set_audio(audio)
                    except Exception as e:
                        print(f"Could not add audio: {e}")
                
                # Write video file
                final_video.write_videofile(output_path, fps=24)
                final_video.close()
            
            return output_path
            
        except Exception as e:
            print(f"Error creating video: {e}")
            # Fallback: create simple text file with script
            with open(output_path.replace('.mp4', '_script.txt'), 'w') as f:
                f.write(f"Cat News Script:\n\n{script}")
            return f"Script saved (video creation failed): {output_path.replace('.mp4', '_script.txt')}"
    
    def generate_viral_cat_news_ideas(self, count: int = 3) -> str:
        """Generate viral cat news video ideas based on recent events."""
        prompt = f"""
        Generate {count} viral cat news video ideas for YouTube Shorts based on recent news/trends.
        
        Each idea should be:
        - A serious news topic but told from a cat's perspective
        - Funny and shareable
        - 30 seconds perfect for shorts
        - Include visual suggestions
        
        Format:
        1. Title: [Catchy title with cat puns]
           Topic: [News angle]
           Hook: [Opening line]
           Visuals: [What we'd see]
        """
        
        return ai_provider.generate_content(prompt, max_tokens=600, temperature=0.8)
    
    def _parse_script(self, script: str) -> List[Dict]:
        """Parse script into timed segments."""
        lines = script.split('\n')
        segments = []
        
        for line in lines:
            if line.strip() and not line.startswith('['):
                # Extract timing if available
                duration = 3  # Default
                text = line.strip()
                
                # Look for timing markers like [0-3s]
                if ':' in line and any(char in line for char in ['INTRO', 'NEWS', 'IMPACT', 'OUTRO']):
                    text = line.split(':', 1)[1].strip()
                    if 'INTRO' in line or 'OUTRO' in line:
                        duration = 3
                    else:
                        duration = 8
                
                segments.append({
                    'text': text,
                    'duration': duration
                })
        
        return segments

class VideoCreationTool:
    """Legacy tool for basic video creation."""
    
    def create_text_video(self, script: str, output_path: str = "content/output.mp4") -> str:
        """Create a simple text-based video from script."""
        try:
            # Parse script into segments
            segments = self._parse_script(script)
            clips = []
            
            for segment in segments:
                # Create text clip
                clip = TextClip(
                    segment['text'],
                    fontsize=70,
                    color='white',
                    bg_color='black',
                    size=(1080, 1920)  # Vertical format
                ).set_duration(segment['duration'])
                
                clips.append(clip)
            
            # Concatenate clips
            final_video = concatenate_videoclips(clips)
            final_video.write_videofile(output_path, fps=24)
            
            return f"Video created: {output_path}"
        except Exception as e:
            return f"Error creating video: {str(e)}"
    
    def _parse_script(self, script: str) -> List[Dict]:
        """Parse script into timed segments."""
        lines = script.split('\n')
        segments = []
        
        for line in lines:
            if line.strip() and not line.startswith('['):
                segments.append({
                    'text': line.strip(),
                    'duration': 3  # Default 3 seconds per segment
                })
        
        return segments

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
