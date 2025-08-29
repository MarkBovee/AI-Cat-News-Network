# 🧪 Agent Testing Framework

This directory contains modular testing tools for the AI Cat News Network that test each component independently with separate output folders.

## 🎯 **Testing Philosophy**

**Each agent/component outputs to its own folder** so you can:
- ✅ **Inspect individual outputs** before moving to next step
- ✅ **Debug specific components** without running full workflow  
- ✅ **Mix and match results** from different test runs
- ✅ **Verify each step** works correctly

## 📁 **Output Structure**

```
test_outputs/                     # All test outputs
├── 00_metadata/                  # Test metadata and logs
├── 01_script_generation/         # Script generation outputs
├── 02_video_generation/          # Video generation outputs  
├── 03_voice_generation/          # Voice generation outputs
└── 04_final_assembly/            # Final assembled packages

component_tests/                  # Individual component tests
├── script_generation/            # Script component outputs
├── video_generation/             # Video component outputs
├── voice_generation/             # Voice component outputs
└── integration/                  # Integration reports
```

## 🔧 **Testing Tools**

### 1. **Component Tester** (`test_components.py`)
**Quick individual component testing**

```bash
python scripts/test_components.py
```

**Menu Options:**
- 📝 Test Script Generation Component
- 🎥 Test Video Generation Component  
- 🎤 Test Voice Generation Component
- 🔗 Integration Check
- 🚀 Test All Components

**Outputs:** `component_tests/[component]/`

### 2. **Agent Framework** (`test_agent_framework.py`)
**Full workflow testing with detailed outputs**

```bash
python scripts/test_agent_framework.py
```

**Menu Options:**
- 📝 Test Script Generation Agent Only
- 🎥 Test Video Generation Agent Only
- 🎤 Test Voice Generation Agent Only
- 📦 Test Final Assembly Agent Only
- 🚀 Run Full Test Suite
- 🔍 Configuration Check

**Outputs:** `test_outputs/[session_id]/`

### 3. **Integration Test** (`test_integration.py`)
**System-wide integration verification**

```bash
python scripts/test_integration.py
```

**Tests:** All imports, providers, API configurations, mock generations

## 🚀 **Usage Workflow**

### **1. Start with Component Testing**
```bash
# Test individual components first
python scripts/test_components.py
# Choose option 5 (Test All Components)
```

**Check outputs in:** `component_tests/`

### **2. Run Integration Check**
```bash
python scripts/test_integration.py
```

**Verify:** All systems can import and initialize

### **3. Test Agent Framework**
```bash
python scripts/test_agent_framework.py
# Choose option 5 (Run Full Test Suite)
```

**Check outputs in:** `test_outputs/[timestamp]/`

### **4. Inspect Results**
Each test creates detailed JSON files with:
- ✅ **Test results and status**
- ✅ **API configuration checks**
- ✅ **Generated content**
- ✅ **Error details if any**
- ✅ **Next steps recommendations**

## 📊 **Example Test Session**

```bash
# 1. Test components individually
python scripts/test_components.py
# Output: component_tests/script_generation/script_data_143055.json

# 2. Check what was generated
cat component_tests/script_generation/script_data_143055.json

# 3. Run full agent test
python scripts/test_agent_framework.py
# Output: test_outputs/20250829_143100/

# 4. Check final assembly
cat test_outputs/20250829_143100/04_final_assembly/final_package.json
```

## 🔍 **Output File Examples**

### Script Generation Output
```json
{
  "topic": "Breaking: Local Cat Becomes Mayor",
  "timestamp": "2025-08-29T14:30:55",
  "raw_response": "Generated script content...",
  "word_count": 125,
  "character_count": 850
}
```

### Video Generation Output
```json
{
  "status": "completed",
  "provider": "veo3",
  "video_url": "generated_video.mp4",
  "video_path": "output/veo3_cat_news_1724958655.mp4",
  "prompt": "Professional cat anchor..."
}
```

### Final Assembly Output
```json
{
  "title": "Breaking: Local Cat Becomes Mayor",
  "anchor": "Whiskers Winston",
  "script": [...],
  "video": {...},
  "voice": {...},
  "metadata": {
    "production_ready": true,
    "components_tested": {
      "script": true,
      "video": true,
      "voice": true
    }
  }
}
```

## 🛠️ **Debugging Workflow**

**If a component fails:**

1. **Check component test first**
   ```bash
   python scripts/test_components.py
   # Test just the failing component
   ```

2. **Inspect the output files**
   ```bash
   # Check what was generated/what error occurred
   cat component_tests/[component]/[latest_file]
   ```

3. **Fix configuration**
   ```bash
   # Add missing API keys to .env
   # Verify with integration check
   python scripts/test_integration.py
   ```

4. **Re-test the workflow**
   ```bash
   python scripts/test_agent_framework.py
   ```

## 📋 **API Requirements by Component**

| Component | Required API | Free Option |
|-----------|-------------|-------------|
| **Script Generation** | `GROQ_API_KEY` | ✅ Free |
| **Video Generation** | `GOOGLE_API_KEY` or `MINIMAX_API_KEY` | ✅ Veo 3 Free Tier |
| **Voice Generation** | `ELEVENLABS_API_KEY` | ❌ Paid only |
| **Final Assembly** | Any of above | ✅ Can work with free APIs |

## 🎯 **Testing Strategy**

1. **Development**: Use component tests for quick iteration
2. **Integration**: Use agent framework for full workflow validation  
3. **Production**: Use integration test for deployment verification
4. **Debugging**: Use component tests to isolate issues

**Each test saves detailed outputs so you can trace exactly what happened at each step!**
