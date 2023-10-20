from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User


@app.route('/')
def index():
    # if 'user_id' not in session:
    #     theUser = False
    theUsers = User.getAll()
    # data = {
    #     'id': session['user_id']
    # }
    # theUser = User.getOne(data)
    return render_template('index.html', users=theUsers)

@app.route('/user/<user_id>/view/')
def viewUser(user_id):
    data = {
        'id': user_id
    }
    theUser = User.getOne(data)
    return render_template('viewUser.html', user=theUser)

@app.route('/addUser/')
def addUser():
    return render_template('addUser.html')

@app.route('/createUser/', methods=['post'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'username': request.form['username']
    }
    User.save(data)
    # session['user_id'] = id
    return redirect('/')