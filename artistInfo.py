
import requests
from pprint import pprint
from gpiozero import Button
from signal import pause
button = Button(2)

API_KEY = "6bbb512da09f63739a8b648f1e908cd9" 
ARTIST = input("Who is your favourite Artst?: ")

print(f"\n...Press the button to find out about {ARTIST}...\n")


def printInfo():
	url =  "http://ws.audioscrobbler.com/2.0/"

	params = {
    	"method": "artist.getinfo",
    	"artist": ARTIST,
    	"api_key": API_KEY,
    	"format": "json"
	}

	response = requests.get(url, params=params)

	info = response.json()["artist"]["bio"]["content"]
	print(info.rstrip("\n"), end="")
	print()


"""Button Trigger """
button.when_pressed =  printInfo
pause()

