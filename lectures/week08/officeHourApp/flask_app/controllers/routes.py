from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkAnimals import park

# ================================================
# These are hard coded routes no database
# ================================================

# ! You can use the better comments extension to color your comments

# ********** This is another version **********

# root = {
#     'title': 'title'
# }

@app.route('/fakeData')
def index():
    theData = park
    root = {
        'title': 'Hard Coded Data'
    }
    print("what does my data look like", theData)
    return render_template('fakeData.html', data=theData, root=root)