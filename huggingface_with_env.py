"""
Hugging Face API with .env Configuration
"""

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("HF_API_KEY not found in .env file")

print(f"✓ Loaded HF_API_KEY: {HF_API_KEY[:20]}...")

# Initialize client with API key from .env
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_API_KEY
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain Docker in one sentence."}
]

print("\n" + "="*70)
print("Hugging Face API - Chat Completion Example")
print("="*70)

try:
    response = client.chat_completion(
        messages=messages,
        max_tokens=200,
        temperature=0.7
    )
    
    print(f"\nUser: Explain Docker in one sentence.")
    print(f"Assistant: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"Error: {e}")
    print("Note: Hugging Face free tier inference may be limited.")
    print("Try using OpenRouter, Together AI, or Groq instead.")
