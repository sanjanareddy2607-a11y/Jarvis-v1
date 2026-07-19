# 🤖 JARVIS — Personal AI Operating System

### *A Fully Local, Private, Open-Source AI Assistant*

**Built with Passion | Powered by Ollama | Automated by n8n | Crafted with Python**

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green?style=for-the-badge&logo=openai)](https://ollama.ai)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)](https://docker.com)
[![Flask](https://img.shields.io/badge/Flask-REST%20API-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ✨ What is JARVIS?

> **The AI Assistant You Control. The AI Assistant That Respects Your Privacy.**

JARVIS is a **revolutionary local-first AI system** that brings the power of ChatGPT to your laptop—**without the internet, without the servers, without giving away your data.**

Imagine having:
- 🧠 **A personal AI brain** that thinks at GPU speed
- 🔒 **100% privacy** (no data ever leaves your machine)
- 💰 **Zero cost** (no subscriptions, no API bills)
- 🚀 **Blazing fast** (responses in 2-10 seconds)
- 🛠️ **Completely yours** (run it anywhere, anytime)

**This isn't theoretical. It's real. It's working. You built it.** ✅

---

## 🎯 Why JARVIS Matters

| Feature | ChatGPT | JARVIS |
|---------|---------|--------|
| **Internet Required** | ✅ Always | ❌ Never |
| **Data Privacy** | ☁️ Cloud | 🏠 Local |
| **Monthly Cost** | 💵 $20+ | 💰 Free |
| **Works Offline** | ❌ No | ✅ Yes |
| **Own Your Data** | ❌ No | ✅ Yes |
| **Customizable** | ❌ Limited | ✅ Full |
| **Open Source** | ❌ No | ✅ Yes |
| **Run Anywhere** | ❌ Web only | ✅ Desktop |

**JARVIS wins on every metric that matters.** 🏆

---

## 🚀 Quick Start (30 Seconds!)

### **Fastest Way to Chat with JARVIS**

```bash
# 1. Navigate to project
cd C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis

# 2. Activate AI brain
venv\Scripts\activate

# 3. Open your ChatGPT-like interface
# Go to browser: http://localhost:3000

# 4. START CHATTING! 🤖
```

**That's it. You now have a private AI assistant running locally on your machine.**

---

## 💫 Features That Make JARVIS Powerful

### 🧠 **Three AI Brains (3x 7B Models)**

- **Mistral 7B** → Fast & Accurate (Default choice)
- **Llama2 7B** → Best for Deep Reasoning
- **Neural Chat 7B** → Expert at Coding Help

Switch between them anytime. Choose based on your need.

### 💬 **ChatGPT-Quality Interface**

- Beautiful, responsive design
- Conversation history
- Dark/light mode
- Multi-model support
- One-click model switching

### 🔧 **Smart Python Tools**

- **PDF Reader** → Extract text from research papers
- **CSV Analyzer** → Analyze data instantly
- **File Lister** → Explore project structures
- **Resume Analyzer** → Career-focused intelligence
- **Job Matcher** → Match jobs to your skills

### 🤖 **Workflow Automation** (n8n)

- Visual automation builder
- No coding required
- Connect anything to anything
- Webhook triggers
- Scheduled tasks

### 🔗 **REST API Server**
/api/health              → Check system status
/api/read_file           → Read any text file
/api/extract_pdf         → Extract PDF text
/api/analyze_csv         → Analyze CSV data
/api/list_directory      → List folder structure
/api/match_job_resume    → Match jobs to resume

### 🛡️ **Maximum Privacy & Control**

- ✅ No internet required
- ✅ No data collection
- ✅ No tracking
- ✅ No cookies
- ✅ Run offline forever

---

## 🏗️ System Architecture
YOU (User)
↓
OPEN WEBUI (Chat Interface - localhost:3000)
↓
OLLAMA (AI Brain - localhost:11434)
├─→ Mistral 7B
├─→ Llama2 7B
└─→ Neural Chat 7B
↓
N8N (Workflows - localhost:5678)
├─→ FLASK API (Python Tools - localhost:5000)
└─→ File Processing & Data Analysis
↓
RESPONSES (Back to You)

---

## 🔧 Tech Stack

- **AI/LLM:** Ollama (Local LLM Inference)
- **Models:** Mistral 7B, Llama2 7B, Neural Chat 7B
- **Interface:** Open WebUI (ChatGPT-like UX)
- **Automation:** n8n (No-code Workflows)
- **API:** Flask (Python REST Server)
- **Tools:** PDF Extraction, CSV Analysis, File Processing
- **Deployment:** Docker (Containerized)
- **GPU:** NVIDIA CUDA optimized
- **Language:** Python 3.11+
- **Version Control:** Git

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model Load Time** | 3-5 seconds |
| **First Response** | 5-10 seconds |
| **Follow-up Response** | 2-5 seconds |
| **PDF Processing** | <3 seconds |
| **CSV Analysis** | <1 second |
| **GPU Usage** | 4-6GB VRAM |
| **RAM Usage** | 6-7GB total |

**Tested on:** GTX 1650 + Ryzen 5000 + 8GB RAM

---

## 💻 Hardware Requirements

### ✅ Minimum (Tested & Working)

- **CPU:** AMD Ryzen 5000 Series or equivalent
- **GPU:** NVIDIA GTX 1650 (4GB VRAM)
- **RAM:** 8GB
- **Storage:** 50GB+ for models
- **OS:** Windows 10/11

### ⭐ Recommended

- **CPU:** Ryzen 7 / i7 or better
- **GPU:** RTX 3060+ (8GB+ VRAM)
- **RAM:** 16GB+
- **Storage:** 100GB+ (SSD recommended)

---

## 🚀 Installation Guide

### Step 1: Prerequisites

- Python 3.9+
- Git installed
- Docker Desktop
- 50GB+ disk space

### Step 2: Download Ollama

https://ollama.ai

### Step 3: Setup Python Environment

```bash
cd jarvis
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 4: Start Services

**Terminal 1 - Flask API:**
```bash
cd python-tools
python main.py
```

**Terminal 2 - Docker:**
```bash
docker start open-webui n8n
```

### Step 5: Access Jarvis

- **Chat:** http://localhost:3000
- **Workflows:** http://localhost:5678
- **API:** http://localhost:5000/api/health

---

## 📚 Usage Examples

### Example 1: Simple Chat
YOU: "Explain quantum computing"
JARVIS: "Quantum computers use quantum bits (qubits)..."

### Example 2: Code Help
YOU: "Write Python code to check if a string is a palindrome"
JARVIS: "
def is_palindrome(s):
s = s.lower().replace(' ', '')
return s == s[::-1]
"

### Example 3: Document Analysis
YOU: "Summarize this research paper"
JARVIS: [Extracts PDF] → [Analyzes] → [Returns summary]

---

## 🎓 What You'll Learn

- ✅ AI/ML & Local LLM deployment
- ✅ REST API design with Flask
- ✅ Docker containerization
- ✅ n8n workflow automation
- ✅ Python advanced features
- ✅ System architecture & design
- ✅ GPU programming (CUDA)
- ✅ Git & version control

---

## 📁 Project Structure
jarvis/
├── python-tools/           # Python scripts & Flask API
│   ├── main.py             # Flask server
│   ├── file_reader.py      # Text file reading
│   ├── pdf_extractor.py    # PDF extraction
│   ├── csv_analyzer.py     # CSV analysis
│   ├── file_lister.py      # Directory listing
│   └── requirements.txt     # Dependencies
├── workflows/              # n8n workflow backups
├── config/                 # Configuration files
├── data/                   # Sample data & uploads
├── docs/                   # Documentation
├── README.md               # This file
├── LICENSE                 # MIT License
├── .env                    # Environment variables
└── .gitignore              # Git ignore rules

---

## 🔐 Privacy & Security

**Your data is YOURS.**
ChatGPT:    Your Messages → OpenAI Servers
JARVIS:     Your Messages → Your GPU → Your Laptop (Stays Local)
No telemetry
No tracking
No data collection
No internet needed
100% offline capable

---

## 🚀 Next Steps

1. ✅ Start using JARVIS daily
2. ✅ Try different models
3. ✅ Explore n8n workflows
4. ✅ Share on GitHub
5. ✅ Build on top of it

---

## 🤝 Contributing

This is a personal portfolio project. Feel free to fork and build upon it!

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

## 👨‍💻 About the Builder

**Sanjana Reddy** - CS Student specializing in AI & ML

- 🎓 Building AI systems from scratch
- 💻 Full-stack developer
- 🚀 Open source enthusiast
- 🌍 Passionate about local AI

---

## ⭐ Show Your Support

If JARVIS helped you:

- ⭐ Star this repository
- 🔁 Share with others
- 💬 Leave feedback
- 🐛 Report bugs
- 💡 Suggest features

---

<div align="center">

### **Built with ❤️ • Powered by Ollama • Automated by n8n**

### **Your Personal AI Operating System**

</div>
