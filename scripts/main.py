import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents.content_agents import (
    create_content_strategist,
    create_script_writer,
    create_visual_creator,
    create_social_media_manager
)
from tasks.content_tasks import (
    create_content_idea_task,
    create_script_writing_task,
    create_video_creation_task,
    create_publishing_task
)

# Load environment variables
load_dotenv()

def run_content_creation_workflow(topic: str = "AI and technology"):
    """
    Main workflow for content creation.
    
    Args:
        topic (str): The topic for content creation
    """
    print(f"🚀 Starting content creation workflow for topic: {topic}")
    
    # Create agents
    print("🤖 Creating AI agents...")
    content_strategist = create_content_strategist()
    script_writer = create_script_writer()
    visual_creator = create_visual_creator()
    social_media_manager = create_social_media_manager()
    
    # Create tasks
    print("📋 Setting up tasks...")
    idea_task = create_content_idea_task(content_strategist)
    
    # Create crew
    crew = Crew(
        agents=[content_strategist, script_writer, visual_creator, social_media_manager],
        tasks=[idea_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute workflow
    print("🎬 Executing content creation workflow...")
    try:
        result = crew.kickoff()
        print("✅ Workflow completed successfully!")
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"❌ Error in workflow: {str(e)}")
        return None

def run_single_video_creation(content_idea: str):
    """
    Workflow for creating a single video.
    
    Args:
        content_idea (str): The content idea for the video
    """
    print(f"🎥 Creating single video for idea: {content_idea}")
    
    # Create agents
    script_writer = create_script_writer()
    visual_creator = create_visual_creator()
    social_media_manager = create_social_media_manager()
    
    # Create sequential tasks
    script_task = create_script_writing_task(script_writer, content_idea)
    
    # For now, we'll run tasks individually
    # In a full implementation, you'd chain these together
    crew = Crew(
        agents=[script_writer],
        tasks=[script_task],
        process=Process.sequential,
        verbose=True
    )
    
    try:
        result = crew.kickoff()
        print("✅ Script creation completed!")
        return result
    except Exception as e:
        print(f"❌ Error in video creation: {str(e)}")
        return None

if __name__ == "__main__":
    print("🎬 CrewAI Content Creation System")
    print("=" * 50)
    
    # Example usage
    print("\n1. Running content idea generation...")
    ideas_result = run_content_creation_workflow("AI automation tools")
    
    if ideas_result:
        print("\n2. Creating video from first idea...")
        sample_idea = "5 AI tools that will change how you work in 2024"
        video_result = run_single_video_creation(sample_idea)
    
    print("\n🏁 Demo completed!")
