# 🐱 AI Cat News Network

**Professional news content creation with AI-powered cat anchors for viral social media videos**

## 🆕 Multi-Provider Video Generation

### Supported Video Generation Providers

#### 🆓 Google Veo 3 (Recommended for Testing)
- **Free tier available** through Google AI Studio
- High-quality video generation
- 9:16 aspect ratio support for social media
- Easy setup with Google account

#### 💼 MiniMax (HailuoAI)
- Professional paid API service
- Reliable text-to-video generation
- Multiple duration options
- Established provider

## 🚀 Quick Start

### 1. Choose Your Video Provider

**For Free Testing (Recommended):**
```bash
# Get Google API key from https://ai.google.dev/
# Add to .env file:
GOOGLE_API_KEY=your_google_api_key_here
```

**For Production/Paid Service:**
```bash
# Get MiniMax API key from https://www.minimaxi.com/
# Add to .env file:
MINIMAX_API_KEY=your_minimax_api_key_here
```

### 2. Run the Setup

```powershell
# Windows PowerShell
.\run_cat_news_updated.ps1
```

### 3. Try the Demos

- **Option 2**: Google Veo 3 Demo (Free)
- **Option 1**: MiniMax Demo (Paid)
- **Option 3**: Compare Both Providers

## 🎬 Features

- **AI Script Generation**: Powered by Groq (fast & free)
- **Dual Video Providers**: Choose between Google Veo 3 and MiniMax
- **Voice Generation**: ElevenLabs integration
- **Social Media Optimized**: 9:16 vertical format
- **Cat News Personalities**: Multiple anchor characters
- **Complete Production Workflow**: Script → Video → Voice → Package

## 📋 Setup Requirements

### Required Environment Variables

```bash
# AI Script Generation (Free)
GROQ_API_KEY=your_groq_api_key

# Video Generation (Choose one or both)
GOOGLE_API_KEY=your_google_api_key      # Free tier available
MINIMAX_API_KEY=your_minimax_api_key    # Paid service

# Voice Generation (Optional)
ELEVENLABS_API_KEY=your_elevenlabs_key
ELEVENLABS_VOICE_ID=your_voice_id
```

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/AI-Cat-News-Network.git
cd AI-Cat-News-Network

# Install dependencies
pip install -r requirements.txt

# Run setup
.\run_cat_news_updated.ps1
```

## 🔍 Provider Comparison

| Feature | Google Veo 3 | MiniMax |
|---------|-------------|---------|
| **Pricing** | Free tier + paid | Paid only |
| **Quality** | High | High |
| **Setup** | Easy (Google account) | API signup required |
| **Best For** | Testing, development | Production |
| **Format Support** | 9:16 vertical | 9:16 vertical |

## 🎯 Cat News Content

### Anchor Personalities
- **Whiskers Winston**: Professional, slightly sarcastic
- **Fluffy McDouglas**: Serious journalist with playful moments  
- **Mittens McReporter**: Energetic field reporter

### Content Categories
- Technology and AI developments
- Environmental and climate news
- Social media platform changes
- Economic market updates
- Space exploration discoveries
- Entertainment industry news

## 📁 Project Structure

```
AI-Cat-News-Network/
├── scripts/                    # Python execution scripts
│   ├── veo3_video_demo.py     # Google Veo 3 demo
│   ├── ai_video_generator_demo.py  # MiniMax demo
│   ├── provider_comparison.py  # Compare providers
│   └── ...
├── tools/                     # Core tools and utilities
│   ├── unified_video_generator.py  # Multi-provider video generation
│   ├── ai_video_generator.py      # MiniMax integration
│   └── content_tools.py           # Content creation tools
├── config/                    # Configuration and settings
├── agents/                    # AI agent definitions
├── tasks/                     # Task definitions
├── workflows/                 # Workflow orchestration
├── content/                   # Generated content storage
└── output/                    # Final output packages
```

## 🔧 Development

### Running Tests
```bash
# Test AI setup
python scripts/test_groq_setup.py

# Test voice generation
python scripts/test_voice.py

# Compare video providers
python scripts/provider_comparison.py
```

### Creating Custom Content
```python
from tools.unified_video_generator import generate_cat_news_video

# Generate with Google Veo 3 (free)
result = generate_cat_news_video(
    "A cat reporting on space exploration", 
    provider="veo3",
    duration=30
)

# Generate with MiniMax (paid)
result = generate_cat_news_video(
    "A cat reporting on tech news",
    provider="minimax", 
    duration=30
)
```

## 💡 Tips & Best Practices

1. **Start with Google Veo 3** for free testing and development
2. **Use both providers** to compare quality and choose the best fit
3. **Test different prompts** to find what works best for each provider
4. **Keep prompts detailed** for better video generation results
5. **Use 9:16 aspect ratio** for optimal social media performance

## 🆘 Support

### Common Issues

**Video Generation Fails:**
- Check API key configuration
- Verify internet connection
- Try the provider comparison tool

**Poor Video Quality:**
- Refine your prompts with more detail
- Try the alternative provider
- Adjust duration settings

### Getting Help
- Check the provider comparison tool
- Review demo scripts for examples
- Ensure all API keys are properly configured

## 📈 Roadmap

- [ ] Additional video providers (Runway, Pika Labs)
- [ ] Advanced prompt templates
- [ ] Automated social media posting
- [ ] Analytics and performance tracking
- [ ] Voice cloning for consistent anchors
- [ ] Multi-language support

---

**Ready to create viral cat news content? Start with Google Veo 3's free tier today!** 🚀🐱