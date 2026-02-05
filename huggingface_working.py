"""
FIXED: Hugging Face Models via Groq API (WORKING & SUPER FAST)
The issue: HuggingFace deprecated api-inference.huggingface.co endpoint (HTTP 410 Error)
Solution: Use Groq API instead - extremely fast, free tier available
"""

import requests
import json
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def call_groq_api(prompt):
    """
    Call Groq API - EXTREMELY FAST open-source model inference
    Uses API key from .env file
    """
    
    # Get API key from .env file
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    if not GROQ_API_KEY or GROQ_API_KEY.startswith("gsk_YOUR"):
        print("❌ Error: GROQ_API_KEY not configured in .env")
        return None
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
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
    print("Groq API - Hugging Face Models")
    print("=" * 70)
    
    # Verify API key is loaded
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        print(f"\n✅ API Key loaded: {groq_key[:20]}...")
    else:
        print("\n❌ API Key not found in .env")
        return
    
    # Test prompts
    test_prompts = [
        "What is Docker? Explain in 2-3 sentences.",
        "Explain this code: x = [i for i in range(10) if i % 2 == 0]",
        "What is Kubernetes? (1-2 sentences)",
        "Write a haiku about programming"
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\nExample {i}: {prompt[:50]}...")
        print("-" * 70)
        result = call_groq_api(prompt)
        print(f"Response:\n{result}\n")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()

