from flask_app import app
from flask import render_template, redirect
from flask_app.dataFiles.mealPlanning import *
from flask_app.dataFiles.studentGrades import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meals')
def meals():
    theMeals = mealPlanning
    print("the Meals", theMeals[0])
    return render_template("meals.html", meals=theMeals)

@app.route('/grades')
def grades():
    theGrades = classroom
    print('the data', theGrades[0])
    return render_template("grades.html", grades=theGrades)

