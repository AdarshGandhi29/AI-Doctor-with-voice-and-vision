import sys
sys.dont_write_bytecode = True

import os
import base64
import shutil
from groq import Groq  # type: ignore

# Prevent Python from generating .pyc files
sys.dont_write_bytecode = True

# Load API Key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def encode_image(image_path):
    """Convert an image to Base64 encoding."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image_with_query(query, model, encoded_image):
    """Send an image and query to the AI model for analysis."""
    client = Groq(api_key=GROQ_API_KEY)
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]
    
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    # Define parameters
    query = "Can you analyze my face and tell me if I have acne or any skin condition? Provide advice if needed."
    model="meta-llama/llama-4-scout-17b-16e-instruct"
    image_path = "C:/AI-Doctor-with-voice-and-vision/acne.jpg"
    
    # Encode Image & Run Analysis
    encoded_image = encode_image(image_path)
    response = analyze_image_with_query(query, model, encoded_image)
    
    # Print AI Response
    print(response)
    
    # Cleanup __pycache__ folder if exists
    shutil.rmtree("__pycache__", ignore_errors=True)