from flask_app import app
from flask import render_template, redirect, session, request

userList = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addUser')
def addUser():
    return render_template("addUser.html")

@app.route('/createUser', methods=['post'])
def createUser():
    session['user'] = request.form['user']
    userList.append(session['user'])
    return redirect('/users')

@app.route('/users')
def users():
    if 'user' not in session:
        return redirect('/addUser')
    else:
        return render_template("users.html", users=userList)
    
@app.route('/logout/')
def logout():
    session.clear()
    userList = []
    return redirect('/')

@app.route('/removeName/<user>')
def removeName(user):
    userList.remove(user)
    return redirect('/users')

@app.route('/editUser/<user>')
def editUser(user):
    user = user
    return render_template('editUser.html',user=user)

@app.route('/updateUser/<user>', methods=['post'])
def updateUser(user):
    badUser = user
    newUser = request.form['user']
    print('badUser', badUser, 'newUser', newUser)
    for user in userList:
        if user == badUser:
            user = newUser
    print('thelist', userList)
    return redirect('/users')