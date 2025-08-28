#!/usr/bin/env python3
"""
Simple Cat News Generator - Text and Voice Only
Demo without video dependencies
"""

import os
from dotenv import load_dotenv
from config.ai_provider import ai_provider

# Load environment variables
load_dotenv()

class SimpleCatNewsGenerator:
    """Simple cat news generator without video dependencies."""
    
    def __init__(self):
        self.output_dir = "content/cat_news"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_cat_news_ideas(self, count: int = 3) -> str:
        """Generate viral cat news video ideas."""
        prompt = f"""
        Generate {count} viral cat news video ideas for YouTube Shorts.
        
        Make them about current events but from a cat's perspective - funny and shareable!
        
        Each idea should be:
        - A serious news topic but told by cats
        - Funny with cat puns and behavior
        - Perfect for 30-second videos
        - Viral-worthy content
        
        Format:
        1. Title: [Catchy title with cat puns]
           Topic: [News angle from cat perspective] 
           Hook: [Opening line that grabs attention]
           Key Points: [Main content points]
           Outro: [Funny cat sign-off]
        """
        
        return ai_provider.generate_content(prompt, max_tokens=800, temperature=0.8)
    
    def create_cat_news_script(self, topic: str) -> str:
        """Generate a complete cat news script."""
        prompt = f"""
        Create a hilarious 30-second cat news script about: {topic}
        
        STYLE: Professional news but with cat behavior and cat puns
        PERSPECTIVE: Cats are the news anchors and reporters
        TONE: Funny but informative
        
        FORMAT:
        [0-3s] INTRO: "Good evening, I'm [Cat Name] with Cat News Network..."
        [3-15s] MAIN NEWS: Explain the topic from cat perspective with puns
        [15-25s] IMPACT: How this affects the cat community/world
        [25-30s] OUTRO: Typical cat sign-off with cat behavior
        
        Include:
        - Cat puns and wordplay
        - Typical cat behaviors (napping, hunting, judging humans)
        - News anchor professionalism but with cat personality
        - Make it shareable and viral-worthy
        """
        
        return ai_provider.generate_content(prompt, max_tokens=500, temperature=0.8)
    
    def save_content(self, title: str, content: str) -> str:
        """Save generated content to file."""
        filename = f"{self.output_dir}/{title.lower().replace(' ', '_').replace(':', '')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Cat News Content: {title}\n")
            f.write("=" * 50 + "\n\n")
            f.write(content)
            f.write(f"\n\nGenerated on: {os.getcwd()}")
        
        return filename

def main():
    print("🐱 Cat News Generator - Simple Demo")
    print("=" * 50)
    
    # Check API keys
    groq_key = os.getenv('GROQ_API_KEY')
    print(f"🔑 Groq API: {'✅ Connected' if groq_key else '❌ Not set'}")
    
    if not groq_key:
        print("⚠️ Please set GROQ_API_KEY in .env file")
        return
    
    generator = SimpleCatNewsGenerator()
    
    print("\nWhat would you like to generate?")
    print("1. 💡 Cat news video ideas")
    print("2. 📝 Cat news script for specific topic")
    print("3. 🔄 Both")
    
    choice = input("\nChoice (1-3): ").strip()
    
    if choice in ["1", "3"]:
        print("\n🧠 Generating cat news ideas...")
        try:
            ideas = generator.generate_cat_news_ideas(3)
            print("\n✅ Cat News Ideas Generated!")
            print("-" * 60)
            print(ideas)
            print("-" * 60)
            
            # Save ideas
            ideas_file = generator.save_content("Cat News Ideas", ideas)
            print(f"💾 Saved to: {ideas_file}")
            
        except Exception as e:
            print(f"❌ Error generating ideas: {e}")
    
    if choice in ["2", "3"]:
        print("\n📝 Creating cat news script...")
        
        # Example topics
        topics = [
            "AI becomes more popular than catnip",
            "Humans working from home disrupts cat nap schedules", 
            "New study shows cats are actually in charge",
            "Global shortage of cardboard boxes causes panic",
            "Social media influencer cats demand higher treat payments"
        ]
        
        print("\nSample topics:")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")
        
        custom_topic = input("Enter custom topic or choose number (1-5): ").strip()
        
        if custom_topic.isdigit() and 1 <= int(custom_topic) <= 5:
            selected_topic = topics[int(custom_topic) - 1]
        elif custom_topic:
            selected_topic = custom_topic
        else:
            selected_topic = topics[0]
        
        print(f"\n🎬 Creating script for: {selected_topic}")
        
        try:
            script = generator.create_cat_news_script(selected_topic)
            print("\n✅ Cat News Script Generated!")
            print("-" * 60)
            print(script)
            print("-" * 60)
            
            # Save script
            script_file = generator.save_content(f"Script - {selected_topic}", script)
            print(f"💾 Saved to: {script_file}")
            
        except Exception as e:
            print(f"❌ Error generating script: {e}")
    
    print(f"\n📁 All files saved in: {generator.output_dir}/")
    print("🏁 Demo completed!")

if __name__ == "__main__":
    main()
