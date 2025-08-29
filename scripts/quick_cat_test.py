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

# Real news topics that cats would report on
real_news_topics = [
    "Dozens of corgis compete for racing and costume titles in Lithuania",
    "Dozens of corgis compete for racing and costume titles in Lithuania",  # Adding twice for higher chance
    "Scientists discover new species of deep-sea fish with glowing fins",
    "Town's annual pumpkin festival breaks attendance records with 50,000 visitors",
    "Researchers develop AI that can predict weather patterns 30 days in advance",
    "Local bakery creates world's largest cinnamon roll weighing 1,200 pounds",
    "Marathon runner completes race while juggling for entire 26.2 miles",
    "New study shows urban gardens reduce city temperatures by 5 degrees",
    "Artist creates massive sand sculpture visible from space",
    "Community volunteers plant 10,000 trees in single weekend",
    "Hotel offers guests chance to sleep in transparent pods under northern lights"
]

import random
topic = random.choice(real_news_topics)
print(f"📰 Real News Topic: {topic}")

# Generate script
script_prompt = f"""
You are a professional cat news anchor reporting REAL human news but from a feline perspective. 

Create a hilarious 20-second cat news script about this REAL news story: {topic}

Requirements:
- Report the actual human news accurately
- Add cat commentary, reactions, and puns throughout
- Show cats are either jealous, confused, or dismissive of human activities
- Include typical cat behaviors and attitudes

Format:
**INTRO** (3-4 seconds)
(Serious news music. Professional cat anchor at desk)
"Good evening, I'm [Cat Name] with breaking human news..."

**MAIN** (12-14 seconds)  
Report the actual story but with cat reactions like:
- "While we cats have been [doing superior cat thing], humans are apparently..."
- Include cat puns and superior attitude
- Show bewilderment at human behavior

**OUTRO** (3-4 seconds)
Cat signs off with typical dismissive cat behavior
"And that's why cats remain superior. Now excuse me while I [cat activity]."

Keep it under 100 words total. Make it viral-worthy with cat humor!
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
