#!/usr/bin/env python3
"""
Content Manager for AI Cat News Network
Handles organized content storage and retrieval
"""
import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

class ContentManager:
    """Manages organized content storage for AI Cat News Network"""
    
    def __init__(self, base_path: str = "content"):
        self.base_path = base_path
        self.newsitems_path = os.path.join(base_path, "newsitems")
        self.ideas_path = os.path.join(base_path, "ideas")
        self.scripts_path = os.path.join(base_path, "scripts")
        self.audio_path = os.path.join(base_path, "audio")
        self.video_path = os.path.join(base_path, "video")
        
        # Ensure all directories exist
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create all content directories if they don't exist"""
        for path in [self.newsitems_path, self.ideas_path, self.scripts_path, 
                     self.audio_path, self.video_path]:
            os.makedirs(path, exist_ok=True)
    
    def _generate_timestamp(self) -> str:
        """Generate timestamp for file naming"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def save_news_item(self, topic: str, source: str = "real_news", metadata: Optional[Dict] = None) -> str:
        """Save a news item/topic for processing"""
        timestamp = self._generate_timestamp()
        filename = f"newsitem_{timestamp}.json"
        filepath = os.path.join(self.newsitems_path, filename)
        
        news_data = {
            "timestamp": timestamp,
            "topic": topic,
            "source": source,
            "metadata": metadata or {},
            "status": "pending"
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def save_script(self, content: str, news_item_id: Optional[str] = None, script_type: str = "cat_news") -> str:
        """Save a generated script"""
        timestamp = self._generate_timestamp()
        filename = f"script_{script_type}_{timestamp}.txt"
        filepath = os.path.join(self.scripts_path, filename)
        
        # Save script content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Save metadata
        metadata_file = filepath.replace('.txt', '_metadata.json')
        metadata = {
            "timestamp": timestamp,
            "script_type": script_type,
            "news_item_id": news_item_id,
            "filepath": filepath,
            "character_count": len(content),
            "word_count": len(content.split())
        }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return filepath
    
    def save_audio(self, audio_data: bytes, script_filepath: str, voice_settings: Optional[Dict] = None) -> str:
        """Save generated audio file"""
        timestamp = self._generate_timestamp()
        script_name = os.path.basename(script_filepath).replace('.txt', '')
        filename = f"audio_{script_name}_{timestamp}.mp3"
        filepath = os.path.join(self.audio_path, filename)
        
        # Save audio file
        with open(filepath, 'wb') as f:
            f.write(audio_data)
        
        # Save metadata
        metadata_file = filepath.replace('.mp3', '_metadata.json')
        metadata = {
            "timestamp": timestamp,
            "script_filepath": script_filepath,
            "voice_settings": voice_settings or {},
            "audio_filepath": filepath,
            "file_size_kb": len(audio_data) / 1024
        }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return filepath
    
    def save_video(self, video_data: bytes, audio_filepath: str, video_settings: Optional[Dict] = None) -> str:
        """Save generated video file"""
        timestamp = self._generate_timestamp()
        audio_name = os.path.basename(audio_filepath).replace('.mp3', '')
        filename = f"video_{audio_name}_{timestamp}.mp4"
        filepath = os.path.join(self.video_path, filename)
        
        # Save video file
        with open(filepath, 'wb') as f:
            f.write(video_data)
        
        # Save metadata
        metadata_file = filepath.replace('.mp4', '_metadata.json')
        metadata = {
            "timestamp": timestamp,
            "audio_filepath": audio_filepath,
            "video_settings": video_settings or {},
            "video_filepath": filepath,
            "file_size_kb": len(video_data) / 1024
        }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return filepath
    
    def save_idea(self, idea: str, category: str = "general", metadata: Optional[Dict] = None) -> str:
        """Save a content idea for future use"""
        timestamp = self._generate_timestamp()
        filename = f"idea_{category}_{timestamp}.json"
        filepath = os.path.join(self.ideas_path, filename)
        
        idea_data = {
            "timestamp": timestamp,
            "idea": idea,
            "category": category,
            "metadata": metadata or {},
            "status": "new"
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(idea_data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def get_latest_files(self, content_type: str, limit: int = 5) -> list:
        """Get the latest files of a specific content type"""
        type_mapping = {
            "newsitems": (self.newsitems_path, ['.json']),
            "scripts": (self.scripts_path, ['.txt']),
            "audio": (self.audio_path, ['.mp3']),
            "video": (self.video_path, ['.mp4']),
            "ideas": (self.ideas_path, ['.json'])
        }
        
        if content_type not in type_mapping:
            raise ValueError(f"Unknown content type: {content_type}")
        
        path, extensions = type_mapping[content_type]
        files = []
        
        for filename in os.listdir(path):
            # Check if file has the right extension and is not a metadata file
            if (any(filename.endswith(ext) for ext in extensions) and 
                not filename.endswith('_metadata.json')):
                filepath = os.path.join(path, filename)
                files.append({
                    "filename": filename,
                    "filepath": filepath,
                    "modified": os.path.getmtime(filepath)
                })
        
        # Sort by modification time (newest first)
        files.sort(key=lambda x: x["modified"], reverse=True)
        return files[:limit]
    
    def create_content_package(self, script_filepath: str, audio_filepath: str, 
                             video_filepath: Optional[str] = None) -> Dict[str, Any]:
        """Create a complete content package with all assets"""
        timestamp = self._generate_timestamp()
        
        package = {
            "timestamp": timestamp,
            "package_id": f"catnews_{timestamp}",
            "script": script_filepath,
            "audio": audio_filepath,
            "video": video_filepath,
            "status": "complete" if video_filepath else "partial"
        }
        
        # Save package metadata
        package_file = os.path.join(self.base_path, f"package_{timestamp}.json")
        with open(package_file, 'w') as f:
            json.dump(package, f, indent=2)
        
        return package

# Global instance for easy importing
content_manager = ContentManager()
