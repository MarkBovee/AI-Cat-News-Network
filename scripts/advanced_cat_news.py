#!/usr/bin/env python3
"""
AI Cat News Creator - Alternative Video Generation
Uses AI for content and voice, with fallback video options
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from config.ai_provider import ai_provider

# Load environment variables
load_dotenv()

class AdvancedCatNewsCreator:
    """Advanced cat news creator with voice and structured output."""
    
    def __init__(self):
        self.output_dir = "content/cat_videos"
        self.temp_dir = "content/temp"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def create_complete_cat_news_package(self, topic: str = None):
        """Create a complete cat news package: script, voice, metadata."""
        
        if not topic:
            topic = self._get_trending_topic()
        
        print(f"🎬 Creating complete cat news package for: {topic}")
        
        # Step 1: Generate comprehensive script
        script_data = self._generate_enhanced_script(topic)
        
        # Step 2: Generate voice-over
        voice_file = self._generate_voice_over(script_data['clean_text'])
        
        # Step 3: Generate video metadata
        metadata = self._generate_video_metadata(topic, script_data)
        
        # Step 4: Create video instructions
        video_instructions = self._create_video_production_guide(script_data)
        
        # Step 5: Save complete package
        package_path = self._save_complete_package(topic, {
            'script': script_data,
            'voice_file': voice_file,
            'metadata': metadata,
            'video_instructions': video_instructions
        })
        
        return package_path
    
    def _get_trending_topic(self):
        """Generate a trending topic for cat news."""
        prompt = """
        Generate 1 current, trending topic that would be perfect for a viral cat news video.
        Make it something that's actually happening in the world but can be told from a cat's perspective.
        
        Examples: 
        - New AI technology launch
        - Environmental news
        - Social media trends
        - Economic changes
        - Space exploration
        
        Return just the topic, no explanation.
        """
        
        return ai_provider.generate_content(prompt, max_tokens=50, temperature=0.7).strip()
    
    def _generate_enhanced_script(self, topic: str):
        """Generate a detailed, timed script with visual cues."""
        prompt = f"""
        Create a professional 30-second cat news script about: {topic}
        
        Requirements:
        - Professional news format but with cat personality
        - Include timing markers for each segment
        - Add visual direction cues in brackets
        - Make it funny but informative
        - Perfect for YouTube Shorts (vertical video)
        
        Format:
        [0-3s] INTRO: [Visual: Cat anchor at news desk] "Good evening, I'm [Cat Name] with breaking news..."
        [3-15s] MAIN: [Visual: Relevant footage] "Today's development in [topic] means..."
        [15-25s] ANALYSIS: [Visual: Cat expert commentary] "Cat experts say this will impact..."
        [25-30s] OUTRO: [Visual: Cat anchor] "Stay tuned for more. Now back to my nap."
        
        Include cat puns and behavior naturally.
        """
        
        full_script = ai_provider.generate_content(prompt, max_tokens=600, temperature=0.8)
        
        # Extract clean text for voice-over (without timing and visual cues)
        clean_text = self._extract_clean_dialogue(full_script)
        
        return {
            'full_script': full_script,
            'clean_text': clean_text,
            'topic': topic,
            'duration': 30
        }
    
    def _extract_clean_dialogue(self, script: str):
        """Extract just the spoken dialogue from the script."""
        lines = script.split('\n')
        dialogue = []
        
        for line in lines:
            if line.strip():
                # Remove timing markers like [0-3s]
                # Remove visual cues like [Visual: ...]
                clean_line = line
                
                # Remove timing patterns
                import re
                clean_line = re.sub(r'\[\d+-\d+s\]', '', clean_line)
                clean_line = re.sub(r'\[Visual:.*?\]', '', clean_line)
                
                # Extract text after category markers
                if ':' in clean_line and any(word in clean_line.upper() for word in ['INTRO', 'MAIN', 'ANALYSIS', 'OUTRO']):
                    clean_line = clean_line.split(':', 1)[1]
                
                clean_line = clean_line.strip().strip('"')
                if clean_line:
                    dialogue.append(clean_line)
        
        return ' '.join(dialogue)
    
    def _generate_voice_over(self, text: str):
        """Generate voice-over using ElevenLabs."""
        try:
            from elevenlabs import generate
            
            print("🎤 Generating voice-over...")
            
            # Generate audio
            audio = generate(
                text=text,
                voice="Sarah",  # Friendly female voice
                model="eleven_monolingual_v1"
            )
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            voice_path = f"{self.temp_dir}/cat_news_voice_{timestamp}.mp3"
            
            with open(voice_path, 'wb') as f:
                f.write(audio)
            
            print(f"✅ Voice-over created: {voice_path}")
            return voice_path
            
        except ImportError:
            print("⚠️ ElevenLabs not available - voice-over skipped")
            return None
        except Exception as e:
            print(f"❌ Voice generation failed: {e}")
            return None
    
    def _generate_video_metadata(self, topic: str, script_data: dict):
        """Generate YouTube/Instagram metadata."""
        prompt = f"""
        Create viral social media metadata for a cat news video about: {topic}
        
        Generate:
        1. YouTube Title (max 100 chars, clickbait but accurate)
        2. Description (engaging, 2-3 sentences)
        3. 15 relevant hashtags (mix of trending and niche)
        4. Tags (10 keywords for YouTube)
        
        Make it optimized for YouTube Shorts and Instagram Reels.
        Format as JSON.
        """
        
        metadata_text = ai_provider.generate_content(prompt, max_tokens=400, temperature=0.7)
        
        # Try to parse as JSON, fallback to structured text
        try:
            return json.loads(metadata_text)
        except:
            return {
                "title": f"🐱 CAT NEWS: {topic.title()}",
                "description": f"Breaking cat news about {topic}! Our feline reporters investigate.",
                "hashtags": ["#CatNews", "#ViralVideo", "#Cats", "#Funny", "#Shorts"],
                "raw_metadata": metadata_text
            }
    
    def _create_video_production_guide(self, script_data: dict):
        """Create instructions for video production."""
        return {
            "format": "Vertical 9:16 (1080x1920)",
            "duration": "30 seconds",
            "style": "Cat news anchor setup",
            "visual_elements": [
                "Cat in professional news anchor setting",
                "News desk with cat-sized microphone",
                "Background: news studio or home office",
                "Text overlays for key points",
                "Smooth transitions between segments"
            ],
            "editing_notes": [
                "Keep cuts quick for short attention spans",
                "Add subtle cat sound effects",
                "Use professional news graphics but cat-themed",
                "Ensure text is readable on mobile"
            ]
        }
    
    def _save_complete_package(self, topic: str, package_data: dict):
        """Save the complete cat news package."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = topic.lower().replace(' ', '_').replace(':', '').replace(',', '')
        
        package_dir = f"{self.output_dir}/cat_news_{safe_topic}_{timestamp}"
        os.makedirs(package_dir, exist_ok=True)
        
        # Save script
        with open(f"{package_dir}/script.txt", 'w', encoding='utf-8') as f:
            f.write(f"CAT NEWS SCRIPT: {topic}\n")
            f.write("=" * 50 + "\n\n")
            f.write(package_data['script']['full_script'])
            f.write(f"\n\nClean dialogue for voice-over:\n")
            f.write(package_data['script']['clean_text'])
        
        # Save metadata as JSON
        with open(f"{package_dir}/metadata.json", 'w', encoding='utf-8') as f:
            json.dump(package_data['metadata'], f, indent=2)
        
        # Save production guide
        with open(f"{package_dir}/production_guide.json", 'w', encoding='utf-8') as f:
            json.dump(package_data['video_instructions'], f, indent=2)
        
        # Copy voice file if it exists
        if package_data['voice_file'] and os.path.exists(package_data['voice_file']):
            import shutil
            voice_dest = f"{package_dir}/voice_over.mp3"
            shutil.copy2(package_data['voice_file'], voice_dest)
            print(f"🎤 Voice-over saved: {voice_dest}")
        
        # Create summary file
        with open(f"{package_dir}/README.md", 'w', encoding='utf-8') as f:
            f.write(f"# Cat News Video Package: {topic}\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Package Contents:\n")
            f.write("- `script.txt` - Full script with timing and visual cues\n")
            f.write("- `metadata.json` - YouTube/Instagram metadata\n")
            f.write("- `production_guide.json` - Video production instructions\n")
            if package_data['voice_file']:
                f.write("- `voice_over.mp3` - AI-generated voice-over\n")
            f.write("\n## Next Steps:\n")
            f.write("1. Review script and production guide\n")
            f.write("2. Film cat performing news anchor role\n")
            f.write("3. Edit video using production guide\n")
            f.write("4. Add voice-over audio\n")
            f.write("5. Upload using provided metadata\n")
        
        print(f"📦 Complete package saved: {package_dir}")
        return package_dir

