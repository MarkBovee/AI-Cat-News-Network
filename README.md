# 🐱 AI Cat News Network

**AI-powered cat news anchors creating viral social media content with real news stories and feline commentary**

## ⚠️ CRITICAL PROJECT RULE: NO MOVIEPY EVER
**MOVIEPY IS COMPLETELY FORBIDDEN** - This project uses AI video generation only:
- ✅ MiniMax Hailuo AI Video Generation
- ✅ Runway ML Gen-4 AI Video Generation  
- ✅ HunyuanVideo via Wan2GP Local AI Generation
- ❌ **NEVER MoviePy or any local video editing libraries**

## 🎯 What This Does

Transform real news into entertaining cat commentary videos perfect for:
- 📱 **YouTube Shorts** (vertical 9:16 format)
- 📸 **Instagram Reels** (optimized for engagement)
- 🎵 **TikTok** (viral-ready content)

Our AI cats report on actual human news with hilarious feline perspective, superior attitude, and professional news anchor format.

## � Quick Start

### 1. Setup & Launch
```powershell
# Windows - Run the PowerShell Studio
.\AI-Cat-News-Studio.ps1
```

This automatically:
- ✅ Checks Python installation
- ✅ Creates/activates virtual environment
- ✅ Installs all dependencies (CrewAI 0.175.0, ElevenLabs, etc.)
- ✅ Shows interactive menu with 12 options

### 2. Test the Pipeline

**Start Simple (Recommended):**
- **Option 1**: Generate Cat News Script → Creates script from real news
- **Option 2**: Generate Voice-Over → Creates professional voice-over  
- **Option 6**: Browse Content → See your organized files

**Video Generation Options:**
- **Option 4**: MiniMax Hailuo (6s, Professional, ~$0.10)
- **Option 5**: Google Veo 3 (Variable, Advanced AI)
- **Option 7**: Runway ML Gen-4 (Configurable, Cinematic, ~$1-8) ⭐ **RECOMMENDED**
- **New**: Pika Labs (High-quality, 9:16 optimized)
- **New**: Dream Machine (Exceptional quality, cinematic results) ⭐ **HIGH QUALITY**

**Runway ML Configuration** (in .env file):
- `VIDEO_DURATION=10` (5-90 seconds, start with 10s for testing)
- `VIDEO_RESOLUTION=1080p` (720p/1080p/2160p)
- `VIDEO_QUALITY=high` (standard/high/premium)

**Advanced Testing:**
- **Option 3**: Veo 3 Metadata Preparation
- **Full Automation**: Run script → voice → video → cleanup

## 📁 Project Structure

```
AI-Cat-News-Network/
├── AI-Cat-News-Studio.ps1     # 🎛️ Main PowerShell interface
├── content/                   # 📦 All generated content (organized)
│   ├── newsitems/            # 📰 Real news stories selected
│   ├── scripts/              # 📝 Generated cat news scripts  
│   ├── audio/                # 🎤 Voice-over files
│   └── video/                # 🎬 Final video productions
├── scripts/                  # 🔧 Individual test scripts
├── agents/                   # 🤖 CrewAI agent definitions
├── tools/                    # ⚙️ AI video generation tools
├── config/                   # ⚙️ AI provider settings
└── utils/                    # 🛠️ Content management utilities
```

## 🎬 Content Production Pipeline

### 1. News Selection & Script Generation
- **Real News Sources**: Curated actual news stories (corgis racing, AI developments, etc.)
- **Cat Commentary**: Professional news format with feline superiority complex
- **AI Generation**: Powered by Groq AI (Llama 3.1 70B model)
- **Viral Optimization**: Hook + Story + Impact + Cat sign-off structure

### 2. Voice Generation
- **ElevenLabs Integration**: Professional AI voice-over
- **News Anchor Voice**: Authoritative yet playful cat personality
- **Automatic Processing**: Reads scripts and generates high-quality audio

### 3. Video Creation
- **Multiple Providers**: Choose Google Veo 3 (free) or MiniMax (paid)
- **Social Media Format**: Vertical 9:16 optimized for TikTok/Reels/Shorts
- **Professional Output**: Complete video packages ready for upload

## 🎥 Video Generation Options

| Type                          | Model / Platform                                                     | Highlights                                     |
| ----------------------------- | -------------------------------------------------------------------- | ---------------------------------------------- |
| **Open-source (self-hosted)** | HunyuanVideo, Open-Sora, Waver, VideoCrafter1, CogVideoX-Flash       | Full control, free if you host/run it yourself |
| **API wrappers**              | OpenVideoGen                                                         | Turn local models into API services easily     |
| **Hosted free tiers**         | Replicate models, Dream Machine, Hailuo, Pika Labs, Runway, Reelmind | Access without infra, some free credits/plans  |
| **Community tools**           | Chipling.xyz, studio.sefirot.io                                      | Experimental platforms; may require vetting    |

