# Quick Start Guide - Jarvis AI System

## Starting the System

### 1. Activate Virtual Environment
```bash
cd C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis
venv\Scripts\activate
```

### 2. Start Flask Server (Terminal 1)
```bash
cd python-tools
python main.py
```

You'll see:
🚀 Starting Jarvis Python Tools Server...
📍 Server running on http://localhost:5000

### 3. Start Docker Containers (Terminal 2)
```bash
docker start open-webui n8n
```

### 4. Access Interfaces

**Open WebUI (Chat):** http://localhost:3000
- Chat with Ollama models
- Ask questions
- Get instant responses

**n8n (Workflows):** http://localhost:5678
- Create automation workflows
- Connect tools together
- Visual workflow builder

**Flask API:** http://localhost:5000/api/health
- Test endpoints
- Call Python tools
- JSON responses

## 🧪 Quick Test

### Test Ollama
```bash
curl http://localhost:11434/api/tags
```

### Test Flask API
```bash
curl http://localhost:5000/api/health
```

### Test in Open WebUI
1. Go to http://localhost:3000
2. Ask: "What is AI?"
3. Should get response in 5-10 seconds

## 🛑 Stopping Services

### Stop Flask
In Terminal 1, press: `Ctrl + C`

### Stop Docker
```bash
docker stop open-webui n8n
```

### Stop Ollama
Open Windows Services, find "Ollama", right-click "Stop"

## ⚠️ Troubleshooting

**"Port already in use"**
- Change port in config or kill process using it

**"Out of memory"**
- Close other apps
- Use CPU mode: `set OLLAMA_GPU=off`

**"Slow responses"**
- First query is slower (model loading)
- Subsequent queries are faster
- Close other apps to free RAM

## 📚 More Info

See `README.md` for full documentation.