"""
1. Learn how to fetch wether data using the OpenWeatherMap API
2. USe NewsAPI.org to fetch top headlines
3. Use date and time module 
4. Use some free quote API to fetch daily inspirational quotes
5. make the dashboard look good with the rich library
"""

import requests
import json 
from tkinter import *
import math

city_name = "Joppatowne,US"
API_KEY = '574b03336b1071c7870836b63fc13435'

def get_weather(API_KEY, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url).json() #allwos us to access individual attributes 
    
    temp = response['main']['temp']
    temp = math.floor(temp - 273.15)
    
    feels_like = response['main']['feels_like']
    feels_like = math.floor(feels_like - 273.15)

    humidity = response['main']['humidity'] #in percentage

    return{
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }


weather = get_weather(API_KEY, city_name)    
print(weather)