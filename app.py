from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "3c195f88f2b5332c421ae8dd55ae467e"

        #81faa0545c9b0ed35b3ab3bcd0a3c657
        #2551ccc05190884ef08f3f4a2ea4f9d1

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial'
        )
        weather_data = weather_url.json()

        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return render_template("result.html",temp=temp,humidity=humidity,wind_speed=wind_speed,city=city)
    return render_template("index.html")