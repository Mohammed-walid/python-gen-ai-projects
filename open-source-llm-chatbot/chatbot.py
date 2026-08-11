"""This module is used for implementing the chatbot logic"""
from transformers import AutoTokenizer, AutoModelForCausalLM

class ChatBot:
    def __init__(self):
        print("Loading the model...")
        self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
        self.conversation_history = []
        print("Chatbot is ready!")

