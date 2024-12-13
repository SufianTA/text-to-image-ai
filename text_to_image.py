# text-to-image-ai/text_to_image.py

from transformers import DALL_E
import torch

# Load DALL-E model
model = DALL_E.from_pretrained("openai/dall-e")

# Example text input
text = "A painting of a futuristic city."

# Generate image from text
image = model.generate(text)
print(image)
