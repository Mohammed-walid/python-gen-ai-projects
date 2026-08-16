"""Gradio interface module"""
import gradio as gr
from speech_to_text import SpeechToText
from audio_downloader import AudioDownloader
class Interface:
    def __init__(self, url):
        print("Downloading audio")
        audio = AudioDownloader()
        audio.download_file(url)

        self.transcriber = SpeechToText()
        self.audio_input = gr.Audio(sources = "upload", type = "filepath")
        self.output_text = gr.Textbox()  # Text output

        self.iface = gr.Interface(fn = self.transcriber.transcribe,
                             inputs = self.audio_input, outputs = self.output_text,
                             title = "Audio Transcription App",
                             description = "Upload the audio file")

    def start_app(self):
        self.iface.launch(server_name="127.0.0.1", server_port=7860)