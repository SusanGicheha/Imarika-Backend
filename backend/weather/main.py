import os
import googletrans
import gtts
import requests

from googletrans import Translator
from geopy.geocoders import Nominatim
from gtts import gTTS

# import classes from the classes.py script
from classes import Location
from classes import Weather
from classes import TranslateText
from classes import TextToSpeech


# call classes to give desired output
address = input("Enter your location ")
location = Location(address)
weather = Weather(location)
weather_details = weather.get_weather_details()
translated_text = TranslateText(weather_details)
translated_weather = translated_text.translate_text()
print(translated_weather)


# tts = TextToSpeech(translated_weather)
# tts.speak_text()

