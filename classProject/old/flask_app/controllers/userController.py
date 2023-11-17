from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User
from flask_app.models.parkModel import Park

# root = {
#     'title': 'title'
# }
# if 'user_id' in session:
#     return redirect('/')
# else:
#     theUser = False

@app.route('/logout/')
def reset():
    session.clear()
    root = {
        'title': 'Class Project'
    }
    if 'user_id' in session:
        theUser = session['user_id']
        return redirect('/')
    else:
        theUser = {
            'firstName': 'Guest'
        }
    return render_template('reset.html',root=root, user=theUser)

@app.route('/')
def index():
    root = {
        'title': 'Class Project'
    }
    if 'user_id' in session:
        # theUser = session['user_id']
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    else:
        theUser = {
            'firstName': 'Guest'
        }
    theUsers = User.getAll()
    theParks = Park.getAll()
    return render_template('index.html', root=root, user=theUser, users=theUsers, parks=theParks)

@app.route('/fakeLogReg/')
def fakeLogReg():
    root = {
        'title': '"Fake" Login/Registration'
    }
    if 'user_id' in session:
        theUser = session['user_id']
        return redirect('/')
    else:
        theUser = {
            'firstName': 'Guest'
        }
    return render_template('fakeLogReg.html', root=root, user=theUser)

@app.route('/user/create/', methods=['POST'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    newUser = User.save(data)
    session['user_id'] = newUser
    return redirect('/')

@app.route('/user/login/', methods=['POST'])
def loginUser():
    data = {
        'email': request.form['email']
    }
    loggedUser = User.getOneEmail(data)
    print('loggedUser', loggedUser.firstName, request.form['firstName'])
    session['user_id'] = loggedUser.id
    return redirect('/')

@app.route('/user/<int:user_id>/view/')
def viewUser(user_id):
    userData = {
        'id': user_id
    }
    viewUser = User.getOne(userData)
    root = {
        'title': f'Viewing {viewUser.firstName}'
    }
    if 'user_id' in session:
        # theUser = session['user_id']
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    else:
        theUser = {
            'firstName': 'Guest'
        }
    
    return render_template('viewUser.html', root=root, user=theUser, viewUser=viewUser)


@app.route('/user/<int:user_id>/edit/')
def editUser(user_id):
    userData = {
        'id': user_id
    }
    viewUser = User.getOne(userData)
    root = {
        'title': f'Editing {viewUser.firstName}'
    }
    if 'user_id' not in session:
        theUser = {
            'firstName': 'Guest'
        }
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    return render_template('editUser.html', root=root, user=theUser, viewUser=viewUser)


@app.route('/user/<int:user_id>/update/', methods=['post'])
def updateUser(user_id):
    data = {
        'id': request.form['id'],
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
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