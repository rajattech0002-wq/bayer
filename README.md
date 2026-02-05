# Open Source LLM API Examples

Complete setup for testing and using open-source Large Language Models via various API providers.

## Features

- ✅ **Local LLM** - Ollama with Mistral 7B (free, no API key needed)
- ✅ **Groq API** - Ultra-fast inference with Llama 3.3
- ✅ **Hugging Face Models** - Access via multiple providers
- ✅ **Environment Variables** - Secure API key management
- ✅ **Docker** - Containerized LLM inference

## Quick Start

### 1. Local Ollama (Recommended for Privacy)
```bash
python ollama_api.py
```

### 2. Groq API (Fastest)
```bash
# 1. Sign up at https://console.groq.com
# 2. Get your API key
# 3. Add to .env:
#    GROQ_API_KEY=your_key_here
# 4. Run:
python huggingface_working.py
```

## File Structure

- `ollama_api.py` - Local LLM with Docker/Ollama
- `huggingface_working.py` - Groq API integration
- `hf_alternatives.py` - OpenRouter, Together AI, Groq setup guides
- `api_with_env.py` - Multi-provider example with .env
- `.env` - API keys (NOT committed to git)
- `.gitignore` - Protects sensitive files

## Setup

### Install Dependencies
```bash
pip install python-dotenv requests huggingface-hub
```

### Configure .env
```bash
# .env file
GROQ_API_KEY=gsk_YOUR_KEY
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY
TOGETHER_API_KEY=YOUR_KEY
HF_API_KEY=hf_YOUR_KEY
```

### Docker & Ollama
```bash
# Start Ollama container
docker run -d --name ollama -v ollama:/root/.ollama -p 11434:11434 ollama/ollama

# Pull a model
docker exec ollama ollama pull mistral

# Run local LLM
python ollama_api.py
```

## API Providers

| Provider | Speed | Cost | Models | Notes |
|----------|-------|------|--------|-------|
| **Groq** | ⚡⚡⚡ Fastest | Free | Llama, Qwen | Recommended |
| **Ollama Local** | Slower | Free | Any | No internet needed |
| **OpenRouter** | Good | Paid | 100+ | Many open-source |
| **Together AI** | Good | Paid | 100+ | Good for training |

## Examples

### Docker
```bash
docker --version
docker ps
```

### LLM Queries
```python
from huggingface_working import call_groq_api

response = call_groq_api("Explain Docker in 2 sentences")
print(response)
```

## Security Notes

⚠️ **NEVER commit `.env` file!**
- API keys are in `.gitignore`
- Use environment variables in production
- Rotate keys regularly if exposed

## Troubleshooting

**Error 410: Gone** - Hugging Face deprecated free inference API
**Error 400: Model decommissioned** - Update model name in script
**Error 401: Invalid API Key** - Check `.env` file configuration
**Connection refused** - Ollama container not running

## License

MIT - Open for educational and commercial use

## Author

Created for testing open-source LLM APIs and Docker containerization.
