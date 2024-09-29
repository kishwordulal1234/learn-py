#!/usr/bin/python3
import requests
print("give me a bottle of rum!")

n = input("inter the place that you wnat to get weather of ")
weather = requests.get(f"https://www.accuweather.com/en/np/{n}/241809/weather-forecast/241809")

if weather.status_code == 200:
    print(requests.json)