from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

@app.route('/dashboard/')
def index():
    if 'user_id' not in session:
        flash("Yo log in to see that page")
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        the_user = User.get_one(data)
        the_sender_comments = User.sender_comments(data)
        the_receiver_comments = User.receiver_comments(data)
        the_users = User.get_all()
    return render_template('index.html', user=the_user, sender_comments=the_sender_comments, receiver_comments=the_receiver_comments, users=the_users)

@app.route('/')
def log_reg():
    return render_template('log_reg.html')

@app.route('/registration/', methods=['post'])
def registration():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    else:
        new_user = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
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
            return redirect('/dashboard/')

@app.route('/login/', methods=['post'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.get_email(data)
    if not user:
        flash("Hey man that email is not in the database register please")
        redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Dude wrong password")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("Welcome back")
        return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    flash("See Ya!")
    return redirect('/')