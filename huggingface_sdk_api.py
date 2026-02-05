"""
Hugging Face Inference API using official SDK
"""

from huggingface_hub import InferenceClient

def main():
    # Initialize the client with your API token
    HF_API_TOKEN = "hf_YOUR_API_TOKEN_HERE"  # Get from .env
    client = InferenceClient(api_key=HF_API_TOKEN)
    
    # Example 1: Text generation
    print("=" * 60)
    print("Example 1: Text Generation with Mistral")
    print("=" * 60)
    try:
        output = client.text_generation(
            "What is Docker? Explain in one sentence.",
            model="mistralai/Mistral-7B-Instruct-v0.1",
            max_new_tokens=100
        )
        print(f"Response: {output}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Another text generation
    print("\n" + "=" * 60)
    print("Example 2: Code Explanation")
    print("=" * 60)
    try:
        output = client.text_generation(
            "Explain this Python code: for i in range(10): print(i)",
            model="mistralai/Mistral-7B-Instruct-v0.1",
            max_new_tokens=100
        )
        print(f"Response: {output}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Summarization
    print("\n" + "=" * 60)
    print("Example 3: Summarization")
    print("=" * 60)
    try:
        text = """
        Docker is a containerization platform that allows developers to package 
        applications and their dependencies into isolated containers. 
        This ensures consistency across development, testing, and production environments.
        """
        output = client.summarization(
            text,
            model="facebook/bart-large-cnn"
        )
        print(f"Summary: {output}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
