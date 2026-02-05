"""
Hugging Face Models via OpenRouter API
OpenRouter provides stable access to many open-source models
Requires OpenRouter API key (free tier available)
"""

import requests
import json

def query_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    """
    Query Hugging Face models through OpenRouter
    Sign up free at: https://openrouter.ai
    """
    
    # You'll need to get your own OpenRouter API key
    OPENROUTER_API_KEY = "sk-or-v1-YOUR_OPENROUTER_KEY"  # Get from https://openrouter.ai
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
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
    Query using Together AI (another Hugging Face model provider)
    Sign up free at: https://www.together.ai
    """
    
    TOGETHER_API_KEY = "YOUR_TOGETHER_AI_KEY"  # Get from https://www.together.ai
    
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
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
    Query using Groq API (very fast inference)
    Sign up free at: https://console.groq.com
    """
    
    GROQ_API_KEY = "YOUR_GROQ_API_KEY"  # Get from https://console.groq.com
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
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
    print("Open-Source LLM APIs (Hugging Face Models)")
    print("=" * 70)
    
    print("\n📝 AVAILABLE OPTIONS:\n")
    
    print("1. OpenRouter")
    print("   - URL: https://openrouter.ai")
    print("   - Free tier: Yes")
    print("   - Models: 100+ open-source models")
    print("   - Speed: Good")
    
    print("\n2. Together AI")
    print("   - URL: https://www.together.ai")
    print("   - Free tier: Yes (free credits)")
    print("   - Models: 100+ open-source models")
    print("   - Speed: Very good")
    
    print("\n3. Groq API")
    print("   - URL: https://console.groq.com")
    print("   - Free tier: Yes")
    print("   - Models: Limited but very fast")
    print("   - Speed: EXTREMELY FAST (50-80 tokens/sec)")
    
    print("\n4. Local Ollama (Already configured)")
    print("   - Local only, free")
    print("   - No internet needed")
    print("   - Slower than cloud APIs")
    
    print("\n" + "=" * 70)
    print("SETUP INSTRUCTIONS:")
    print("=" * 70)
    
    print("\nFor OpenRouter:")
    print("1. Sign up at https://openrouter.ai")
    print("2. Get your API key from https://openrouter.ai/keys")
    print("3. Replace 'sk-or-v1-YOUR_OPENROUTER_KEY' in the script")
    print("4. Run: python hf_direct.py")
    
    print("\nFor Together AI:")
    print("1. Sign up at https://www.together.ai")
    print("2. Get API key from https://www.together.ai/settings/profile/api-keys")
    print("3. Replace 'YOUR_TOGETHER_AI_KEY' in the script")
    
    print("\nFor Groq:")
    print("1. Sign up at https://console.groq.com")
    print("2. Get API key from settings")
    print("3. Replace 'YOUR_GROQ_API_KEY' in the script")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
