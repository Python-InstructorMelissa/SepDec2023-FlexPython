from flask_app import app
from flask import render_template, redirect

theNames = [
    'Melissa',
    'Stephanie',
    'Eric',
    'Corey',
    'Lydia',
    'Kevin',
    'Keith',
    'Delvon',
    'Dre',
    'Geoffrey',
    'Wyn',
    'Lawrence'
]
theCohort = "Web Fundamentals"


@app.route('/')
def index():
    return render_template('index.html', names=theNames, cohort=theCohort)

@app.route('/success')
def success():
    return "success"