import os
from typing import Optional, Dict, Any
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AIProviderManager:
    """
    Manages Groq AI provider for fast and free content generation.
    Simplified setup focusing on Groq only for cleaner architecture.
    """
    
    def __init__(self):
        self.provider = 'groq'
        self.model = os.getenv('AI_MODEL', 'llama3-70b-8192')
        self.client = self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Groq AI client."""
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return Groq(api_key=api_key)
    
    def generate_content(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Generate content using Groq AI.
        
        Args:
            prompt: The input prompt
            max_tokens: Maximum tokens to generate
            temperature: Creativity level (0.0-1.0)
            
        Returns:
            Generated content as string
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error generating content with Groq: {str(e)}")
            return "Error: Could not generate content. Please check your Groq API configuration."
    
    def get_provider_info(self) -> Dict[str, Any]:
        """Get information about the current provider."""
        return {
            'provider': self.provider,
            'model': self.model,
            'status': 'connected' if self.client else 'disconnected'
        }

# Global instance for easy access
ai_provider = AIProviderManager()

# Helper functions for backward compatibility
def generate_content_ideas(topic: str, count: int = 5) -> str:
    """Generate content ideas using the configured AI provider."""
    prompt = f"""
    Generate {count} engaging content ideas for YouTube Shorts and Instagram Reels about {topic}.
    Each idea should be unique, viral-worthy, and suitable for 30-second videos.
    
    Format each idea as:
    {count}. Title: [Catchy title]
       Description: [Brief description]
       Hook: [Opening hook for first 3 seconds]
       Target: [Target audience]
    """
    
    return ai_provider.generate_content(prompt, max_tokens=800, temperature=0.7)

def write_script(content_idea: str) -> str:
    """Write a script for a content idea using the configured AI provider."""
    prompt = f"""
    Write a compelling 30-second script for this content idea:
    {content_idea}
    
    Format:
    [0-3s] HOOK: [Attention-grabbing opening]
    [3-15s] CONTENT: [Main content/story]
    [15-25s] VALUE: [Key takeaway/lesson]
    [25-30s] CTA: [Call to action]
    
    Include visual cues in brackets.
    Make it engaging and optimized for social media.
    """
    
    return ai_provider.generate_content(prompt, max_tokens=500, temperature=0.7)

def generate_hashtags(content_description: str) -> str:
    """Generate hashtags for content using AI."""
    prompt = f"""
    Generate 15 relevant hashtags for this content:
    {content_description}
    
    Include a mix of:
    - Broad trending hashtags (#viral, #fyp)
    - Content-specific hashtags
    - Niche hashtags for better reach
    
    Return as a comma-separated list.
    """
    
    return ai_provider.generate_content(prompt, max_tokens=200, temperature=0.5)
