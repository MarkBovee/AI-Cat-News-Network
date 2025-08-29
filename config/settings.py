# Cat News Video Creator Configuration

# MAIN PROJECT CONCEPT
PROJECT_CONCEPT = {
    "name": "Cat News Network", 
    "description": "AI-powered viral videos where cats act as professional news anchors reporting on actual world news events from a feline perspective",
    "target_platforms": ["YouTube Shorts", "Instagram Reels"],
    "content_style": "Professional news format with cat humor and personality"
}

# NEWS CATEGORIES FOR CAT REPORTING
NEWS_CATEGORIES = [
    "Technology and AI developments",
    "Environmental and climate news", 
    "Social media platform changes",
    "Economic market updates",
    "Space exploration discoveries",
    "Health and wellness trends",
    "Entertainment industry news",
    "Political developments (light humor)",
    "Scientific breakthroughs",
    "Consumer product launches"
]

# CAT NEWS ANCHOR PERSONALITIES
CAT_ANCHORS = {
    "whiskers_winston": {
        "name": "Whiskers Winston",
        "personality": "Professional, slightly sarcastic, loves cat puns",
        "specialty": "Breaking news and technology"
    },
    "fluffy_mcdouglas": {
        "name": "Fluffy McDouglas", 
        "personality": "Serious journalist with occasional playful moments",
        "specialty": "Economic and political news"
    },
    "mittens_reporter": {
        "name": "Mittens McReporter",
        "personality": "Energetic field reporter, very curious",
        "specialty": "Entertainment and social trends"
    }
}

# CONTENT SETTINGS
CONTENT_TYPES = {
    "breaking_news": {
        "duration": 30,
        "style": "urgent_professional", 
        "cta": "follow_for_updates"
    },
    "feature_story": {
        "duration": 30,
        "style": "informative_fun",
        "cta": "engagement"
    },
    "trending_update": {
        "duration": 25,
        "style": "casual_professional",
        "cta": "share_comment"
    }
}

# PLATFORM OPTIMIZATION
PLATFORM_SETTINGS = {
    "youtube_shorts": {
        "aspect_ratio": "9:16",
        "max_duration": 60,
        "optimal_duration": 30,
        "hashtag_limit": 10,
        "title_max_length": 100
    },
    "instagram_reels": {
        "aspect_ratio": "9:16", 
        "max_duration": 90,
        "optimal_duration": 30,
        "hashtag_limit": 30,
        "title_max_length": 150
    }
}

# VIRAL CONTENT FORMULA
VIRAL_FORMULA = {
    "hook_duration": 3,  # seconds
    "story_duration": 17, # seconds  
    "impact_duration": 7, # seconds
    "outro_duration": 3,  # seconds
    "total_target": 30    # seconds
}

# CAT BEHAVIOR ELEMENTS
CAT_BEHAVIORS = [
    "stretching and yawning",
    "batting at objects", 
    "sudden alertness to off-screen sounds",
    "brief grooming sessions",
    "judgmental stares at camera",
    "knocking things off the desk",
    "curling up for impromptu naps",
    "investigating papers/props"
]

# TRENDING HASHTAGS (Updated regularly)
TRENDING_HASHTAGS = [
    "#CatNews",
    "#ViralCats", 
    "#FelineNews",
    "#CatsOfTikTok",
    "#CatVideo",
    "#Shorts",
    "#Reels",
    "#FunnyNews",
    "#CatAnchor",
    "#PetContent"
]

# VIDEO PROVIDERS CONFIGURATION
VIDEO_PROVIDERS = {
    "google_veo3": {
        "name": "Google Veo 3",
        "api_key_env": "GOOGLE_API_KEY",
        "free_tier": True,
        "enabled": True
    },
    "minimax": {
        "name": "MiniMax",
        "api_key_env": "MINIMAX_API_KEY", 
        "free_tier": False,
        "enabled": True
    }
}

# HELPER FUNCTIONS
def get_setting(key, default=None):
    """Get a setting value from the configuration."""
    # This function provides access to all the settings defined above
    settings_dict = {
        'PROJECT_CONCEPT': PROJECT_CONCEPT,
        'NEWS_CATEGORIES': NEWS_CATEGORIES,
        'CAT_ANCHORS': CAT_ANCHORS,
        'CONTENT_TYPES': CONTENT_TYPES,
        'PLATFORM_SETTINGS': PLATFORM_SETTINGS,
        'TRENDING_HASHTAGS': TRENDING_HASHTAGS,
        'VIDEO_PROVIDERS': VIDEO_PROVIDERS
    }
    return settings_dict.get(key, default)
