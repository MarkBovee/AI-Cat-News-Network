import os
from dotenv import load_dotenv
from config.ai_provider import ai_provider

load_dotenv()

print("🎬 Final Cat News Demo")
print("Creating complete video package...")

# Create the viral cat video
topic = "AI-powered smart litter boxes track cat behavior"
print(f"Topic: {topic}")

# Generate script
script_prompt = f"""Create a 30-second professional cat news script about: {topic}

Format with timing:
[0-3s] HOOK: Attention-grabbing opener
[3-8s] INTRO: Cat anchor introduction  
[8-20s] MAIN: Key story details with cat puns
[20-27s] IMPACT: What this means for cats
[27-30s] OUTRO: Cat sign-off

Make it viral-worthy and funny."""

script = ai_provider.generate_content(script_prompt, max_tokens=600, temperature=0.8)

# Generate metadata  
meta_prompt = f"""Create viral YouTube metadata for cat news video about {topic}:
- Catchy title (under 60 chars)
- Description (2 sentences)
- 10 hashtags
Format as: TITLE: | DESCRIPTION: | HASHTAGS:"""

metadata = ai_provider.generate_content(meta_prompt, max_tokens=300, temperature=0.7)

# Save package
os.makedirs("content/final_demo", exist_ok=True)

with open("content/final_demo/COMPLETE_VIDEO_PACKAGE.txt", "w", encoding="utf-8") as f:
    f.write("🐱 COMPLETE CAT NEWS VIDEO PACKAGE\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"TOPIC: {topic}\n\n")
    f.write("SCRIPT WITH TIMING:\n")
    f.write("-" * 30 + "\n")
    f.write(script)
    f.write("\n\n" + "=" * 50 + "\n")
    f.write("VIRAL METADATA:\n")
    f.write("-" * 30 + "\n")
    f.write(metadata)
    f.write("\n\n" + "=" * 50 + "\n")
    f.write("PRODUCTION NOTES:\n")
    f.write("- Film in vertical 9:16 format\n")
    f.write("- Use good lighting on cat\n")
    f.write("- Add news desk props\n")
    f.write("- Sync voice-over with cat footage\n")
    f.write("- Export for YouTube Shorts/Instagram Reels\n")

print("✅ Complete video package saved!")
print("📁 Check: content/final_demo/COMPLETE_VIDEO_PACKAGE.txt")
print("🎬 Ready for viral cat news production! 🚀")
