#!/usr/bin/env python3
"""
MiniMax API Test: Simple test to verify MiniMax integration
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.ai_video_generator import MiniMaxVideoGenerator

def main():
    print("🧪 MiniMax API Test")
    print("=" * 30)
    
    # Create MiniMax generator
    generator = MiniMaxVideoGenerator()
    
    # Test simple prompt
    test_prompt = "A professional orange cat wearing glasses sitting at a news desk"
    
    print(f"🎬 Testing MiniMax API with prompt: {test_prompt}")
    print("⏳ This will make a real API call...")
    
    # Generate video
    result = generator.generate_video_from_prompt(test_prompt, duration=5)
    
    print("\n📊 Result:")
    print(f"   Status: {result.get('status')}")
    print(f"   Message: {result.get('message', 'N/A')}")
    
    if result.get('video_url'):
        print(f"   🎥 Video URL: {result['video_url']}")
    elif result.get('task_id'):
        print(f"   🔄 Task ID: {result['task_id']}")
    
    print("\n✅ MiniMax API test completed!")

if __name__ == "__main__":
    main()
