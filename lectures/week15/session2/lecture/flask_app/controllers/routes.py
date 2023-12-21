from flask_app import app
from flask import render_template, redirect, jsonify
import requests

theWords = [
    'hi',
    'hello',
    'whats up'
]
api = 'https://dojo.navyladyveteran.com/characters/'

@app.route('/')
def index():
    api = 'https://dojo.navyladyveteran.com/characters/'
    api02 = 'https://dojo.navyladyveteran.com/squishies/'
    res = requests.get(api)
    res02 = requests.get(api02)
    if res.status_code == 200:
        theTunes = res.json()
        if res02.status_code == 200:
            theSquishs = res02.json()
            return render_template('index.html', words=theWords, tunes=theTunes, squishs=theSquishs)
    else:
        return jsonify({"error": "Bad Request"}), 500


@app.route('/api')
def api():
    
    res = requests.get(api)
    if res.status_code == 200:
        toons = res.json()
        return jsonify({"theToons": toons})
    else:
        return jsonify({"error": "Bad Request"}), 500

