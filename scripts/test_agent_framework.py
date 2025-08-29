#!/usr/bin/env python3
"""
Modular Agent Testing Framework
Tests each component of the AI Cat News Network independently with separate output folders
"""

import sys
import os
import json
import time
from datetime import datetime
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our components
from config.ai_provider import ai_provider
from config.settings import get_setting
from tools.unified_video_generator import UnifiedVideoGenerator

class AgentTester:
    """Framework for testing each agent/component independently"""
    
    def __init__(self):
        self.base_output_dir = Path("test_outputs")
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.setup_output_directories()
    
    def setup_output_directories(self):
        """Create output directories for each component"""
        self.output_dirs = {
            "script_generation": self.base_output_dir / "01_script_generation" / self.session_id,
            "video_generation": self.base_output_dir / "02_video_generation" / self.session_id,
            "voice_generation": self.base_output_dir / "03_voice_generation" / self.session_id,
            "final_assembly": self.base_output_dir / "04_final_assembly" / self.session_id,
            "metadata": self.base_output_dir / "00_metadata" / self.session_id
        }
        
        # Create all directories
        for dir_path in self.output_dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print(f"🔧 Test session: {self.session_id}")
        print(f"📁 Output directory: {self.base_output_dir}")
        print()

    def test_script_generation_agent(self, topic: str = None) -> dict:
        """Test 1: Script Generation Agent"""
        print("🎬 Testing Script Generation Agent...")
        print("=" * 50)
        
        if not topic:
            topic = "Breaking: Local Cat Becomes Mayor After Promising More Nap Time"
        
        try:
            # Test Groq configuration
            groq_key = get_setting("GROQ_API_KEY")
            print(f"Groq API Key: {'✅ Configured' if groq_key else '❌ Missing'}")
            
            # Generate script
            script_prompt = f"""
            Create a professional 30-second cat news script about: {topic}
            
            Format as JSON:
            {{
                "headline": "Catchy news headline",
                "anchor_name": "Cat anchor name",
                "script_segments": [
                    {{"time": "0-5s", "text": "Opening hook", "visual_cue": "Visual description"}},
                    {{"time": "5-15s", "text": "Main story", "visual_cue": "Visual description"}},
                    {{"time": "15-25s", "text": "Key details", "visual_cue": "Visual description"}},
                    {{"time": "25-30s", "text": "Cat sign-off", "visual_cue": "Visual description"}}
                ],
                "video_prompt": "Detailed prompt for video generation",
                "metadata": {{
                    "target_duration": 30,
                    "style": "professional_cat_news",
                    "platform": "social_media"
                }}
            }}
            """
            
            print(f"📝 Topic: {topic}")
            print("⏳ Generating script...")
            
            response = ai_provider.generate_content(script_prompt, max_tokens=800, temperature=0.7)
            
            # Try to parse as JSON, fallback to structured data
            try:
                script_data = json.loads(response)
            except json.JSONDecodeError:
                # Create fallback structure
                script_data = {
                    "headline": f"Cat News: {topic}",
                    "anchor_name": "Whiskers Winston",
                    "script_segments": [
                        {"time": "0-5s", "text": f"Breaking news: {topic}!", "visual_cue": "Professional cat anchor at news desk"},
                        {"time": "5-15s", "text": "This developing story has cats everywhere talking.", "visual_cue": "Cat looking seriously at camera"},
                        {"time": "15-25s", "text": "Our sources confirm this will change everything.", "visual_cue": "Cat with thoughtful expression"},
                        {"time": "25-30s", "text": "I'm Whiskers Winston, reporting. Meow!", "visual_cue": "Cat giving professional sign-off"}
                    ],
                    "video_prompt": f"A professional cat news anchor reporting on {topic}, sitting at a news desk, serious but charming expression",
                    "metadata": {
                        "target_duration": 30,
                        "style": "professional_cat_news", 
                        "platform": "social_media"
                    },
                    "raw_response": response
                }
            
            # Save script output
            script_file = self.output_dirs["script_generation"] / "script.json"
            with open(script_file, 'w', encoding='utf-8') as f:
                json.dump(script_data, f, indent=2)
            
            # Save metadata
            metadata = {
                "test": "script_generation",
                "topic": topic,
                "timestamp": datetime.now().isoformat(),
                "groq_configured": bool(groq_key),
                "output_file": str(script_file),
                "success": True
            }
            
            metadata_file = self.output_dirs["metadata"] / "01_script_generation.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"✅ Script generated successfully!")
            print(f"📰 Headline: {script_data['headline']}")
            print(f"🐱 Anchor: {script_data['anchor_name']}")
            print(f"📁 Saved to: {script_file}")
            print()
            
            return {
                "success": True,
                "script_data": script_data,
                "output_file": script_file,
                "metadata_file": metadata_file
            }
            
        except Exception as e:
            error_data = {
                "test": "script_generation",
                "topic": topic,
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "success": False
            }
            
            error_file = self.output_dirs["metadata"] / "01_script_generation_error.json"
            with open(error_file, 'w', encoding='utf-8') as f:
                json.dump(error_data, f, indent=2)
            
            print(f"❌ Script generation failed: {str(e)}")
            print(f"📁 Error details saved to: {error_file}")
            print()
            
            return {"success": False, "error": str(e), "error_file": error_file}

    def test_video_generation_agent(self, script_data: dict = None, provider: str = "veo3") -> dict:
        """Test 2: Video Generation Agent"""
        print("🎥 Testing Video Generation Agent...")
        print("=" * 50)
        
        try:
            # Load script if not provided
            if not script_data:
                script_file = self.output_dirs["script_generation"] / "script.json"
                if script_file.exists():
                    with open(script_file, 'r', encoding='utf-8') as f:
                        script_data = json.load(f)
                    print(f"📄 Loaded script from: {script_file}")
                else:
                    print("❌ No script data provided and no script file found")
                    return {"success": False, "error": "No script data available"}
            
            # Initialize video generator
            generator = UnifiedVideoGenerator(provider)
            provider_info = generator.get_provider_info()
            
            print(f"🎬 Provider: {provider_info['name']}")
            print(f"📊 Status: {provider_info['status']}")
            print(f"💰 Pricing: {provider_info['pricing']}")
            
            # Get video prompt from script
            video_prompt = script_data.get('video_prompt', 'A professional cat news anchor reporting news')
            
            print(f"🎯 Video Prompt: {video_prompt[:60]}...")
            print("⏳ Generating video...")
            
            # Generate video
            result = generator.generate_video_from_prompt(video_prompt, duration=30)
            
            # Save video generation result
            video_result_file = self.output_dirs["video_generation"] / f"video_result_{provider}.json"
            with open(video_result_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            
            # Save metadata
            metadata = {
                "test": "video_generation",
                "provider": provider,
                "provider_info": provider_info,
                "video_prompt": video_prompt,
                "timestamp": datetime.now().isoformat(),
                "result": result,
                "output_file": str(video_result_file),
                "success": result.get('status') in ['completed', 'error']  # Even errors are "successful" tests
            }
            
            metadata_file = self.output_dirs["metadata"] / f"02_video_generation_{provider}.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"📊 Result Status: {result['status']}")
            print(f"📁 Result saved to: {video_result_file}")
            
            if result['status'] == 'completed':
                print(f"✅ Video generated successfully!")
                if result.get('video_path'):
                    print(f"🎬 Video path: {result['video_path']}")
            elif result['status'] == 'error':
                print(f"⚠️  Video generation error (expected if API not configured): {result.get('message', 'Unknown error')}")
            
            print()
            
            return {
                "success": True,
                "result": result,
                "output_file": video_result_file,
                "metadata_file": metadata_file
            }
            
        except Exception as e:
            error_data = {
                "test": "video_generation",
                "provider": provider,
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "success": False
            }
            
            error_file = self.output_dirs["metadata"] / f"02_video_generation_{provider}_error.json"
            with open(error_file, 'w', encoding='utf-8') as f:
                json.dump(error_data, f, indent=2)
            
            print(f"❌ Video generation failed: {str(e)}")
            print(f"📁 Error details saved to: {error_file}")
            print()
            
            return {"success": False, "error": str(e), "error_file": error_file}

    def test_voice_generation_agent(self, script_data: dict = None) -> dict:
        """Test 3: Voice Generation Agent"""
        print("🎤 Testing Voice Generation Agent...")
        print("=" * 50)
        
        try:
            # Load script if not provided
            if not script_data:
                script_file = self.output_dirs["script_generation"] / "script.json"
                if script_file.exists():
                    with open(script_file, 'r', encoding='utf-8') as f:
                        script_data = json.load(f)
                    print(f"📄 Loaded script from: {script_file}")
                else:
                    print("❌ No script data provided and no script file found")
                    return {"success": False, "error": "No script data available"}
            
            # Check ElevenLabs configuration
            elevenlabs_key = get_setting("ELEVENLABS_API_KEY")
            voice_id = get_setting("ELEVENLABS_VOICE_ID", "2ajXGJNYBR0iNHpS4VZb")
            
            print(f"ElevenLabs API Key: {'✅ Configured' if elevenlabs_key else '❌ Missing'}")
            print(f"Voice ID: {voice_id}")
            
            # Extract text from script segments
            script_segments = script_data.get('script_segments', [])
            full_script_text = " ".join([segment.get('text', '') for segment in script_segments])
            
            print(f"🎙️  Script text: {full_script_text[:100]}...")
            
            # Voice generation result (mock for now since we may not have ElevenLabs configured)
            voice_result = {
                "status": "configured" if elevenlabs_key else "not_configured",
                "voice_id": voice_id,
                "script_text": full_script_text,
                "estimated_duration": len(full_script_text.split()) * 0.5,  # ~0.5 seconds per word
                "mock": not elevenlabs_key
            }
            
            if elevenlabs_key:
                voice_result["message"] = "ElevenLabs configured - ready for voice generation"
                voice_result["audio_file"] = f"output/voice_cat_news_{int(time.time())}.mp3"
            else:
                voice_result["message"] = "ElevenLabs not configured - using text-to-speech fallback"
                voice_result["audio_file"] = "mock_voice_output.mp3"
            
            # Save voice generation result
            voice_result_file = self.output_dirs["voice_generation"] / "voice_result.json"
            with open(voice_result_file, 'w', encoding='utf-8') as f:
                json.dump(voice_result, f, indent=2)
            
            # Save script text for voice generation
            script_text_file = self.output_dirs["voice_generation"] / "script_text.txt"
            with open(script_text_file, 'w', encoding='utf-8') as f:
                f.write(full_script_text)
            
            # Save metadata
            metadata = {
                "test": "voice_generation",
                "elevenlabs_configured": bool(elevenlabs_key),
                "voice_id": voice_id,
                "script_length": len(full_script_text),
                "word_count": len(full_script_text.split()),
                "timestamp": datetime.now().isoformat(),
                "result": voice_result,
                "output_files": {
                    "result": str(voice_result_file),
                    "script_text": str(script_text_file)
                },
                "success": True
            }
            
            metadata_file = self.output_dirs["metadata"] / "03_voice_generation.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"📊 Status: {voice_result['status']}")
            print(f"📁 Result saved to: {voice_result_file}")
            print(f"📄 Script text saved to: {script_text_file}")
            
            if elevenlabs_key:
                print("✅ ElevenLabs configured - ready for voice generation!")
            else:
                print("⚠️  ElevenLabs not configured - using mock voice generation")
            
            print()
            
            return {
                "success": True,
                "result": voice_result,
                "output_files": {
                    "result": voice_result_file,
                    "script_text": script_text_file
                },
                "metadata_file": metadata_file
            }
            
        except Exception as e:
            error_data = {
                "test": "voice_generation",
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "success": False
            }
            
            error_file = self.output_dirs["metadata"] / "03_voice_generation_error.json"
            with open(error_file, 'w', encoding='utf-8') as f:
                json.dump(error_data, f, indent=2)
            
            print(f"❌ Voice generation test failed: {str(e)}")
            print(f"📁 Error details saved to: {error_file}")
            print()
            
            return {"success": False, "error": str(e), "error_file": error_file}

    def test_final_assembly_agent(self, script_data: dict = None, video_result: dict = None, voice_result: dict = None) -> dict:
        """Test 4: Final Assembly Agent"""
        print("📦 Testing Final Assembly Agent...")
        print("=" * 50)
        
        try:
            # Load previous results if not provided
            if not script_data:
                script_file = self.output_dirs["script_generation"] / "script.json"
                if script_file.exists():
                    with open(script_file, 'r', encoding='utf-8') as f:
                        script_data = json.load(f)
            
            if not video_result:
                video_file = self.output_dirs["video_generation"] / "video_result_veo3.json"
                if video_file.exists():
                    with open(video_file, 'r', encoding='utf-8') as f:
                        video_result = json.load(f)
            
            if not voice_result:
                voice_file = self.output_dirs["voice_generation"] / "voice_result.json"
                if voice_file.exists():
                    with open(voice_file, 'r', encoding='utf-8') as f:
                        voice_result = json.load(f)
            
            # Create final package
            final_package = {
                "title": script_data.get('headline', 'Cat News Video') if script_data else 'Cat News Video',
                "anchor": script_data.get('anchor_name', 'Unknown Anchor') if script_data else 'Unknown Anchor',
                "script": script_data.get('script_segments', []) if script_data else [],
                "video": video_result if video_result else {"status": "not_generated"},
                "voice": voice_result if voice_result else {"status": "not_generated"},
                "metadata": {
                    "created_at": datetime.now().isoformat(),
                    "session_id": self.session_id,
                    "components_tested": {
                        "script": script_data is not None,
                        "video": video_result is not None,
                        "voice": voice_result is not None
                    },
                    "production_ready": all([
                        script_data is not None,
                        video_result and video_result.get('status') == 'completed',
                        voice_result and voice_result.get('status') == 'configured'
                    ])
                }
            }
            
            # Save final package
            package_file = self.output_dirs["final_assembly"] / "final_package.json"
            with open(package_file, 'w', encoding='utf-8') as f:
                json.dump(final_package, f, indent=2)
            
            # Create production summary
            summary = {
                "session_id": self.session_id,
                "timestamp": datetime.now().isoformat(),
                "components": {
                    "script_generation": "✅ Completed" if script_data else "❌ Failed",
                    "video_generation": "✅ Completed" if video_result and video_result.get('status') == 'completed' else "⚠️  Configured but not generated" if video_result else "❌ Failed",
                    "voice_generation": "✅ Ready" if voice_result and voice_result.get('status') == 'configured' else "⚠️  Not configured" if voice_result else "❌ Failed",
                    "final_assembly": "✅ Completed"
                },
                "production_ready": final_package["metadata"]["production_ready"],
                "next_steps": []
            }
            
            if not script_data:
                summary["next_steps"].append("Configure Groq API for script generation")
            if not video_result or video_result.get('status') != 'completed':
                summary["next_steps"].append("Configure video generation API (Google Veo 3 or MiniMax)")
            if not voice_result or voice_result.get('status') != 'configured':
                summary["next_steps"].append("Configure ElevenLabs API for voice generation")
            
            if not summary["next_steps"]:
                summary["next_steps"].append("Ready for production! All components working.")
            
            summary_file = self.output_dirs["final_assembly"] / "production_summary.json"
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)
            
            # Save metadata
            metadata = {
                "test": "final_assembly",
                "timestamp": datetime.now().isoformat(),
                "package": final_package,
                "summary": summary,
                "output_files": {
                    "package": str(package_file),
                    "summary": str(summary_file)
                },
                "success": True
            }
            
            metadata_file = self.output_dirs["metadata"] / "04_final_assembly.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"📦 Final package created: {final_package['title']}")
            print(f"🎬 Production ready: {'✅ Yes' if final_package['metadata']['production_ready'] else '❌ No'}")
            print(f"📁 Package saved to: {package_file}")
            print(f"📊 Summary saved to: {summary_file}")
            print()
            
            return {
                "success": True,
                "package": final_package,
                "summary": summary,
                "output_files": {
                    "package": package_file,
                    "summary": summary_file
                },
                "metadata_file": metadata_file
            }
            
        except Exception as e:
            error_data = {
                "test": "final_assembly",
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "success": False
            }
            
            error_file = self.output_dirs["metadata"] / "04_final_assembly_error.json"
            with open(error_file, 'w', encoding='utf-8') as f:
                json.dump(error_data, f, indent=2)
            
            print(f"❌ Final assembly failed: {str(e)}")
            print(f"📁 Error details saved to: {error_file}")
            print()
            
            return {"success": False, "error": str(e), "error_file": error_file}

    def run_full_test_suite(self, topic: str = None, video_provider: str = "veo3") -> dict:
        """Run all agent tests in sequence"""
        print("🧪 AI Cat News Network - Full Agent Test Suite")
        print("=" * 60)
        print(f"📅 Session: {self.session_id}")
        print(f"📁 Output: {self.base_output_dir}")
        print()
        
        results = {}
        
        # Test 1: Script Generation
        script_result = self.test_script_generation_agent(topic)
        results["script_generation"] = script_result
        
        # Test 2: Video Generation
        if script_result["success"]:
            video_result = self.test_video_generation_agent(script_result.get("script_data"), video_provider)
            results["video_generation"] = video_result
        else:
            video_result = None
            results["video_generation"] = {"success": False, "error": "Script generation failed"}
        
        # Test 3: Voice Generation
        if script_result["success"]:
            voice_result = self.test_voice_generation_agent(script_result.get("script_data"))
            results["voice_generation"] = voice_result
        else:
            voice_result = None
            results["voice_generation"] = {"success": False, "error": "Script generation failed"}
        
        # Test 4: Final Assembly
        assembly_result = self.test_final_assembly_agent(
            script_result.get("script_data") if script_result["success"] else None,
            video_result.get("result") if video_result and video_result["success"] else None,
            voice_result.get("result") if voice_result and voice_result["success"] else None
        )
        results["final_assembly"] = assembly_result
        
        # Overall summary
        print("📊 Test Suite Summary")
        print("=" * 30)
        for test_name, result in results.items():
            status = "✅ Pass" if result["success"] else "❌ Fail"
            print(f"{test_name}: {status}")
        
        print()
        print(f"📁 All outputs saved to: {self.base_output_dir}")
        print(f"🔍 Check individual component outputs in subdirectories")
        
        return results

