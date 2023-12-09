from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.userModel import User
from flask_app.models.profileModel import Profile
from flask_app.models.toolsModel import Tools

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('logreg.html')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theTools = Tools.getAll()
        return render_template('index.html', user=theUser, tools=theTools)
    

@app.route('/registration/', methods=['post'])
def registration():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    else:
        newUser = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash('Something went wrong')
            return redirect('/')
        else:
            session['user_id'] = id
            data = {
                'user_id': id
            }
            userProfile = Profile.save(data)
            if not userProfile:
                flash("You are now logged in")
                return redirect('/')
            else:
                flash("Logged in and profile created")
                return redirect('/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data) # check if the email is in the database
    if not user: # if not let them know
        flash('That email is not in our database please register')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Wrong password')
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("You are now logged in")
        return redirect('/')



@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')