### Current Implementation Status
- ✅ **Hailuo (MiniMax)** - Working but needs account funding
- ✅ **Runway ML** - Working with configurable settings  
- ✅ **HunyuanVideo** - Framework ready, needs model integration
- ✅ **Pika Labs** - Working (API key required)
- ✅ **Dream Machine** - Working (API key required)
- 📋 **CogVideoX-Flash** - Planned

## 🎮 PowerShell Studio Menu

Run `.\AI-Cat-News-Studio.ps1` to access:

```
1. 🎬 MiniMax Video Generator Demo (Paid API)
2. 🆕 Google Veo 3 Video Generator Demo (Free Tier)
3. 🔍 Compare Video Providers 
4. 📰 Quick Cat News Test (Generate script from real news)
5. 🧪 Test Groq AI Setup
6. 🎤 Test Voice Generation  
7. 🚀 Full Production Demo - MiniMax
8. 🚀 Full Production Demo - Veo 3
9. 🧪 Integration Test (All Systems)
10. � Test Individual Components
11. 🧬 Test Agent Framework (CrewAI workflow)
12. 📁 Browse Content Structure (View organized files)
```

## 🔧 Configuration

### Required API Keys

Create a `.env` file in the project root:

```env
# Primary AI Provider (Free and Fast)
GROQ_API_KEY=your_groq_api_key_here

# Video Generation Providers
GOOGLE_API_KEY=your_google_api_key_here      # Free tier available
MINIMAX_API_KEY=your_minimax_api_key_here    # Professional paid service

# Voice Generation
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=your_preferred_voice_id

# Optional: Video Upload Integration
YOUTUBE_API_KEY=your_youtube_api_key_here
```

### Getting API Keys

- **Groq**: Free at [console.groq.com](https://console.groq.com)
- **Google Veo 3**: Free tier at [ai.google.dev](https://ai.google.dev)
- **MiniMax**: Paid service at [minimaxi.com](https://www.minimaxi.com)
- **ElevenLabs**: Voice generation at [elevenlabs.io](https://elevenlabs.io)

## 🏗️ Technical Architecture

### CrewAI Framework (v0.175.0)
- **Multi-Agent System**: Coordinated AI agents for content creation
- **Task Management**: Automated workflow from news to video
- **Tool Integration**: Unified interface for all AI services

### Content Management
- **Organized Structure**: Automatic file organization by content type
- **Metadata Tracking**: Complete information about generation settings
- **Pipeline Linking**: Files automatically linked across production stages
- **Scalable Storage**: Ready for hundreds of videos

### AI Providers
- **Script Generation**: Groq AI (fast, free, reliable)
- **Video Creation**: Google Veo 3 + MiniMax (multiple options)
- **Voice Synthesis**: ElevenLabs (professional quality)

## 📊 Content Examples

### Real News Stories We Cover
- "Dozens of corgis compete for racing and costume titles in Lithuania"
- "Scientists discover new species of deep-sea fish with glowing fins"
- "Marathon runner completes race while juggling for entire 26.2 miles"
- "Artist creates massive sand sculpture visible from space"

### Cat Commentary Style
- **Professional Format**: News anchor intro/main/outro structure
- **Feline Perspective**: Superior attitude with humorous observations
- **Viral Elements**: Puns, relatable content, engaging hooks
- **Social Media Ready**: 20-30 second format perfect for shorts

## 🚀 Getting Started

### Windows Users
```powershell
# 1. Clone the repository
git clone https://github.com/MarkBovee/AI-Cat-News-Network.git
cd AI-Cat-News-Network

# 2. Run the PowerShell studio
.\AI-Cat-News-Studio.ps1

# 3. Start with option 4 (Quick Cat News Test)
# Then try option 6 (Voice Generation)
# Finally explore option 12 (Content Browser)
```

### Testing the Pipeline
1. **Start Simple**: Option 4 → Generates script from real news
2. **Add Voice**: Option 6 → Creates professional voice-over  
3. **View Results**: Option 12 → Browse your organized content
4. **Go Advanced**: Options 1-2 → Full video generation

## 📈 Project Status

✅ **Working Features**:
- Real news script generation with cat commentary
- ElevenLabs voice generation (modern API)
- Organized content structure with metadata
- PowerShell studio interface with 12 options
- CrewAI framework updated to latest version (0.175.0)
- Content browser and pipeline tracking

🚧 **In Development**:
- Video generation integration testing
- Automated social media posting
- Multiple cat anchor personalities
- Batch content creation workflows

## 🤝 Contributing

This project uses:
- **CrewAI 0.175.0** for multi-agent workflows
- **Python 3.13** with virtual environment
- **PowerShell** for Windows integration
- **Git-crypt** for secure API key storage

## 📄 License

MIT License - Create as many cat news videos as your heart desires! 🐱📺