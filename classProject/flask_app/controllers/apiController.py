from flask_app import app
from flask import render_template, redirect, jsonify, request, session, flash
import requests
from flask_app.config import key
from flask_app.models.profileModel import Profile

api_url = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'
weatherAPI = key.WEATHER_API_KEY

@app.route('/user/zipCode/', methods=['post'])
def latLong():
    print('the form', request.form)
    theZip = request.form['zip_code']
    geoUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={theZip}&appid={weatherAPI}"
    print('geoUrl', geoUrl)
    response = requests.get(geoUrl)
    res = response.json()
    session['user_zip'] = theZip
    user = session['user_id']
    locationData = {
        'user_id': user,
        'lat': res['lat'],
        'lon': res['lon']
    }
    updateProfile = Profile.update(locationData)
    print(res)
    return res

def getConditions(lat, lon):
    weatherUrl = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=imperial{weatherAPI}"
    response = requests.get(weatherUrl)
    res = response.json()
    return res