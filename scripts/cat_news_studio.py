#!/usr/bin/env python3
"""
🐱 Complete AI Cat News Video Creator - Final Demo
Creates viral cat news content with script, voice instructions, and metadata
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from config.ai_provider import ai_provider

load_dotenv()

class CompleteCatNewsStudio:
    """Professional cat news video production studio."""
    
    def __init__(self):
        self.studio_dir = "content/cat_news_studio"
        os.makedirs(self.studio_dir, exist_ok=True)
        print("🎬 Cat News Studio initialized!")
    
    def create_viral_cat_video(self, custom_topic=None):
        """Create a complete viral cat news video package."""
        
        print("\n🚀 Creating Viral Cat News Video...")
        print("=" * 50)
        
        # Step 1: Topic Generation
        if custom_topic:
            topic = custom_topic
        else:
            topic = self.generate_trending_topic()
        
        print(f"📰 Topic: {topic}")
        
        # Step 2: Script Creation
        script_data = self.create_professional_script(topic)
        print("✅ Professional script created")
        
        # Step 3: Video Metadata
        metadata = self.generate_viral_metadata(topic, script_data)
        print("✅ Viral metadata generated")
        
        # Step 4: Production Guide
        production_guide = self.create_production_guide(script_data)
        print("✅ Production guide created")
        
        # Step 5: Voice Instructions
        voice_instructions = self.create_voice_instructions(script_data)
        print("✅ Voice-over instructions prepared")
        
        # Step 6: Save Complete Package
        package_path = self.save_video_package(topic, {
            'script': script_data,
            'metadata': metadata,
            'production': production_guide,
            'voice': voice_instructions
        })
        
        print(f"🎉 Complete video package created: {package_path}")
        return package_path
    
    def generate_trending_topic(self):
        """Generate a viral-worthy topic."""
        prompt = """
        Generate 1 current trending topic perfect for a viral cat news video.
        It should be:
        - Related to real current events or trends
        - Perfect for cat commentary and puns
        - Shareable and funny
        - Good for 30-second format
        
        Examples: "AI chatbots replace customer service", "New social media platform launches", "Climate change affects coffee prices"
        
        Return just the topic title, no quotes or explanation.
        """
        
        return ai_provider.generate_content(prompt, max_tokens=50, temperature=0.7).strip().strip('"')
    
    def create_professional_script(self, topic):
        """Create a professional cat news script with timing."""
        prompt = f"""
        Create a professional 30-second cat news script about: {topic}
        
        Requirements:
        - Professional news anchor style but with cat personality
        - Include precise timing for each segment
        - Add visual direction cues
        - Make it viral-worthy with cat puns
        - Perfect for YouTube Shorts (vertical video)
        
        Format:
        [0-3s] COLD OPEN: [Visual cue] "Dialogue with hook..."
        [3-8s] INTRO: [Visual cue] "Good evening, I'm [Cat Name] with Cat News Network..."
        [8-20s] MAIN STORY: [Visual cue] "Breaking news about [topic] with cat perspective..."
        [20-27s] IMPACT: [Visual cue] "This means for the cat community..."
        [27-30s] OUTRO: [Visual cue] "Reporting for CNN - Cat News Network, I'm [Name]. *yawn*"
        
        Include natural cat behaviors and relevant puns.
        """
        
        full_script = ai_provider.generate_content(prompt, max_tokens=800, temperature=0.8)
        
        # Extract clean dialogue for voice-over
        dialogue_only = self.extract_dialogue(full_script)
        
        return {
            'full_script': full_script,
            'dialogue_only': dialogue_only,
            'duration': 30,
            'segments': self.parse_segments(full_script)
        }
    
    def extract_dialogue(self, script):
        """Extract spoken dialogue from script."""
        import re
        
        # Remove timing markers and visual cues
        clean = re.sub(r'\[\d+-\d+s\]', '', script)
        clean = re.sub(r'\[Visual:.*?\]', '', clean)
        clean = re.sub(r'\[.*?\]', '', clean)
        
        # Extract dialogue after colons
        lines = clean.split('\n')
        dialogue = []
        
        for line in lines:
            if ':' in line and any(word in line.upper() for word in ['OPEN', 'INTRO', 'MAIN', 'IMPACT', 'OUTRO']):
                text = line.split(':', 1)[1].strip().strip('"')
                if text:
                    dialogue.append(text)
        
        return ' '.join(dialogue)
    
    def parse_segments(self, script):
        """Parse script into timed segments."""
        import re
        segments = []
        
        # Find timing patterns like [0-3s]
        timing_pattern = r'\[(\d+)-(\d+)s\]'
        lines = script.split('\n')
        
        for line in lines:
            timing_match = re.search(timing_pattern, line)
            if timing_match:
                start_time = int(timing_match.group(1))
                end_time = int(timing_match.group(2))
                duration = end_time - start_time
                
                # Extract segment type and content
                segment_type = line.split(']')[1].split(':')[0].strip() if ']:' in line else "SEGMENT"
                content = line.split(':', 1)[1].strip() if ':' in line else line
                
                segments.append({
                    'type': segment_type,
                    'start': start_time,
                    'duration': duration,
                    'content': content
                })
        
        return segments
    
    def generate_viral_metadata(self, topic, script_data):
        """Generate metadata optimized for virality."""
        prompt = f"""
        Create viral social media metadata for a cat news video about: {topic}
        
        Generate optimized content for YouTube Shorts and Instagram Reels:
        
        1. TITLE: Catchy, clickbait-style title under 60 characters with cat puns
        2. DESCRIPTION: Engaging 2-sentence description that hooks viewers
        3. HASHTAGS: 15 strategic hashtags (trending + niche + cat-related)
        4. YOUTUBE_TAGS: 10 keywords for YouTube algorithm
        5. HOOK_TEXT: Text overlay for the first 3 seconds to grab attention
        
        Format as valid JSON. Make it optimized for maximum shares and engagement.
        """
        
        metadata_raw = ai_provider.generate_content(prompt, max_tokens=500, temperature=0.7)
        
        # Try to parse JSON, fallback to manual structure
        try:
            metadata = json.loads(metadata_raw)
        except:
            metadata = {
                "title": f"🐱 BREAKING: Cats React to {topic}",
                "description": f"Our feline news team investigates {topic} and the results are purr-fectly shocking! 😸",
                "hashtags": ["#CatNews", "#ViralVideo", "#Cats", "#Funny", "#Shorts", "#Reels", "#CatsOfTikTok", "#FelineNews", "#CatVideo", "#Viral"],
                "youtube_tags": ["cats", "funny", "news", "viral", "shorts"],
                "hook_text": "🚨 BREAKING CAT NEWS 🚨",
                "raw_response": metadata_raw
            }
        
        return metadata
    
    def create_production_guide(self, script_data):
        """Create detailed video production instructions."""
        return {
            "video_specs": {
                "format": "Vertical 9:16 aspect ratio",
                "resolution": "1080x1920 (minimum)",
                "duration": "30 seconds exactly",
                "frame_rate": "24-30 fps"
            },
            "filming_setup": {
                "location": "Home office or clean background",
                "props": ["News desk (cat-sized)", "Microphone", "Papers/tablet", "Good lighting"],
                "cat_positioning": "Seated at desk, facing camera",
                "backup_plan": "If cat won't cooperate, use voiceover with B-roll footage"
            },
            "visual_style": {
                "graphics": "News-style lower thirds with cat puns",
                "colors": "Professional blue/white with cat-friendly accents",
                "fonts": "Clean, readable fonts (mobile-optimized)",
                "transitions": "Quick cuts, no long fades"
            },
            "editing_checklist": [
                "Add opening graphic with 'CAT NEWS NETWORK'",
                "Sync voice-over with cat footage",
                "Add text overlays for key points",
                "Include hook text in first 3 seconds",
                "Add subtle background music",
                "Ensure captions are accurate",
                "Export in vertical format"
            ]
        }
    
    def create_voice_instructions(self, script_data):
        """Create voice-over recording/generation instructions."""
        return {
            "voice_style": {
                "tone": "Professional news anchor with slight playfulness",
                "pace": "Moderate to fast (news style)",
                "energy": "Confident and engaging",
                "accent": "Neutral/American"
            },
            "recording_tips": [
                "Record in quiet environment",
                "Use good microphone if available",
                "Practice cat puns with emphasis",
                "Leave slight pauses for visual cues",
                "Record in multiple takes for best quality"
            ],
            "ai_voice_options": {
                "elevenlabs_voice": "Sarah (friendly female)",
                "alternative": "Adam (professional male)",
                "settings": "Model: eleven_monolingual_v1, Stability: 0.75"
            },
            "script_for_voice": script_data['dialogue_only'],
            "timing_notes": "Total duration should be 25-28 seconds to allow for pauses"
        }
    
    def save_video_package(self, topic, package_data):
        """Save complete video production package."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = topic.lower().replace(' ', '_').replace(':', '').replace(',', '')[:30]
        
        package_dir = f"{self.studio_dir}/catnews_{safe_topic}_{timestamp}"
        os.makedirs(package_dir, exist_ok=True)
        
        # Save script
        with open(f"{package_dir}/01_SCRIPT.txt", 'w', encoding='utf-8') as f:
            f.write(f"🐱 CAT NEWS SCRIPT: {topic}\n")
            f.write("=" * 60 + "\n\n")
            f.write("FULL SCRIPT WITH TIMING:\n")
            f.write("-" * 30 + "\n")
            f.write(package_data['script']['full_script'])
            f.write("\n\n" + "=" * 60 + "\n")
            f.write("DIALOGUE ONLY (FOR VOICE-OVER):\n")
            f.write("-" * 30 + "\n")
            f.write(package_data['script']['dialogue_only'])
        
        # Save metadata
        with open(f"{package_dir}/02_METADATA.json", 'w', encoding='utf-8') as f:
            json.dump(package_data['metadata'], f, indent=2, ensure_ascii=False)
        
        # Save production guide
        with open(f"{package_dir}/03_PRODUCTION_GUIDE.json", 'w', encoding='utf-8') as f:
            json.dump(package_data['production'], f, indent=2)
        
        # Save voice instructions
        with open(f"{package_dir}/04_VOICE_INSTRUCTIONS.json", 'w', encoding='utf-8') as f:
            json.dump(package_data['voice'], f, indent=2)
        
        # Create quick reference
        with open(f"{package_dir}/README.md", 'w', encoding='utf-8') as f:
            f.write(f"# 🐱 Cat News Video: {topic}\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## 📋 Production Checklist:\n\n")
            f.write("### Pre-Production:\n")
            f.write("- [ ] Review script and timing\n")
            f.write("- [ ] Set up filming location\n")
            f.write("- [ ] Prepare props and lighting\n")
            f.write("- [ ] Brief your cat actor 😸\n\n")
            f.write("### Production:\n")
            f.write("- [ ] Film cat news anchor segments\n")
            f.write("- [ ] Record or generate voice-over\n")
            f.write("- [ ] Capture B-roll footage if needed\n\n")
            f.write("### Post-Production:\n")
            f.write("- [ ] Edit video following production guide\n")
            f.write("- [ ] Add graphics and text overlays\n")
            f.write("- [ ] Sync audio and video\n")
            f.write("- [ ] Export in vertical format (9:16)\n\n")
            f.write("### Publishing:\n")
            f.write("- [ ] Upload to YouTube Shorts\n")
            f.write("- [ ] Upload to Instagram Reels\n")
            f.write("- [ ] Use provided metadata and hashtags\n")
            f.write("- [ ] Monitor performance and engagement\n\n")
            f.write("## 📁 Package Contents:\n")
            f.write("- `01_SCRIPT.txt` - Complete script with timing\n")
            f.write("- `02_METADATA.json` - Social media metadata\n")
            f.write("- `03_PRODUCTION_GUIDE.json` - Video production specs\n")
            f.write("- `04_VOICE_INSTRUCTIONS.json` - Voice-over guidelines\n\n")
            f.write("## 🎯 Expected Results:\n")
            f.write("- Duration: 30 seconds\n")
            f.write("- Format: Vertical video optimized for mobile\n")
            f.write("- Target: High engagement on YouTube Shorts & Instagram Reels\n")
            f.write("- Style: Professional news with cat humor\n")
        
        return package_dir

