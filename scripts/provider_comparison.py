#!/usr/bin/env python3
"""
Video Provider Comparison Tool
Compare MiniMax vs Google Veo 3 for AI Cat News Network
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.unified_video_generator import list_video_providers
from config.settings import get_setting, VIDEO_PROVIDERS
import json

def display_provider_comparison():
    """Display detailed comparison of video providers"""
    print("🔍 AI Video Generation Provider Comparison")
    print("=========================================")
    print()
    
    providers = list_video_providers()
    
    for provider in providers:
        print(f"🎬 {provider['name']}")
        print(f"   ID: {provider['provider']}")
        print(f"   Status: {'✅ Configured' if provider['status'] == 'configured' else '❌ Not Configured'}")
        print(f"   Pricing: {provider['pricing']}")
        print(f"   Features: {', '.join(provider['features'])}")
        
        # Get additional details from settings
        provider_id = provider['provider']
        if provider_id in VIDEO_PROVIDERS:
            details = VIDEO_PROVIDERS[provider_id]
            api_key = get_setting(details['api_key_env'])
            print(f"   API Key: {'✅ Set' if api_key else '❌ Missing'} ({details['api_key_env']})")
        
        print()

def show_setup_instructions():
    """Show setup instructions for each provider"""
    print("🚀 Setup Instructions")
    print("=====================")
    print()
    
    print("📋 MiniMax (HailuoAI) Setup:")
    print("1. Visit: https://www.minimaxi.com/")
    print("2. Sign up for an account")
    print("3. Navigate to API settings")
    print("4. Generate an API key")
    print("5. Add MINIMAX_API_KEY=your_key_here to your .env file")
    print("💰 Pricing: Paid service with usage-based billing")
    print()
    
    print("📋 Google Veo 3 Setup:")
    print("1. Visit: https://ai.google.dev/")
    print("2. Sign up for a free account")  
    print("3. Go to Google AI Studio")
    print("4. Generate an API key")
    print("5. Add GOOGLE_API_KEY=your_key_here to your .env file")
    print("💰 Pricing: Free tier available + paid options for higher usage")
    print()

def recommend_provider():
    """Provide provider recommendations based on use case"""
    print("💡 Provider Recommendations")
    print("===========================")
    print()
    
    print("🆓 For Free/Trial Usage:")
    print("   Recommended: Google Veo 3")
    print("   ✅ Free tier available")
    print("   ✅ High-quality output")
    print("   ✅ Part of Google's AI ecosystem")
    print("   ✅ Good for testing and development")
    print()
    
    print("💼 For Production/Commercial Use:")
    print("   Consider: Both providers based on needs")
    print("   📊 MiniMax: Established API, reliable service")
    print("   📊 Veo 3: Newer technology, potentially better quality")
    print("   📊 Test both to see which works better for your content")
    print()
    
    print("🎯 For Cat News Network Specifically:")
    print("   Best approach: Dual-provider setup")
    print("   ✅ Use Veo 3 for initial testing (free tier)")
    print("   ✅ Use MiniMax as backup/alternative")
    print("   ✅ Compare results and choose based on quality")
    print("   ✅ Have redundancy if one service is down")
    print()

def main():
    print("🎭 AI Cat News Network - Video Provider Analysis")
    print("===============================================")
    print()
    
    # Display current status
    display_provider_comparison()
    
    # Show setup instructions
    show_setup_instructions()
    
    # Provide recommendations
    recommend_provider()
    
    print("🔧 Quick Setup Check:")
    google_key = get_setting("GOOGLE_API_KEY")
    minimax_key = get_setting("MINIMAX_API_KEY")
    
    if google_key and minimax_key:
        print("✅ Both providers configured - you're ready for full testing!")
    elif google_key:
        print("✅ Google Veo 3 configured - you can start with free tier")
        print("⚠️  Consider adding MiniMax for comparison")
    elif minimax_key:
        print("✅ MiniMax configured - paid service ready")
        print("💡 Consider adding Google Veo 3 for free tier testing")
    else:
        print("❌ No providers configured")
        print("🚀 Start with Google Veo 3 (free tier) for testing")
    
    print()
    print("📈 Next Steps:")
    print("1. Configure at least one provider")
    print("2. Run the respective demo scripts")
    print("3. Compare video quality and features")
    print("4. Choose your preferred provider for production")
    print()
    print("✨ Analysis completed!")

if __name__ == "__main__":
    main()
