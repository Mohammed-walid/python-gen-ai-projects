"""This module is used to make a user interface
 for my Image Captioning Application """

import gradio as gr
from image_captioner import ImageCaptioner

class GradioInterface:
    def __init__(self):
        self.captioner = ImageCaptioner()

    def upload(self, image_path):
        """This is the fn function for the gradio interface"""
        text = ""

        caption = self.captioner.caption(image_path, text)
        return caption

    def launch_application(self):
        iface = gr.Interface(
            fn = self.upload,
            inputs = gr.Image(type = "filepath"),
            outputs = "text",
            title = "Image Captioning",
            description = "this is a web app for image captioning"
        )
        iface.launch()
