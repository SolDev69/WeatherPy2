# from datetime import datetime
import math

from app import kToC, kToF, degree, command_line, weatherCity, weathergetLongTerm

from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)

if not command_line:
    print(
        "Please import this file and run the \'init()\' function if you wish to use this as a command line app"
    )


@app.route('/bye')
def bye_world():
    return "bye"


@app.route('/nothing')
def dex():
    return "This html file doesn't exist! It's generated fully by python/flask! Wow!"


@app.route('/pi')
def pi():
    return str(math.pi * 1)


# @app.route("/index")
# def index():
#     return render_template("default.html", time=datetime.now())
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if ((request.form.get('action1') == 'Submit')
                and (request.form.get('output1') != "")):
            return redirect("/weather?city=" + request.form.get('output1'))
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('root.html')

    return render_template("root.html")


# @app.route('/')
# def index():
#   if request.method == 'POST':
#         if request.form['submit_button'] == 'Do Something':
#             pass # do something
#         elif request.form['submit_button'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)
#   return render_template("root.html") TODO LATER
@app.route('/weather')
def weather():
    city = request.args.get('city')
    if (type(city) == type(None)):
        city = "Ottawa"

    output = weatherCity(city)
    forecast = weather
    temperatureC = str(kToC(output.json()["main"]["temp"])) + degree() + "C"
    temperatureF = str(kToF(output.json()["main"]["temp"])) + degree() + "F"
    temperature = str(output.json()["main"]["temp"]) + " Kelvin"
    forecastObject = weathergetLongTerm(output)
    i = 0
    forecast = []
    for day in forecastObject:
        # print(
        #     "It will be " + str(kToC(day["temp"]["day"])) + " in " + str(i) + "days"
        # )
        if i == 0:
            forecast.append("It will be " + str(kToC(day["temp"]["day"])) +
                            degree() + "C later today")
        else:
            forecast.append("It will be " + str(kToC(day["temp"]["day"])) +
                            degree() + "C in " + str(i) + " day(s)")
        i = i + 1
    return render_template("weather.html",
                           weather=temperatureC,
                           weatherF=temperatureF,
                           weatherK=temperature,
                           city=city,
                           #d1=forecast[0],
                           d2=forecast[1],
                           d3=forecast[2],
                           d4=forecast[3],
                           d5=forecast[4],
                           d6=forecast[5],
                           d7=forecast[6],
                           d8=forecast[7]
                          )


app.run(host='0.0.0.0', port=8080)
