"""This module is used for image captioning"""

from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading the pre-trained model...")
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
