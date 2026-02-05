"""
Hugging Face Inference API Example (Updated with new router endpoint)
Requires: pip install requests
"""

import requests
import json

def query_huggingface_router(prompt, model="gpt2", api_token=None):
    """
    Query Hugging Face using new router endpoint
    
    Args:
        prompt (str): The input text/prompt
        model (str): Model ID from Hugging Face Hub
        api_token (str): Your HuggingFace API token
    
    Returns:
        dict: Response from the API
    """
    
    if not api_token:
        raise ValueError("Please provide your HuggingFace API token")
    
    API_URL = f"https://router.huggingface.co/models/{model}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    payload = {"inputs": prompt}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Set your API token here or use environment variable
    HF_API_TOKEN = "hf_YOUR_API_TOKEN_HERE"  # Replace with your actual token from .env
    
    # Example 1: Text generation with Mistral
    print("=" * 50)
    print("Example 1: Text Generation (Mistral)")
    print("=" * 50)
    prompt = "What is Docker? Explain in one sentence."
    result = query_huggingface_router(prompt, model="mistralai/Mistral-7B-Instruct-v0.1", api_token=HF_API_TOKEN)
    if result:
        print(json.dumps(result, indent=2))
    
    # Example 2: Another prompt
    print("\n" + "=" * 50)
    print("Example 2: Code Explanation")
    print("=" * 50)
    prompt = "What does this Python code do? print('Hello World')"
    result = query_huggingface_router(prompt, model="mistralai/Mistral-7B-Instruct-v0.1", api_token=HF_API_TOKEN)
    if result:
        print(json.dumps(result, indent=2))
