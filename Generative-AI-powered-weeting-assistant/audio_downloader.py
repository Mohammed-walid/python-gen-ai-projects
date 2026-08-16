"""This module is used to download the audio file"""
import requests

class AudioDownloader:
    def __init__(self):
        self.url = ""
        self.file_path = "downloaded_audio.mp3"
    def download_file(self, url):
        self.url = url
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(self.file_path, "wb") as file:
                file.write(response.content)
                print("Audio file downloaded successfully")
        else:
            print("Downloading Failed")

    def get_audio_name(self):
        return self.file_path
