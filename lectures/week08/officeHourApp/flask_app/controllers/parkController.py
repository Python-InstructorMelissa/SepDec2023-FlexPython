from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkModel import Park
from flask_app.models.userModel import User

# root = {
#     'title': 'title'
# }

@app.route('/')
def allParks():
    root = {
        'title': 'Parks and Animals'
    }
    # print('the session', session['user_id'])
    if 'user_id' not in session:
        theUser = False
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    theParks = Park.getAll()
    return render_template('index.html', parks=theParks, root=root, user=theUser)