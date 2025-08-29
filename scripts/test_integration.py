#!/usr/bin/env python3
"""
Integration Test for AI Cat News Network
Tests Google Veo 3 and MiniMax video generation providers
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing Module Imports...")
    
    try:
        from tools.unified_video_generator import UnifiedVideoGenerator, list_video_providers
        print("✅ Unified video generator imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import unified video generator: {e}")
        return False
    
    try:
        from config.settings import get_setting, VIDEO_PROVIDERS
        print("✅ Settings module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import settings: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI imported successfully")
    except ImportError as e:
        print(f"❌ Google AI package not installed: {e}")
        print("📦 Install with: pip install google-generativeai")
        return False
    
    return True

def test_provider_detection():
    """Test that providers are detected correctly"""
    print("\n🔍 Testing Provider Detection...")
    
    try:
        from tools.unified_video_generator import list_video_providers
        providers = list_video_providers()
        
        print(f"📊 Found {len(providers)} video providers:")
        for provider in providers:
            status_emoji = "✅" if provider["status"] == "configured" else "❌"
            print(f"  {status_emoji} {provider['name']} ({provider['provider']})")
        
        return len(providers) >= 2  # Should have at least MiniMax and Veo3
    except Exception as e:
        print(f"❌ Provider detection failed: {e}")
        return False

def test_veo3_initialization():
    """Test Google Veo 3 initialization"""
    print("\n🆕 Testing Google Veo 3 Initialization...")
    
    try:
        from tools.unified_video_generator import UnifiedVideoGenerator
        
        generator = UnifiedVideoGenerator("veo3")
        info = generator.get_provider_info()
        
        print(f"📋 Provider: {info['name']}")
        print(f"📊 Status: {info['status']}")
        print(f"💰 Pricing: {info['pricing']}")
        print(f"🔧 Features: {', '.join(info['features'])}")
        
        return True
    except Exception as e:
        print(f"❌ Veo3 initialization failed: {e}")
        return False

def test_minimax_initialization():
    """Test MiniMax initialization"""
    print("\n🎬 Testing MiniMax Initialization...")
    
    try:
        from tools.unified_video_generator import UnifiedVideoGenerator
        
        generator = UnifiedVideoGenerator("minimax")
        info = generator.get_provider_info()
        
        print(f"📋 Provider: {info['name']}")
        print(f"📊 Status: {info['status']}")
        print(f"💰 Pricing: {info['pricing']}")
        print(f"🔧 Features: {', '.join(info['features'])}")
        
        return True
    except Exception as e:
        print(f"❌ MiniMax initialization failed: {e}")
        return False

def test_api_key_configuration():
    """Test API key configuration"""
    print("\n🔑 Testing API Key Configuration...")
    
    try:
        from config.settings import get_setting
        
        google_key = get_setting("GOOGLE_API_KEY")
        minimax_key = get_setting("MINIMAX_API_KEY")
        groq_key = get_setting("GROQ_API_KEY")
        
        print(f"Google API Key: {'✅ Configured' if google_key else '❌ Missing'}")
        print(f"MiniMax API Key: {'✅ Configured' if minimax_key else '❌ Missing'}")
        print(f"Groq API Key: {'✅ Configured' if groq_key else '❌ Missing'}")
        
        if google_key or minimax_key:
            print("✅ At least one video provider is configured")
            return True
        else:
            print("⚠️  No video providers configured")
            return False
            
    except Exception as e:
        print(f"❌ API key check failed: {e}")
        return False

def test_mock_video_generation():
    """Test mock video generation (no API calls)"""
    print("\n� Testing Mock Video Generation...")
    
    try:
        from tools.unified_video_generator import UnifiedVideoGenerator
        
        # Test with a provider that likely doesn't have API key configured
        test_prompt = "A professional cat anchor reporting breaking news"
        
        print("Testing Veo3 mock generation...")
        veo3_generator = UnifiedVideoGenerator("veo3")
        veo3_result = veo3_generator.generate_video_from_prompt(test_prompt, duration=5)
        
        print(f"  Status: {veo3_result['status']}")
        print(f"  Provider: {veo3_result.get('provider', 'unknown')}")
        
        print("Testing MiniMax mock generation...")
        minimax_generator = UnifiedVideoGenerator("minimax")
        minimax_result = minimax_generator.generate_video_from_prompt(test_prompt, duration=5)
        
        print(f"  Status: {minimax_result['status']}")
        print(f"  Provider: {minimax_result.get('provider', 'unknown')}")
        
        return True
    except Exception as e:
        print(f"❌ Mock generation failed: {e}")
        return False

def main():
    print("🐱 AI Cat News Network - Integration Test")
    print("=========================================")
    print()
    
    tests = [
        ("Module Imports", test_imports),
        ("Provider Detection", test_provider_detection),
        ("Veo3 Initialization", test_veo3_initialization),
        ("MiniMax Initialization", test_minimax_initialization),
        ("API Key Configuration", test_api_key_configuration),
        ("Mock Video Generation", test_mock_video_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
    
    print(f"\n� Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Integration is working correctly.")
        print("\n🚀 Ready to use:")
        print("  • Run ./run_cat_news_updated.ps1")
        print("  • Try option 2 for Google Veo 3 demo")
        print("  • Try option 3 for provider comparison")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        print("\n🔧 Common fixes:")
        print("  • Install missing packages: pip install -r requirements.txt")
        print("  • Configure API keys in .env file")
        print("  • Check file paths and imports")
    
    print()
    print("✨ Integration test completed!")

if __name__ == "__main__":
    main()
try:
    from tools.unified_video_generator import UnifiedVideoGenerator, list_video_providers
    print("✅ Unified video generator imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")

try:
    from config.settings import VIDEO_PROVIDERS, get_setting
    print("✅ Settings imported successfully")
except ImportError as e:
    print(f"❌ Settings import error: {e}")

# Test 2: Check video providers
print()
print("🔍 Testing provider listing...")
try:
    providers = list_video_providers()
    print(f"✅ Found {len(providers)} video providers:")
    for provider in providers:
        print(f"   - {provider['name']} ({provider['provider']})")
except Exception as e:
    print(f"❌ Provider listing error: {e}")

# Test 3: Check API keys
print()
print("🔑 Checking API configuration...")
import os
from dotenv import load_dotenv

load_dotenv()

google_key = os.getenv('GOOGLE_API_KEY')
minimax_key = os.getenv('MINIMAX_API_KEY')

print(f"Google API Key: {'✅ Configured' if google_key else '❌ Not configured'}")
print(f"MiniMax API Key: {'✅ Configured' if minimax_key else '❌ Not configured'}")

# Test 4: Try creating generators
print()
print("🎬 Testing video generator creation...")
try:
    veo3_gen = UnifiedVideoGenerator("veo3")
    print("✅ Veo 3 generator created successfully")
    
    minimax_gen = UnifiedVideoGenerator("minimax") 
    print("✅ MiniMax generator created successfully")
except Exception as e:
    print(f"❌ Generator creation error: {e}")

print()
print("🎯 Integration test completed!")
print()
print("Next steps:")
print("1. Add your API keys to .env file")
print("2. Run the full demo scripts")
print("3. Test video generation with real prompts")
