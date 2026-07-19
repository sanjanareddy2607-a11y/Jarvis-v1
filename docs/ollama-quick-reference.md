# Ollama Quick Reference

## Available Models

### Mistral (7B)

- Speed: Fast ⚡
- Quality: Good 🧠
- Use: General questions

### Neural Chat (7B)

- Speed: Fast ⚡
- Quality: Good 🧠
- Use: Coding problems

### Llama 2 (7B)

- Speed: Medium ⚡⚡
- Quality: Excellent 🧠🧠
- Use: Complex reasoning

## Common Commands

### List all models

### Run a model interactively

### Pull a new model

### API Request Example
```bash
curl http://localhost:11434/api/generate \
  -d '{"model":"mistral","prompt":"Your question","stream":false}'
```

### Check Ollama Status
```bash
curl http://localhost:11434/api/tags
```

## Performance Tips
- Close other apps to free up RAM
- GPU acceleration works with NVIDIA drivers
- First query is slower (model loads), subsequent queries are faster
- Maximum context: ~3000 tokens per query