def main():
    print("🚀 Advanced AI Cat News Creator")
    print("=" * 50)
    
    # Check API keys
    groq_key = os.getenv('GROQ_API_KEY')
    elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
    
    print(f"🔑 Groq API: {'✅' if groq_key else '❌'}")
    print(f"🔑 ElevenLabs API: {'✅' if elevenlabs_key else '❌'}")
    
    if not groq_key:
        print("❌ Groq API key required for script generation")
        return
    
    creator = AdvancedCatNewsCreator()
    
    print("\nChoose option:")
    print("1. 🎯 Create cat news for specific topic")
    print("2. 🔥 Create cat news for trending topic (AI-generated)")
    print("3. 🔄 Create multiple videos (batch)")
    
    choice = input("\nChoice (1-3): ").strip()
    
    if choice == "1":
        topic = input("Enter your topic: ").strip()
        if not topic:
            topic = "AI technology becomes more advanced than catnip"
        
        package_path = creator.create_complete_cat_news_package(topic)
        
    elif choice == "2":
        print("🔍 Generating trending topic...")
        package_path = creator.create_complete_cat_news_package()
        
    elif choice == "3":
        count = input("How many videos to create (1-3): ").strip()
        try:
            count = int(count)
            if count < 1 or count > 3:
                count = 2
        except:
            count = 2
        
        print(f"🔄 Creating {count} cat news videos...")
        for i in range(count):
            print(f"\n--- Video {i+1}/{count} ---")
            package_path = creator.create_complete_cat_news_package()
    
    else:
        print("Invalid choice, creating trending topic video...")
        package_path = creator.create_complete_cat_news_package()
    
    print(f"\n🎉 Cat news creation completed!")
    print("Check the generated package for all video production materials.")

if __name__ == "__main__":
    main()
