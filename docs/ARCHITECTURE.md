# Jarvis System Architecture

## System Overview

┌─────────────────────────────────────────────────┐
│              USER INTERFACE LAYER               │
│  • Open WebUI (Chat)    • n8n (Workflows)       │
└──────────────┬──────────────────┬───────────────┘
│                  │
└──────┬───────────┘
│
┌─────────────▼────────────────┐
│  ORCHESTRATION LAYER (n8n)   │
│  • Webhook triggers          │
│  • Workflow logic            │
│  • API calls                 │
└─────────────┬────────────────┘
│
┌─────────────┴────────────────┐
│                              │
┌───▼──────┐             ┌────────▼────┐
│  OLLAMA   │             │   FLASK     │
│  (LLM)    │             │   (API)     │
│ • Mistral │             │ • Tools     │
│ • Llama2  │             │ • Files     │
│ • Neural  │             │ • Data      │
└───┬──────┘             └────────┬────┘
│                             │
└─────────────┬───────────────┘
│
┌─────────────▼────────────────┐
│     STORAGE & PROCESSING     │
│ • PDFs  • CSV  • Text Files  │
│ • Python Tools  • Data Cache │
└──────────────────────────────┘

## Component Details

### 1. Ollama (Local LLM)
- **Role:** AI inference engine
- **Models:** 3x 7B parameter models
- **Port:** 11434
- **GPU:** NVIDIA CUDA optimized
- **Response Time:** 2-10 seconds

### 2. Open WebUI
- **Role:** User-facing chat interface
- **Port:** 3000
- **Features:** Chat, history, multi-model
- **Container:** Docker

### 3. n8n (Workflow Engine)
- **Role:** Automation & orchestration
- **Port:** 5678
- **Features:** Visual workflows, webhooks, integrations
- **Container:** Docker

### 4. Flask API Server
- **Role:** Custom Python tools exposure
- **Port:** 5000
- **Endpoints:** 6+ REST APIs
- **Runtime:** Python 3.11

### 5. Python Tools
- `file_reader.py`: Read TXT files
- `pdf_extractor.py`: Extract PDF text
- `csv_analyzer.py`: Analyze CSV data
- `file_lister.py`: Directory structure
- `resume_analyzer.py`: Resume analysis

## Data Flow Examples

### Example 1: Simple Chat

User Input (Open WebUI)
↓
Ollama processes query
↓
Response returned
↓
User sees answer

### Example 2: Document Analysis (via Flask)

User uploads PDF
↓
n8n webhook receives it
↓
Calls Flask /api/extract_pdf
↓
Flask extracts text
↓
Sends to Ollama for analysis
↓
Results returned to user

## Performance Characteristics

| Operation | Time | Resource |
|-----------|------|----------|
| Model load | 3-5s | GPU 4GB |
| First query | 5-10s | GPU + CPU |
| Subsequent query | 2-5s | GPU |
| PDF extraction | 1-3s | CPU |
| CSV analysis | <1s | CPU |

## Security Model

- ✅ **Local Only:** No internet required
- ✅ **Private:** No data leaves your machine
- ✅ **Isolated:** Docker containers for safety
- ✅ **No Auth:** Local access only
- ⚠️ **Not Production:** Use firewall for network access

## Scaling Considerations

### For Better Performance
- Upgrade to 16GB RAM
- Use RTX 3060+ GPU (8GB+)
- Use SSD for OS (faster model loading)

### For More Features
- Add database (SQLite/PostgreSQL)
- Implement caching layer
- Add authentication
- Use production WSGI server (Gunicorn)

## Technology Decisions

**Why Ollama?**
- Simplest local LLM deployment
- Good model selection
- GPU optimization out-of-box

**Why n8n?**
- Visual workflow builder
- No coding required for automation
- Good Docker support

**Why Flask?**
- Lightweight & simple
- Perfect for prototype/MVP
- Easy to extend

## Future Architecture

Current: Single-machine local system
Future:  Multi-user cloud system
┌─ Web UI (React)
├─ API Gateway
├─ Load Balancer
├─ Multiple Ollama instances
├─ Database (PostgreSQL)
└─ Cache Layer (Redis)

