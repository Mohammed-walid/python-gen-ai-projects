"""This is the main module  and will be used to run the program"""
from interface import Interface

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"
app = Interface(url)
app.start_app()
