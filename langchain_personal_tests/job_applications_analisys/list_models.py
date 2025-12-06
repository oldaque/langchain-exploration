import os
from dotenv import load_dotenv
from google.ai import generativelanguage as glm

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("GOOGLE_API_KEY not found in environment.")
    exit(1)

print("Listing available models...")
try:
    # Create a client for the GenerativeService
    client = glm.ModelServiceClient(
        client_options={'api_key': api_key}
    )

    # List models
    for model in client.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(model.name)
except Exception as e:
    print(f"Error listing models: {e}")
