from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User

# root = {
#     'title': 'title'
# }

@app.route('/logReg/')
def logReg():
    root = {
        'title': 'Login / Register'
    }
    if 'user_id' in session:
        return redirect('/')
    else:
        theUser = False
    return render_template('logReg.html', root=root, user=theUser)

@app.route('/createUser/', methods=['post'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    newUser = User.save(data)
    session['user_id'] = newUser
    return redirect('/')

@app.route('/returnUser/', methods=['post'])
def returnUser():
    data = {
        'email': request.form['email']
    }
    theUser = User.getEmail(data)
    session['user_id'] = theUser.id
    return redirect('/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')