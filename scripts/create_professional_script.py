#!/usr/bin/env python3
"""
Professional Video Script Generator for AI Cat News Network
Creates detailed video scripts optimized for AI video generation with visual descriptions
"""
import os
import sys
import time
from dotenv import load_dotenv

# Add the parent directory to sys.path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.content_manager import content_manager

load_dotenv()

def create_professional_video_script(news_text, duration_seconds):
    """Create a detailed video script optimized for AI video generation"""
    print(f"Professional Video Script Generator - {duration_seconds}s")
    print("=" * 55)
    
    # Validate inputs
    if not news_text or len(news_text.strip()) < 10:
        print("❌ News text must be at least 10 characters long")
        return False
    
    if duration_seconds < 3 or duration_seconds > 30:
        print("❌ Duration must be between 3 and 30 seconds for optimal results")
        return False
    
    print(f"News: {news_text}")
    print(f"Duration: {duration_seconds} seconds")
    
    # Create professional video script with detailed visual descriptions
    script_content = generate_detailed_script(news_text, duration_seconds)
    
    # Save the script
    try:
        script_path = content_manager.save_script(script_content, script_type=f"professional_{duration_seconds}s")
        script_filename = os.path.basename(script_path)
        print(f"Professional script saved: {script_filename}")
        
        # Display script preview
        print(f"\nScript Preview:")
        print("=" * 50)
        print(script_content[:500] + "..." if len(script_content) > 500 else script_content)
        print("=" * 50)
        
        return script_path
        
    except Exception as e:
        print(f"❌ Failed to save script: {e}")
        return False

def generate_detailed_script(news_text, duration):
    """Generate a detailed script with visual descriptions for AI video generation"""
    
    # Professional cat news anchor setup
    studio_setup = """**PROFESSIONAL CAT NEWS VIDEO SCRIPT**

**STUDIO SETUP:**
Modern news studio with blue and silver gradient backdrop, professional broadcast lighting setup. Orange tabby cat wearing tiny black news tie sits behind polished glass news desk with subtle newsroom graphics. Soft key lighting from left, fill light from right, background slightly out of focus for professional depth of field.

**CAMERA SETUP:**
Medium close-up shot (waist up), fixed professional camera position, broadcast quality 1080p, slight warm color grading typical of news broadcasts. Camera height at cat's eye level for authoritative perspective."""

    # Time-based action descriptions for different durations
    if duration <= 6:
        action_script = f"""
**ACTION TIMELINE (0-{duration} seconds):**
0-1s: Cat sits in perfect news anchor posture, ears forward, looking directly at camera with alert, professional expression. Tail positioned neatly behind desk.

1-3s: Cat maintains steady eye contact with camera while speaking. Subtle ear movements show attentiveness. Whiskers occasionally twitch with natural cat expressions.

3-{duration}s: Cat demonstrates professional anchor behaviors - slight head tilt for emphasis, ears rotating as if listening to producer, maintaining dignified posture throughout delivery."""

    elif duration <= 10:
        action_script = f"""
**ACTION TIMELINE (0-{duration} seconds):**
0-2s: Cat sits in professional news anchor position, ears perked forward, serious expression, direct eye contact with camera.

2-5s: While delivering news, cat shows natural behaviors - head tilts for emphasis, ear movements, whisker twitches. Maintains professional demeanor.

5-{duration}s: Cat occasionally glances at off-camera teleprompter, returns gaze to camera. Subtle grooming gesture (paw to whisker) adds authentic cat behavior while maintaining news anchor authority."""

    else:
        action_script = f"""
**ACTION TIMELINE (0-{duration} seconds):**
0-3s: Professional opening - cat in perfect anchor pose, direct camera eye contact, ears forward.

3-8s: Mid-segment natural cat behaviors while speaking - head tilts, ear rotations, whisker movements. Occasional glance at desk papers.

8-15s: Cat demonstrates engagement with story - leaning slightly forward for emphasis, tail swish behind desk, maintaining professional composure.

15-{duration}s: Professional closing - cat straightens posture, direct camera gaze, slight head nod as if signing off to commercial break."""

    # Style and technical specifications
    technical_specs = f"""
**VISUAL STYLE:**
Cinematic broadcast quality, professional news lighting, shallow depth of field, stable camera work. Realistic cat behavior blended seamlessly with professional news anchor authority. Clean, modern newsroom aesthetic.

**AUDIO SYNC:**
"{news_text}"

**DURATION:** {duration} seconds
**QUALITY:** Broadcast professional, mobile-optimized 9:16 aspect ratio
**MOOD:** Authoritative yet charming, professional news with delightful cat personality"""

    return studio_setup + action_script + technical_specs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_professional_script.py \"News text here\" duration_seconds")
        print("Example: python create_professional_script.py \"Breaking: Cats demand more treats!\" 6")
        sys.exit(1)
    
    news_text = sys.argv[1]
    try:
        duration = int(sys.argv[2])
    except ValueError:
        print("Duration must be a number")
        sys.exit(1)
    
    script_path = create_professional_video_script(news_text, duration)
    if script_path:
        print(f"Ready for video generation!")
        print(f"Script saved at: {script_path}")
        print(f"Next: Use this script with your video generation provider")
    else:
        sys.exit(1)
