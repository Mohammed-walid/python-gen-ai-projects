"""This is the main module  and will be used to run the program"""


from audio_downloader import AudioDownloader
from speech_to_text import SpeechToText
audio = AudioDownloader()
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"
audio.download_file(url)
audio_name = audio.get_audio_name()
transcriber = SpeechToText()
transcriber.transcribe(audio_name)


