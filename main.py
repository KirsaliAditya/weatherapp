import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=eef6043cf3fc47beb6b165810230105&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
weather = wdic["current"]["condition"]["text"]
lat = wdic["location"]["lat"]
long = wdic["location"]["lon"]
time = wdic["location"]["localtime"]
print(f"the current in {city} is {w} degrees")
print(f"Weather: {weather}")
print(f"Latitude: {lat}")
print(f"Longitude: {long}")
print(f"Date & Time: {time}")

speaker.speak(f"the current in {city} is {w} degrees")



