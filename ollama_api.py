"""
Ollama Local LLM API Example
Requires: docker pull ollama/ollama and ollama run mistral (or other models)
"""

import requests
import json

def query_ollama(prompt, model="mistral"):
    """
    Query local Ollama instance
    
    Args:
        prompt (str): The input text/prompt
        model (str): Model name installed in Ollama
    
    Returns:
        dict: Response from Ollama
    """
    
    OLLAMA_URL = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to Ollama. Make sure Ollama is running.")
        print("Start Ollama with: docker run -d -v ollama:/root/.ollama -p 11434:11434 ollama/ollama")
        print("Then run a model: docker exec <container> ollama run mistral")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def list_models():
    """List available models in Ollama"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("Ollama Local LLM API Examples")
    print("=" * 60)
    
    # Check available models
    print("\nChecking available models...")
    models_info = list_models()
    if models_info and "models" in models_info:
        print(f"Available models: {[m['name'] for m in models_info['models']]}")
    else:
        print("No models found or Ollama not running")
    
    # Example 1: Simple prompt
    print("\n" + "=" * 60)
    print("Example 1: What is Docker?")
    print("=" * 60)
    result = query_ollama("What is Docker? Explain in one sentence.", model="mistral")
    if result:
        print(f"Response:\n{result.get('response', 'No response')}")
    
    # Example 2: Code explanation
    print("\n" + "=" * 60)
    print("Example 2: Python Code Explanation")
    print("=" * 60)
    result = query_ollama(
        "Explain this Python code: x = [i for i in range(10) if i % 2 == 0]",
        model="mistral"
    )
    if result:
        print(f"Response:\n{result.get('response', 'No response')}")
    
    # Example 3: JSON response
    print("\n" + "=" * 60)
    print("Example 3: Full Response Object")
    print("=" * 60)
    result = query_ollama("What is Kubernetes?", model="mistral")
    if result:
        print(json.dumps(result, indent=2))
