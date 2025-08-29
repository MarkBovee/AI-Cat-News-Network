#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.ai_provider import ai_provider

load_dotenv()

# Quick test
print("🐱 Quick Cat News Test")
print("Creating trending cat news video...")

# Generate topic
topic_prompt = "Generate 1 current trending topic perfect for viral cat news. Return just the topic."
topic = ai_provider.generate_content(topic_prompt, max_tokens=30, temperature=0.7).strip()
print(f"📰 Topic: {topic}")

# Generate script
script_prompt = f"""
Create a funny 20-second cat news script about: {topic}

Format:
INTRO: Cat anchor introduces breaking news
MAIN: Key details from cat perspective with puns
OUTRO: Cat signs off with typical cat behavior

Keep it under 80 words total.
"""

script = ai_provider.generate_content(script_prompt, max_tokens=300, temperature=0.8)
print(f"📝 Script generated:")
print("-" * 40)
print(script)
print("-" * 40)

# Save to file
os.makedirs("content/quick_test", exist_ok=True)
with open("content/quick_test/cat_news_script.txt", "w") as f:
    f.write(f"Topic: {topic}\n\n{script}")

print("✅ Script saved to content/quick_test/cat_news_script.txt")
print("🎬 Ready for video production!")
