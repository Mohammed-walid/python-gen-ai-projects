"""This module is used to download the audio file"""
import requests

class AudioDownloader:
    def __init__(self):
        self.url = ""

    def download_file(self, url):
        self.url = url
        response = requests.get(self.url)
        file_path = "downloaded_audio.mp3"

        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
                print("Audio file downloaded successfully")
        else:
            print("Downloading Failed")
