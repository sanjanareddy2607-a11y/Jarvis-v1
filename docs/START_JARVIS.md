# 🚀 How to Start & Use Jarvis AI System

## Starting Jarvis (Every Time)

### Method 1: Quick Start (Just Chat)

1. **Open Command Prompt/PowerShell**
2. Navigate to jarvis:
```bash
   cd C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis
   venv\Scripts\activate
```

3. **Open Jarvis in Browser:** 

http://localhost:3000

4. **Start Chatting!**
   - Type your question
   - Wait 3-10 seconds
   - Get AI response

### Method 2: Full Stack (With All Tools)

**Terminal 1: Start Flask API Server**
```bash
cd C:\Users\sanja\OneDrive\sthithapragn\PROJECT J\jarvis
venv\Scripts\activate
cd python-tools
python main.py
```

**Terminal 2: Start Docker Containers**
```bash
docker start open-webui n8n
```

**Then:**
- Chat: http://localhost:3000
- Workflows: http://localhost:5678
- API: http://localhost:5000/api/health

---

## What You Can Do With Jarvis

### 1. Ask Questions (Chat Mode)
- "Explain AI in simple terms"
- "Write Python code for..."
- "What are the latest trends in..."
- "Help me debug this error..."

### 2. Analyze Documents (With Tools)
- Upload a PDF → Jarvis extracts text
- Upload a CSV → Jarvis analyzes data
- Upload a research paper → Jarvis summarizes it

### 3. Automate Tasks (With n8n)
- Create workflows
- Automate repetitive tasks
- Chain multiple steps together

---

## Example Conversations

### Example 1: Simple Chat
You: "What is cryptocurrency?"
Jarvis: "Cryptocurrency is a digital currency that uses cryptography...
[5-10 seconds of thinking]
Full answer appears"

### Example 2: Code Help
You: "I have a Python error: 'NameError: name x is not defined'. Help!"
Jarvis: "This error means variable 'x' is used before being defined...
Here's how to fix it:

Define x first
Check indentation
..."

### Example 3: Complex Question
You: "Compare machine learning vs deep learning"
Jarvis: "Machine Learning is... Deep Learning is...
Here are the key differences..."

---

## Understanding Response Times

- **First question:** 5-10 seconds (model loading)
- **Next questions:** 2-5 seconds (model already loaded)
- **Complex questions:** 10-20 seconds (more thinking)

---

## Closing Jarvis

When done:

1. Close browser tab (localhost:3000)
2. In terminal, press: `Ctrl + C`
3. If Flask running: Press `Ctrl + C` again

Done! ✅

---

## Troubleshooting

**"Connection refused"?**
- Make sure venv is activated
- Make sure Ollama is running
- Check if port 3000 is not blocked

**"Out of memory"?**
- Close other apps
- Restart your computer
- Use smaller model (Mistral instead of Llama2)

**"Slow responses"?**
- First query is always slower
- Close browser tabs to free RAM
- Consider upgrading RAM to 16GB

---

## Your Models Compared

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| Mistral | ⚡⚡⚡⚡⚡ | 🧠🧠🧠 | Fast answers |
| Llama2 | ⚡⚡⚡⚡ | 🧠🧠🧠🧠 | Better quality |
| Neural Chat | ⚡⚡⚡⚡ | 🧠🧠🧠 | Coding help |

---

## What Makes Jarvis Special

✅ **Completely Private** - No internet, no tracking
✅ **Free** - No monthly subscriptions
✅ **Fast** - Runs on your GPU
✅ **Customizable** - You can add your own tools
✅ **Offline** - Works anywhere, anytime
✅ **Owned by You** - Not controlled by any company

---

## Next Steps

1. Use Jarvis daily to get comfortable with it
2. Try different models (change the dropdown in Open WebUI)
3. Ask different types of questions
4. Explore n8n workflows
5. Share on GitHub
6. Tell your friends!

---

Made with ❤️ by Sanjana