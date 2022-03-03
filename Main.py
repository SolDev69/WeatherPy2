import traceback

import requests
import os

# Functions
from Constants import *

def kToF(inputTemp):
    return round((inputTemp-273.15) * 9/5 + 32, 2)
def newLine():
    return "\n"
def space():
    return " "
def kToC(inputtemp):
    return round(inputtemp-273.15, 2)
def dot():
    return "."
def degree():
    return "°"
def printData(r):
    print("Raw data:")
    print(r.json())
    print()
    printvalue = r.json()["name"] + " " + "Temperature = " + str(r.json()["main"]["temp"]) + "K " + str(kToF(r.json()["main"]["temp"])) + degree() + " " + str(kToC(r.json()["main"]["temp"])) + degree() + newLine() + "Feels like " + str(r.json()["main"]["feels_like"]) + "K " + str(kToF(r.json()["main"]["feels_like"])) + degree() + " " + str(kToC(r.json()["main"]["feels_like"])) + degree() + newLine() + "High " + str(r.json()["main"]["temp_max"]) + "K " + str(kToF(r.json()["main"]["temp_max"])) + degree() + " " + str(kToC(r.json()["main"]["temp_max"])) + degree() + newLine() + "Low " + str(r.json()["main"]["temp_min"]) + "K " + str(kToF(r.json()["main"]["temp_min"])) + degree() + " " + str(kToC(r.json()["main"]["temp_min"])) + degree() + newLine() + "ID " + str(r.json()["weather"][0]["id"]) + newLine() + "The weather now is " + str(r.json()["weather"][0]["description"]) + ", or " + str(r.json()["weather"][0]["main"]).lower() + dot() + newLine()
    print(printvalue)
    return r.json()["main"]["temp"]
# def printData(r):
    print("Raw data:")
    print(r.json())
    print()
    printvalue = r.json()["name"] + " " + "Temperature = " + str(r.json()["main"]["temp"]) + "K " + str(kToF(r.json()["main"]["temp"])) + degree() + " " + str(kToC(r.json()["main"]["temp"])) + degree() + newLine() + "Feels like " + str(r.json()["main"]["feels_like"]) + "K " + str(kToF(r.json()["main"]["feels_like"])) + degree() + " " + str(kToC(r.json()["main"]["feels_like"])) + degree() + newLine() + "High " + str(r.json()["main"]["temp_max"]) + "K " + str(kToF(r.json()["main"]["temp_max"])) + degree() + " " + str(kToC(r.json()["main"]["temp_max"])) + degree() + newLine() + "Low " + str(r.json()["main"]["temp_min"]) + "K " + str(kToF(r.json()["main"]["temp_min"])) + degree() + " " + str(kToC(r.json()["main"]["temp_min"])) + degree() + newLine() + "ID " + str(r.json()["weather"][0]["id"]) + newLine() + "The weather now is " + str(r.json()["weather"][0]["description"]) + ", or " + str(r.json()["weather"][0]["main"]).lower() + dot() + newLine()
    print(printvalue)
    return r.json()["main"]["temp"]

def printDataLong(r):
    print()
    print(
        "Daily forecast"
    )
    i = 0
    for day in r.json()["daily"]:
        print(
            "It will be " + str(kToC(day["temp"]["day"])) + " in " + str(i) + "days"
        )
        i=i+1


#Check if api key exists
if(os.getenv("WEATHER_API_KEY") == None):
    print("Please create an account at http://openweathermap.org/api, create a key, and run 'setx WEATHER_API_KEY = ' your api key if on windows")
    exit(2)


def weathergetLongTerm(j):
    lat = j.json()["coord"]["lat"]
    lon = j.json()["coord"]["lon"]
    ln = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + os.getenv("WEATHER_API_KEY")
    s = requests.get(ln)
    print(ln)
    print(s.json())
    printDataLong(s)
# Main function
def weatherget(uszipcode):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+uszipcode+",us&appid=" + os.getenv("WEATHER_API_KEY"))
    printData(r)
    weathergetLongTerm(r)


def weatherGetCity(location, country):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "," + country + "&appid=" + os.getenv("WEATHER_API_KEY"))
    printData(r)

def weatherCity(location):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + os.getenv("WEATHER_API_KEY"))
    #printData(r)
    return r

command_line = False

def init():
    try:
        uszip = str(input("Input US ZIP code, if not just leave empty.\n"))
        weatherget(uszip)
    except Exception as e:
        track = traceback.format_exc()
        print(track)
        print("External location detected! (1.1 features not present in this mode)" + newLine())
        city = str(input("Input city name" + newLine()))
        try:
            weatherGetCity(city, str(input("country (optional)" + newLine())))
        except:
            weatherCity(city)

def runCommandLine():
    return init()

def weatherGetFlask(uszipcode, country):
    zip = str(uszipcode)
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zip+"," + country + "&appid=" + os.getenv("WEATHER_API_KEY"))

    return printData(r)
# Start of program
print(app_name + newLine() + "Version " + version + space() + phase)

# TODO: Get working on heroku

