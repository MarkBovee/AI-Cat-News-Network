#!/usr/bin/env python3
"""
Test Complete Cat News Workflow - AI Cat News Network
Demonstrates the full end-to-end pipeline from script to video
"""

import os
import sys
import time
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

def test_workflow():
    """Test the complete cat news video generation workflow"""
    
    print("🧪 Testing Complete Cat News Workflow")
    print("=" * 50)
    
    try:
        # Step 1: Generate content
        print("📝 Step 1: Generating script and audio...")
        test_prompt = "Breaking news: Local cat elected mayor, promises tuna for all!"
        result = os.system(f'python scripts/create_quick_video.py "{test_prompt}" 5')
        if result != 0:
            print("❌ Script/audio generation failed")
            return False
        
        # Wait a moment
        time.sleep(1)
        
        # Step 2: Create video
        print("\n🎬 Step 2: Creating video...")
        result = os.system("python scripts/create_basic_video.py")
        if result != 0:
            print("❌ Video creation failed")
            return False
        
        print("\n✅ Complete workflow test successful!")
        print("🎯 Generated: Script + Audio + Video")
        print("💡 Check content/ folders for all files")
        
        return True
        
    except Exception as e:
        print(f"❌ Workflow test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 AI Cat News Network - Workflow Test")
    print("Testing complete pipeline: Content → Audio → Video")
    print()
    
    success = test_workflow()
    
    if success:
        print("\n🎉 WORKFLOW TEST PASSED!")
        print("🔥 AI Cat News Network is ready for production!")
    else:
        print("\n❌ WORKFLOW TEST FAILED")
        print("💡 Check individual components")
        sys.exit(1)
