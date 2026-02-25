#Create a text-to-image generation pipeline using a pre-trained model like DALL-E. 

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize client with token from .env
client = InferenceClient(token=HF_TOKEN)

prompt = (
    "Generate Van Gogh's Starry Night in the style of a modern digital painting, with vibrant colors and dynamic brushstrokes."
)

# Generate image
image = client.text_to_image(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-schnell"
)

# Save image
image.save("generated_artwork.png")
print("✅ Image generated and saved as generated_artwork.png")