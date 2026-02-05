"""
Hugging Face Models via OpenRouter - Using .env Configuration
"""

import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def query_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    """
    Query Hugging Face models through OpenRouter using API key from .env
    """
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key or api_key.startswith("sk-or-v1-YOUR"):
        print("❌ Error: Set OPENROUTER_API_KEY in .env file")
        print("   Sign up at: https://openrouter.ai")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com",
        "X-Title": "HF-API-Test",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        else:
            return f"Error {response.status_code}: {response.text[:200]}"
    except Exception as e:
        return f"Exception: {str(e)}"


def query_together_ai(prompt):
    """
    Query using Together AI with API key from .env
    """
    
    api_key = os.getenv("TOGETHER_API_KEY")
    
    if not api_key or api_key.startswith("YOUR"):
        print("❌ Error: Set TOGETHER_API_KEY in .env file")
        print("   Sign up at: https://www.together.ai")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7,
    }
    
    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        else:
            return f"Error {response.status_code}: {response.text[:200]}"
    except Exception as e:
        return f"Exception: {str(e)}"


def query_groq_api(prompt):
    """
    Query using Groq API with key from .env (EXTREMELY FAST)
    """
    
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key.startswith("YOUR"):
        print("❌ Error: Set GROQ_API_KEY in .env file")
        print("   Sign up at: https://console.groq.com")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7,
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        else:
            return f"Error {response.status_code}: {response.text[:200]}"
    except Exception as e:
        return f"Exception: {str(e)}"


def main():
    print("=" * 70)
    print("Hugging Face Models via API Providers (.env Configuration)")
    print("=" * 70)
    
    print("\n📋 Checking .env configuration...\n")
    
    hf_key = os.getenv("HF_API_KEY")
    or_key = os.getenv("OPENROUTER_API_KEY")
    together_key = os.getenv("TOGETHER_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    print(f"✓ HF_API_KEY: {hf_key[:20]}..." if hf_key and not hf_key.startswith("hf_hispn") else "✗ HF_API_KEY: Not set or demo key")
    print(f"✓ OPENROUTER_API_KEY: {or_key[:15]}..." if or_key and not or_key.startswith("sk-or-v1-YOUR") else "✗ OPENROUTER_API_KEY: Not configured")
    print(f"✓ TOGETHER_API_KEY: Configured" if together_key and not together_key.startswith("YOUR") else "✗ TOGETHER_API_KEY: Not configured")
    print(f"✓ GROQ_API_KEY: Configured" if groq_key and not groq_key.startswith("YOUR") else "✗ GROQ_API_KEY: Not configured")
    
    print("\n" + "=" * 70)
    print("QUICK START")
    print("=" * 70)
    
    print("""
1. Edit .env file and add your API keys:
   - OpenRouter: https://openrouter.ai/keys
   - Together AI: https://www.together.ai/settings/profile/api-keys
   - Groq: https://console.groq.com

2. Update .env with your keys

3. Run examples:
   python openrouter_example.py
   python together_example.py
   python groq_example.py
""")


if __name__ == "__main__":
    main()
