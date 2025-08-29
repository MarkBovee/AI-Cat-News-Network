#!/usr/bin/env python3
"""
Short Cat News Script Generator
Creates ultra-short scripts optimized for 6-second videos
"""
import os
import sys
import json
import time
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

# Get API key
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("❌ GROQ_API_KEY not found in environment variables")
    exit(1)

print("🎬 Short Cat News Script Generator (6-Second Optimized)")
print("=" * 60)

# Real news topics optimized for quick delivery
short_news_topics = [
    "Japan creates robot that perfectly mimics cat movements",
    "Scientists discover cats understand physics better than expected", 
    "New study shows cats have 276 facial expressions",
    "AI learns to predict cat behavior with 99% accuracy",
    "World's first cat cafe in space opens next year",
    "Researchers find cats can recognize their names in any language",
    "Smart litter box uses AI to monitor cat health",
    "Cat videos officially declared most valuable internet content"
]

import random
selected_topic = random.choice(short_news_topics)

print(f"📰 Selected Topic: {selected_topic}")

# Create ultra-short script (6-second format)
short_script = f"""**6-SECOND CAT NEWS FLASH**

*Professional cat anchor Whiskers at news desk*

"Breaking: {selected_topic}. 
*dramatic pause, ear twitch*
Typical humans... trying to keep up with us cats.
*confident head nod*
This is Whiskers. Stay superior."

*Quick tail flick and fade out*

---
VOICE TIMING: 5-6 seconds maximum
VIDEO STYLE: Quick cuts, professional news format
CAT BEHAVIOR: Subtle ear movements, confident expressions
"""

print("📝 Ultra-Short Script Generated:")
print("=" * 50)
print(short_script)
print("=" * 50)

# Save the script using content manager
timestamp = time.strftime("%Y%m%d_%H%M%S")

# Save script using content manager
script_id = content_manager.save_script(
    content=short_script,
    script_type="short_cat_news_6s"
)

print(f"✅ Short script saved with ID: {script_id}")
print(f"🎬 Optimized for: 6-second video generation")
print(f"⏱️  Target voice duration: 5-6 seconds")
print(f"🎯 Perfect for: MiniMax Hailuo 720p generation")

print(f"\n🎤 Next step: Generate voice-over with .\\AI-Cat-News-Studio.ps1 2")
print(f"🎬 Then generate video with: .\\AI-Cat-News-Studio.ps1 4")

if __name__ == "__main__":
    input("\nPress Enter to continue...")
