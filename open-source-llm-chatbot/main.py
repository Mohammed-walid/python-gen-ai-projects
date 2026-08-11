"""This is the runner module for the chatbot"""
import warnings

from chatbot import ChatBot
from web_interface import WebInterface
if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    app = WebInterface()
    app.start()
