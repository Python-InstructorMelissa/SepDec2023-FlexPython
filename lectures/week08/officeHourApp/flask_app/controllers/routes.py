from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkAnimals import park



@app.route('/')
def index():
    theData = park
    print("what does my data look like", theData)
    return render_template('index.html', data=theData)