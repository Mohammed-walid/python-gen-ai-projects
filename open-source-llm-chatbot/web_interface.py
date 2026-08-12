"""a web interface for my chatbot"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import ChatBot
class WebInterface:
    def __init__(self):
        self.app = Flask(__name__, template_folder=".", static_folder="static")
        CORS(self.app)
        self.bot=ChatBot()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def home():
            return render_template('index.html')

        @self.app.route('/chatbot', methods=['POST'])
        def handle_prompt():
            data = request.get_json()
            input_text = data.get("prompt", "")

            if not input_text:
                return jsonify({"error": True, "response": "Empty prompt received."}), 400
            bot_reply = self.bot.generate_reply(input_text)

            return jsonify({
                "error": False,
                "response": bot_reply
            })

    def start(self):
        self.app.run(host="0.0.0.0", port=5000)
