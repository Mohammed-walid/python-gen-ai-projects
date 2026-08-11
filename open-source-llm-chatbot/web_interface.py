"""a web interface for my chatbot"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import ChatBot
class WebInterface:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/chatbot', methods=['POST'])
        def handle_prompt():
            data = request.get_json()
            input_text = data.get("prompt", "")

    def start(self):
        self.app.run()