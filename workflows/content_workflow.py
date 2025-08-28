from crewai import Crew, Process
from agents.content_agents import *
from tasks.content_tasks import *

class ContentCreationWorkflow:
    """
    Complete workflow for content creation from idea to publication.
    """
    
    def __init__(self):
        self.content_strategist = create_content_strategist()
        self.script_writer = create_script_writer()
        self.visual_creator = create_visual_creator()
        self.social_media_manager = create_social_media_manager()
    
    def generate_content_ideas(self, topic: str, count: int = 5):
        """Generate content ideas for a specific topic."""
        task = create_content_idea_task(self.content_strategist)
        
        crew = Crew(
            agents=[self.content_strategist],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew.kickoff()
    
    def create_video_from_idea(self, content_idea: str):
        """Complete video creation workflow from idea to video."""
        # Task 1: Write script
        script_task = create_script_writing_task(self.script_writer, content_idea)
        
        # Task 2: Create video (placeholder - would take script as input)
        video_task = create_video_creation_task(self.visual_creator, "Generated script")
        
        # Task 3: Prepare publishing
        publish_task = create_publishing_task(self.social_media_manager, "Generated video")
        
        crew = Crew(
            agents=[self.script_writer, self.visual_creator, self.social_media_manager],
            tasks=[script_task, video_task, publish_task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew.kickoff()
    
    def daily_content_batch(self, topics: list, videos_per_topic: int = 1):
        """Create a batch of content for multiple topics."""
        results = []
        
        for topic in topics:
            print(f"Processing topic: {topic}")
            
            # Generate ideas
            ideas = self.generate_content_ideas(topic, videos_per_topic)
            
            # For each idea, create a video
            for i in range(videos_per_topic):
                video_result = self.create_video_from_idea(f"Video {i+1} about {topic}")
                results.append(video_result)
        
        return results

class QuickVideoWorkflow:
    """
    Simplified workflow for quick video creation.
    """
    
    def __init__(self):
        self.script_writer = create_script_writer()
    
    def quick_script(self, idea: str):
        """Quickly generate script for an idea."""
        task = create_script_writing_task(self.script_writer, idea)
        
        crew = Crew(
            agents=[self.script_writer],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        return crew.kickoff()
