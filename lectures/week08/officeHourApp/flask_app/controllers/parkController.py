from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkModel import Park


@app.route('/allParks')
def allParks():
    theParks = Park.getAll()
    return render_template('allParks.html', parks=theParks)