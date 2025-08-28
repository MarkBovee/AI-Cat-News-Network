from crewai import Agent

def create_content_strategist():
    """Content strategist agent for generating content ideas."""
    return Agent(
        role='Content Strategist',
        goal='Generate engaging content ideas for YouTube Shorts and Instagram Reels',
        backstory="""You are a creative content strategist with deep understanding 
        of social media trends. You excel at identifying viral content opportunities 
        and creating content strategies that engage audiences.""",
        verbose=True,
        allow_delegation=False
    )

def create_script_writer():
    """Script writer agent for writing video scripts."""
    return Agent(
        role='Script Writer',
        goal='Write compelling scripts for short-form video content',
        backstory="""You are an experienced scriptwriter specializing in short-form 
        content. You know how to hook viewers in the first 3 seconds and maintain 
        engagement throughout the entire video.""",
        verbose=True,
        allow_delegation=False
    )

def create_visual_creator():
    """Visual creator agent for creating videos."""
    return Agent(
        role='Visual Creator',
        goal='Create engaging visuals and videos from scripts',
        backstory="""You are a skilled visual artist and video editor who specializes 
        in creating eye-catching content for social media. You understand the visual 
        language that resonates with online audiences.""",
        verbose=True,
        allow_delegation=False
    )

def create_social_media_manager():
    """Social media manager agent for uploading content."""
    return Agent(
        role='Social Media Manager',
        goal='Optimize and publish content across social media platforms',
        backstory="""You are a social media expert who understands platform-specific 
        requirements and optimal posting strategies. You know how to maximize reach 
        and engagement across different social networks.""",
        verbose=True,
        allow_delegation=False
    )
