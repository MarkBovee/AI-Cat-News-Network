#!/usr/bin/env python3
"""
Test Runway ML Configuration Settings
Shows how the configurable settings work before running actual generation
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("🎛️ Runway ML Configuration Test")
print("=" * 45)

# Get configurable video settings from environment
config_duration = int(os.getenv('VIDEO_DURATION', '10'))
config_resolution = os.getenv('VIDEO_RESOLUTION', '1080p')
config_aspect_ratio = os.getenv('VIDEO_ASPECT_RATIO', '9:16')
config_quality = os.getenv('VIDEO_QUALITY', 'high')

print(f"📊 Current Settings (from .env file):")
print(f"    Duration: {config_duration} seconds")
print(f"    Resolution: {config_resolution}")
print(f"    Aspect Ratio: {config_aspect_ratio}")
print(f"    Quality: {config_quality}")

# Calculate cost estimates
cost_per_second = 12 / 60  # $12 per minute
estimated_cost = (config_duration * cost_per_second)

print(f"\n💰 Cost Estimation:")
print(f"    Current setting: ~${estimated_cost:.2f}")
print(f"    5s test: ~${(5 * cost_per_second):.2f}")
print(f"    10s test: ~${(10 * cost_per_second):.2f}")
print(f"    20s production: ~${(20 * cost_per_second):.2f}")
print(f"    30s full: ~${(30 * cost_per_second):.2f}")

print(f"\n🎯 Recommended Testing Progression:")
print(f"    1. Start with VIDEO_DURATION=5 (${(5 * cost_per_second):.2f}) for quick test")
print(f"    2. Try VIDEO_DURATION=10 (${(10 * cost_per_second):.2f}) for longer test")
print(f"    3. Use VIDEO_DURATION=20+ for production videos")

print(f"\n🔧 To change settings, edit .env file:")
print(f"    VIDEO_DURATION={config_duration}    # Change to 5, 10, 15, 20, etc.")
print(f"    VIDEO_RESOLUTION={config_resolution}  # Options: 720p, 1080p, 2160p")
print(f"    VIDEO_QUALITY={config_quality}     # Options: standard, high, premium")

# Check if API key is configured
runway_api_key = os.getenv('RUNWAY_API_KEY')
if runway_api_key and runway_api_key != 'your_runway_api_key_here':
    print(f"\n✅ Runway ML API Key: Configured")
    print(f"🚀 Ready to generate {config_duration}s video!")
else:
    print(f"\n❌ Runway ML API Key: Not configured")
    print(f"🔗 Get your key from: https://runwayml.com/account/api-keys")

print(f"\n💡 Next step: Run .\AI-Cat-News-Studio.ps1 7 to generate video")
