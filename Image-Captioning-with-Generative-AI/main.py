"""This is the runner module"""
from gradio_interface import GradioInterface

if __name__ == "__main__":
   app = GradioInterface()
   app.launch_application()
