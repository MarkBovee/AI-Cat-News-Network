#!/usr/bin/env python3
"""
AI Video Demo: AI Cat News Network with Real AI Video Generation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.content_tools import AIVideoCreationTool

def main():
    print("🐱 Starting AI Cat News Network - AI VIDEO DEMO")
    print("=" * 60)
    
    creator = AIVideoCreationTool()
    
    # Test the new AI video generation
    news_topic = "Breaking: Scientists Discover Cats Have Been Running Secret Underground Economy"
    
    print(f"📰 Creating AI-generated video for: {news_topic}")
    print()
    
    # Use the new AI video generation method
    result = creator.create_ai_generated_video(news_topic)
    
    print()
    print("🎬 Result:", result)
    print()
    print("✅ Demo completed! Check the output directory for your AI-generated cat news video.")

if __name__ == "__main__":
    main()
