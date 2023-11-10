from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.data.data import *


@app.route('/')
def hello():
    session.clear()
    return f'Is this app seems to be working <a href="/main">Go to Render HTML route</a>'

@app.route('/main')
def main():
    if 'month' not in session:
        session['month'] = False
    theeWord = session['month']
    return render_template('index.html')

@app.route('/renderData01/')
def renderData01():
    if 'month' not in session:
        session['month'] = False
    theWord = session['month']
    return render_template('renderData01.html', seasons=theSeasons, word=theWord)

@app.route('/renderData02/')
def renderData01():
    if 'month' not in session:
        session['month'] = False
    theWord = session['month']
    return render_template('renderData02.html', months=theMonths, word=theWord)

@app.route('/month/<month>/')
def addSession(month):
    session['month'] = month
    return redirect('/main')