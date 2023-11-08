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
    if 'user_id' not in session:
        theUser = False
    else:
        data = {
        'id': session['user_id']
        }
        theUser = User.getOne(data)
    viewData = {
            'id': user_id
        }
    viewUser = User.getOne(viewData)
    theUserAnimes = User.userAnimes(data)
    print('the anime list', theUserAnimes)
    return render_template('viewUser.html', user=theUser, userAnimes=theUserAnimes, vUser=viewUser)

@app.route('/user/add/')
def addUser():
    return render_template('addUser.html')

@app.route('/user/create/', methods=['post'])
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

@app.route('/user/<int:user_id>/edit/')
def editUser(user_id):
    if 'user_id' not in session:
        theUser = False
    else:
        data = {
        'id': session['user_id']
        }
        theUser = User.getOne(data)
        viewData = {
            'id': user_id
        }
        viewUser = User.getOne(viewData)
    return render_template('editUser.html', user=theUser, vUser=viewUser)

@app.route('/user/<int:user_id>/update/', methods=['POST'])
def updateUser(user_id):
    data = {
        'id': request.form['id'],
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'username': request.form['username']
    }
    User.update(data)
    return redirect(f'/user/{user_id}/view/')

@app.route('/user/<int:user_id>/delete/')
def deleteUser(user_id):
    data = {
        'id': user_id
    }
    User.delete(data)
    return redirect('/logout/')