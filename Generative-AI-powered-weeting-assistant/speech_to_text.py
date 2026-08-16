"""This module is used to transcribe audios"""
from transformers import pipeline
import torch

class SpeechToText:
    def __init__(self):
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model = "openai/whisper-tiny.en",
            chunk_length_s = 30,
        )

    def transcribe(self, audio_sample):
        audio = audio_sample
        transcription = self.pipe(audio, batch_size = 8)["text"]
        print(transcription)
