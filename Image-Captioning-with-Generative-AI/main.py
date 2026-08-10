"""This is the runner module"""
from image_captioner import ImageCaptioner

if __name__ == "__main__":
    captioner = ImageCaptioner()
    caption_one = captioner.caption("countryFlags.png","This image contains: ")
    print(caption_one)