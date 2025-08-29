#!/usr/bin/env python3
"""
Test script for Groq AI provider
Run this test to check if Groq is working before setting up the API key.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_groq_setup():
    """Test Groq configuration and setup."""
    print("🚀 Testing CrewAI with Groq Setup")
    print("=" * 50)
    
    # Check if Groq is configured
    groq_key = os.getenv('GROQ_API_KEY')
    ai_provider = os.getenv('AI_PROVIDER', 'groq')
    
    print(f"📋 AI Provider: {ai_provider}")
    print(f"🔑 Groq API Key: {'✅ Set' if groq_key and groq_key != 'your_groq_api_key_here' else '❌ Not set'}")
    
    if not groq_key or groq_key == 'your_groq_api_key_here':
        print("\n⚠️  Groq API Key not configured!")
        print("\n📝 To get a free Groq API key:")
        print("1. Go to: https://console.groq.com/")
        print("2. Sign up for a free account")
        print("3. Go to API Keys section")
        print("4. Create a new API key")
        print("5. Copy the .env.example to .env")
        print("6. Replace 'your_groq_api_key_here' with your actual key")
        print("\n💡 Groq offers:")
        print("   - Free tier with generous limits")
        print("   - Very fast inference")
        print("   - Great models like Llama 3.1 70B")
        return False
    
    # Test import
    try:
        from config.ai_provider import ai_provider, generate_content_ideas
        print("✅ AI Provider imported successfully")
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Test connection (if API key is set)
    try:
        print("\n🧪 Testing AI generation...")
        test_result = generate_content_ideas("AI automation", 2)
        print("✅ Content generation test successful!")
        print("\n📄 Sample output:")
        print("-" * 30)
        print(test_result[:200] + "..." if len(test_result) > 200 else test_result)
        print("-" * 30)
        return True
    except Exception as e:
        print(f"❌ Generation test failed: {e}")
        print("💡 This might be due to:")
        print("   - Invalid API key")
        print("   - Network connection issues")
        print("   - Groq service temporarily unavailable")
        return False

if __name__ == "__main__":
    success = test_groq_setup()
    
    if success:
        print("\n🎉 All tests passed! Your CrewAI setup is ready.")
        print("🚀 You can now run: python main.py")
    else:
        print("\n🔧 Please fix the issues above before proceeding.")
        print("📖 Check the README.md for detailed setup instructions.")
