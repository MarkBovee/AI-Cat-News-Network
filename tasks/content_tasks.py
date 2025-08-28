from crewai import Task

def create_content_idea_task(agent):
    """Task for generating content ideas."""
    return Task(
        description="""
        Generate 5 engaging content ideas for YouTube Shorts and Instagram Reels.
        Focus on trending topics, educational content, or entertaining concepts.
        Each idea should include:
        - A catchy title
        - Brief description
        - Target audience
        - Estimated engagement potential
        """,
        agent=agent,
        expected_output="A list of 5 content ideas with detailed descriptions"
    )

def create_script_writing_task(agent, content_idea):
    """Task for writing a script."""
    return Task(
        description=f"""
        Write a compelling 30-second script for the following content idea:
        {content_idea}
        
        The script should:
        - Hook viewers in the first 3 seconds
        - Be concise and engaging
        - Include clear call-to-action
        - Be optimized for vertical video format
        - Include timing cues for visuals
        """,
        agent=agent,
        expected_output="A detailed 30-second script with timing cues and visual directions"
    )

def create_video_creation_task(agent, script):
    """Task for creating a video."""
    return Task(
        description=f"""
        Create a short-form video based on this script:
        {script}
        
        Requirements:
        - Duration: 30 seconds maximum
        - Format: Vertical (9:16 aspect ratio)
        - Include engaging visuals
        - Add background music if appropriate
        - Ensure high quality output
        """,
        agent=agent,
        expected_output="A completed video file ready for social media posting"
    )

def create_publishing_task(agent, video_content):
    """Task for publishing content."""
    return Task(
        description=f"""
        Prepare and optimize the following content for publishing:
        {video_content}
        
        Tasks:
        - Generate appropriate hashtags
        - Write engaging captions
        - Optimize for each platform (YouTube Shorts vs Instagram Reels)
        - Schedule optimal posting time
        - Prepare thumbnail if needed
        """,
        agent=agent,
        expected_output="Platform-optimized content packages ready for publishing"
    )
