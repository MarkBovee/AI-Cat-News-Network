#!/usr/bin/env python3
"""
Test script for AI Cat News Video Generation
Create viral cat-themed news videos with current events
"""

import os
from dotenv import load_dotenv
from tools.content_tools import AIVideoCreationTool

# Load environment variables
load_dotenv()

def test_cat_news_ideas():
    """Test generating viral cat news ideas."""
    print("🐱 Testing Cat News Idea Generation")
    print("=" * 50)
    
    ai_video_tool = AIVideoCreationTool()
    
    try:
        ideas = ai_video_tool.generate_viral_cat_news_ideas(3)
        print("✅ Cat News Ideas Generated!")
        print("-" * 50)
        print(ideas)
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Error generating ideas: {e}")

def test_cat_news_video():
    """Test creating a complete cat news video."""
    print("\n🎬 Testing Full Cat News Video Creation")
    print("=" * 50)
    
    # Recent news topics you can use
    news_topics = [
        "AI technology advances in 2025",
        "Climate change solutions",
        "Space exploration updates", 
        "Social media platform changes",
        "Economic market updates"
    ]
    
    print("Available news topics:")
    for i, topic in enumerate(news_topics, 1):
        print(f"{i}. {topic}")
    
    try:
        choice = int(input("\nChoose a topic (1-5): ").strip()) - 1
        selected_topic = news_topics[choice]
    except (ValueError, IndexError):
        selected_topic = news_topics[0]  # Default
    
    print(f"\n🎯 Creating cat news video about: {selected_topic}")
    
    ai_video_tool = AIVideoCreationTool()
    
    try:
        result = ai_video_tool.create_cat_news_video(selected_topic)
        print(f"\n✅ {result}")
        
        # List created files
        print("\n📁 Generated files:")
        if os.path.exists("content/videos"):
            for file in os.listdir("content/videos"):
                print(f"  - content/videos/{file}")
        
        if os.path.exists("content/temp"):
            for file in os.listdir("content/temp"):
                print(f"  - content/temp/{file}")
                
    except Exception as e:
        print(f"❌ Error creating video: {e}")

def test_voice_over_only():
    """Test just the voice-over generation."""
    print("\n🎤 Testing Voice-Over Generation Only")
    print("=" * 50)
    
    test_script = """
    Good evening, I'm Whiskers McFluffington with Cat News Network.
    Breaking news tonight: Local humans have reportedly opened a new bag of treats.
    The cat community is purring with excitement over this development.
    We'll have more updates as this story develops. This is Cat News, goodnight.
    """
    
    ai_video_tool = AIVideoCreationTool()
    
    try:
        voice_path = "content/temp/test_voice.mp3"
        result = ai_video_tool._generate_voice_over(test_script, voice_path)
        
        if result and os.path.exists(result):
            print(f"✅ Voice-over created: {result}")
            file_size = os.path.getsize(result)
            print(f"📊 File size: {file_size} bytes")
        else:
            print("❌ Voice-over generation failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🐱 Cat News Video Generator Test Suite")
    print("=" * 60)
    
    # Check environment
    groq_key = os.getenv('GROQ_API_KEY')
    elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
    
    print(f"🔑 Groq API: {'✅' if groq_key else '❌'}")
    print(f"🔑 ElevenLabs API: {'✅' if elevenlabs_key else '❌'}")
    
    if not groq_key:
        print("⚠️ Groq API key not set - script generation will fail")
    if not elevenlabs_key:
        print("⚠️ ElevenLabs API key not set - voice-over will fail")
    
    print("\nChoose test:")
    print("1. 💡 Generate cat news ideas")
    print("2. 🎬 Create full cat news video") 
    print("3. 🎤 Test voice-over only")
    print("4. 🔄 Run all tests")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        test_cat_news_ideas()
    elif choice == "2":
        test_cat_news_video()
    elif choice == "3":
        test_voice_over_only()
    elif choice == "4":
        test_cat_news_ideas()
        test_cat_news_video()
        test_voice_over_only()
    else:
        print("Invalid choice, running idea generation...")
        test_cat_news_ideas()
    
    print("\n🏁 Testing completed!")
