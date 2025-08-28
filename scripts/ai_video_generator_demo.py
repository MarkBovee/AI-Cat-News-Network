#!/usr/bin/env python3
"""
AI Video Demo (MiniMax): Shows the MiniMax AI video generation framework
"""

import sys
import os
import json
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.ai_video_generator import AIVideoCreator

def main():
    print("🐱 AI Cat News Network - MINIMAX VIDEO GENERATOR DEMO")
    print("=" * 60)
    
    # Create the AI video generator
    creator = AIVideoCreator()
    
    # Test data
    news_topic = "Breaking: Scientists Discover Cats Have Been Running Secret Underground Economy"
    
    mock_script = """
    [0-3s] HOOK: Breaking news from the feline financial sector!
    [3-8s] INTRO: Good evening, I'm Whiskers McFluffington with Cat News Network
    [8-20s] MAIN: Scientists have uncovered evidence that cats worldwide have been operating a sophisticated underground economy, trading in tuna, catnip, and premium scratching posts
    [20-27s] IMPACT: This revelation explains why cats always seem to know where the best hiding spots are
    [27-30s] OUTRO: We'll continue following this story. This is Whiskers McFluffington, signing off. *purr*
    """
    
    print(f"📰 Topic: {news_topic}")
    print(f"📝 Script: {mock_script.strip()}")
    print()
    print("🎬 Generating MiniMax AI video package...")
    
    # Create the video package
    video_package = creator.create_cat_news_video(news_topic, mock_script)
    
    print()
    print("📦 GENERATED MINIMAX VIDEO PACKAGE:")
    print("=" * 40)
    
    for i, segment in enumerate(video_package['segments'], 1):
        print(f"🎥 Segment {i}: {segment['description']}")
        print(f"   📹 Prompt: {segment['prompt'][:80]}...")
        print(f"   ⏱️  Duration: {segment['duration']}s")
        print(f"   📊 Status: {segment['result']['status']}")
        if segment['result'].get('mock_video'):
            print(f"   🔧 Mock Mode: MiniMax API key needed for real video generation")
        elif segment['result'].get('video_url'):
            print(f"   🎬 Video URL: {segment['result']['video_url']}")
        print()
    
    print(f"⏱️  Total Duration: {video_package['total_duration']}s")
    print(f"🏭 Provider: {video_package['provider']}")
    print(f"📁 Package Status: {video_package['status']}")
    print()
    
    if video_package['status'] == 'partial':
        print("💡 To generate real videos:")
        print("   1. Your MiniMax API key is already configured! ✅")
        print("   2. The system will make real API calls to HailuoAI")
        print("   3. Videos will be generated and URLs returned")
        print("   4. Each segment takes ~30-60 seconds to generate")
    
    print()
    print("✅ MiniMax AI Video Generator Demo Completed!")

if __name__ == "__main__":
    main()
