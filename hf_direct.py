"""
Hugging Face Inference API - Simple Direct Calls
"""

import requests
import json

def call_huggingface_api(prompt):
    """
    Call Hugging Face inference API directly
    """
    HF_TOKEN = "hf_YOUR_API_TOKEN_HERE"  # Get from .env
    
    # Using Hugging Face's inference endpoint for a specific model
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 512,
            "temperature": 0.7,
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "No response")
            return str(result)
        else:
            return f"Error {response.status_code}: {response.text[:200]}"
    except Exception as e:
        return f"Exception: {str(e)}"


def main():
    print("=" * 70)
    print("Hugging Face Inference API - Direct Calls")
    print("=" * 70)
    
    prompts = [
        "What is Docker? Explain in 2-3 sentences.",
        "Explain this code: x = [i for i in range(10) if i % 2 == 0]",
        "What is Kubernetes? (1-2 sentences)",
        "Write a haiku about programming"
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\nExample {i}: {prompt[:50]}...")
        print("-" * 70)
        response = call_huggingface_api(prompt)
        print(f"Response:\n{response}")
        print()


if __name__ == "__main__":
    main()
