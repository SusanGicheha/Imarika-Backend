# import python modules

import os
import googletrans
import gtts
import requests
from googletrans import Translator
from geopy.geocoders import Nominatim
from gtts import gTTS


class Location:
    def __init__(self, address):
        self.address = address

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="Paschal")
        location = geolocator.geocode(self.address)
        if location:
            self.lat = str(location.latitude)
            self.long = str(location.longitude)
            return self.lat, self.long
        else:
            print("Not found")


class Weather:
    def __init__(self, location):
        self.location = location
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = "8ef9f127dcefc79f9cc837599ca96e97"
        self.coord = self.location.get_coordinates()
        self.lat = self.coord[0]
        self.long = self.coord[1]
        self.url = self.base_url + "lat=" + self.lat + "&lon=" + self.long + "&appid=" + self.api_key + "&units=" + "metric"
        self.res = requests.get(self.url)
        self.data = self.res.json()

    def get_weather_details(self):
        self.temperature = self.data['main']['temp']
        self.humidity = self.data['main']['humidity']
        self.description = self.data['weather'][0]['description']
        self.temp = (f"The temperature in {self.location.address} area is {self.temperature} degrees")
        self.humid = (f'The humidity in {self.location.address} area is {self.humidity}%')
        self.descr = (f'There are {self.description} in {self.location.address} area')
        self.weather = [self.temp, self.humid, self.descr]
        return self.weather


class TranslateText:
    def __init__(self, weather):
        self.weather = weather
        self.translatedd = []

    def translate_text(self):
        translator = Translator()
        for ent in self.weather:
            translated = translator.translate(str(ent), src='en', dest='sw')
            self.translatedd.append(translated.text)
        return self.translatedd

class TextToSpeech:
    def __init__(self, text):
        self.text = text

    def speak_text(self):
        for i in self.text:
            audio = gtts.gTTS(i)
            audio.save("temp.mp3")
            os.system("temp.mp3")

