from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User


@app.route('/')
def index():
    theUsers = User.getAll()
    if 'user_id' not in session:
        theUser = False
    else:
        data = {
        'id': session['user_id']
        }
        theUser = User.getOne(data)
    return render_template('index.html', users=theUsers, user=theUser)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

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
    newUser = User.save(data)
    print('the new user', newUser)
    session['user_id'] = newUser
    return redirect('/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'username': request.form['username']
    }
    loggedUser = User.getUsername(data)
    session['user_id'] = loggedUser.id
    return redirect('/')