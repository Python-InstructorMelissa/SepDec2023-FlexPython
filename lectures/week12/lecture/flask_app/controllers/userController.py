from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.userModel import User


bcrypt = Bcrypt(app)

# root = {
#     'title': 'title'
# }
# if 'user_id' in session:
#     return redirect('/')
# else:
#     theUser = False

@app.route('/')
def index():
    root = {
        'title': 'LogReg'
    }
    if 'user_id' not in session:
        theUser = False
        return render_template('index.html', root=root, user=theUser)
    else:
        return redirect('/dashboard')

@app.route('/logout/')
def logout():
    session.clear()
    flash("See Ya!")
    return redirect('/')


@app.route('/user/registration/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid: # if isValid is False the redirect back to '/' with flash message
        return redirect('/')
    else:
        newUser = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/')
        else:
            session['user_id'] = id
            flash("You logged in")
            return redirect('/dashboard/')
        
@app.route('/user/login/', methods=['post'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("Hey man that email is not in the database register please")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Dude wrong password")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("Welcome back")
        return redirect('/dashboard/')
        

@app.route('/dashboard/')
def dashboard():
    root = {
        'title': 'Dashboard'
    }
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('dashboard.html', root=root, user=theUser)