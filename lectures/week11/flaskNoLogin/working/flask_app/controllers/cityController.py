from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.cityModel import *

errorsFound = '8/8'


@app.route('/')
def index():
    if 'user' not in session:
        theUser = False
    else:
        theUser = session['user']
    return render_template('index.html', user=theUser, found=errorsFound)

@app.route('/user/session/', methods=['post'])
def userSession():
    session['user'] = request.form['addedBy']
    return redirect('/cities/all/')

@app.route('/cities/all/')
def allCities():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
    theCities = City.getAll()
    return render_template('allCities.html', user=theUser, cities=theCities, found=errorsFound)

@app.route('/city/add/')
def addCity():
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
    return render_template('addCity.html', user=theUser, found=errorsFound)

@app.route('/city/create/', methods=['post'])
def createCity():
    data = {
        'cityName': request.form['cityName'],
        'cityState': request.form['cityState'],
        'addedBy': request.form['addedBy']
    }
    newCity = City.save(data)
    return redirect(f'/cities/all/')

@app.route('/city/<int:city_id>/view/')
def viewCity(city_id):
    if 'user' not in session:
        return redirect('/')
    else:
        theUser = session['user']
    data = {
        'id': city_id
    }
    theCity = City.getOne(data)
    return render_template('viewCity.html', user=theUser, city=theCity, found=errorsFound)

@app.route('/exit/')
def exit():
    session.clear()
    return redirect('/')