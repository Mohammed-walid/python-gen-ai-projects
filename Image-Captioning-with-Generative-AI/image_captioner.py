"""This module is used for image captioning"""
from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image

class ImageCaptioner:
    def __init__(self):
        """Construction method"""
        print("Loading the pre-trained model...")
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def caption(self, img_path, caption_text):
        """This method is used for loading the image and Generate the caption"""
        print("Loading the image...")
        image = Image.open(img_path).convert("RGB")
        inputs = self.processor(image, text = caption_text, return_tensors="pt")
        print("Generating captions...")
        output = self.model.generate(**inputs, max_length = 100)
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption
