"""This is the runner module for the chatbot"""
import warnings

from chatbot import ChatBot

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    chat_bot = ChatBot()
    chat_bot.chat()