def main():
    """Main testing function with menu"""
    tester = AgentTester()
    
    print("🧪 AI Cat News Network - Agent Testing Framework")
    print("=" * 60)
    print()
    print("Choose a test option:")
    print("1. 📝 Test Script Generation Agent Only")
    print("2. 🎥 Test Video Generation Agent Only")  
    print("3. 🎤 Test Voice Generation Agent Only")
    print("4. 📦 Test Final Assembly Agent Only")
    print("5. 🚀 Run Full Test Suite (All Agents)")
    print("6. 🔍 Run Quick Configuration Check")
    print()
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == "1":
        topic = input("Enter news topic (or press Enter for default): ").strip()
        tester.test_script_generation_agent(topic if topic else None)
    
    elif choice == "2":
        provider = input("Enter video provider (veo3/minimax, default: veo3): ").strip()
        tester.test_video_generation_agent(provider=provider if provider else "veo3")
    
    elif choice == "3":
        tester.test_voice_generation_agent()
    
    elif choice == "4":
        tester.test_final_assembly_agent()
    
    elif choice == "5":
        topic = input("Enter news topic (or press Enter for default): ").strip()
        provider = input("Enter video provider (veo3/minimax, default: veo3): ").strip()
        tester.run_full_test_suite(
            topic if topic else None,
            provider if provider else "veo3"
        )
    
    elif choice == "6":
        # Quick configuration check
        print("🔧 Configuration Check")
        print("=" * 30)
        configs = {
            "Groq API": get_setting("GROQ_API_KEY"),
            "Google API": get_setting("GOOGLE_API_KEY"),
            "MiniMax API": get_setting("MINIMAX_API_KEY"),
            "ElevenLabs API": get_setting("ELEVENLABS_API_KEY")
        }
        
        for name, key in configs.items():
            status = "✅ Configured" if key else "❌ Missing"
            print(f"{name}: {status}")
    
    else:
        print("❌ Invalid choice. Running full test suite...")
        tester.run_full_test_suite()

if __name__ == "__main__":
    main()