def main():
    print("🎬 Complete AI Cat News Video Creator")
    print("=" * 60)
    
    # Check API status
    groq_key = os.getenv('GROQ_API_KEY')
    print(f"🔑 Groq AI: {'✅ Connected' if groq_key else '❌ Not configured'}")
    
    if not groq_key:
        print("❌ Please configure GROQ_API_KEY in .env file")
        return
    
    studio = CompleteCatNewsStudio()
    
    print("\n🎯 Choose your cat news video type:")
    print("1. 🔥 Trending Topic (AI-generated)")
    print("2. 📝 Custom Topic")
    print("3. 🚀 Quick Demo (pre-selected topic)")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        print("\n🔍 Generating trending topic...")
        package_path = studio.create_viral_cat_video()
        
    elif choice == "2":
        topic = input("\n📝 Enter your custom topic: ").strip()
        if not topic:
            topic = "Cats discover new way to knock things off tables"
        package_path = studio.create_viral_cat_video(topic)
        
    elif choice == "3":
        demo_topic = "AI robots start working as cat butlers"
        print(f"\n🚀 Creating demo video: {demo_topic}")
        package_path = studio.create_viral_cat_video(demo_topic)
        
    else:
        print("Invalid choice, using trending topic...")
        package_path = studio.create_viral_cat_video()
    
    # Show results
    print(f"\n🎉 SUCCESS! Your viral cat news video package is ready!")
    print(f"📁 Location: {package_path}")
    
    # List package contents
    if os.path.exists(package_path):
        print(f"\n📋 Package contents:")
        for file in sorted(os.listdir(package_path)):
            file_path = os.path.join(package_path, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                print(f"  - {file} ({size:,} bytes)")
    
    print(f"\n🎬 Next steps:")
    print(f"1. Open the package folder: {package_path}")
    print(f"2. Read README.md for production checklist")
    print(f"3. Film your cat following the script!")
    print(f"4. Upload and go viral! 🚀")

if __name__ == "__main__":
    main()
