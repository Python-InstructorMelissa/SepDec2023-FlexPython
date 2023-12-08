from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.userModel import User
from flask_app.models.imageModel import Image

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    thePage = {
        'title': 'Home'
    }
    if 'user_id' not in session:
        return render_template('logReg.html', page=thePage)
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theImages = Image.getAll()
        theUsers = User.getAll()
        # print('please work', theAllImages)
        return render_template('index.html', user=theUser, page=thePage, allImages=theImages, users=theUsers)
    

@app.route('/logout/')
def logout():
    session.clear()
    flash("See Ya!")
    return redirect('/')

@app.route('/reg/', methods=['post'])
def registration():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    else:
        new_user = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(new_user)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/')
        else:
            session['user_id'] = id
            flash("Welcome, you are now logged in")
            return redirect('/')
        
@app.route('/login/', methods=['post'])
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
        return redirect('/')
    

# profile