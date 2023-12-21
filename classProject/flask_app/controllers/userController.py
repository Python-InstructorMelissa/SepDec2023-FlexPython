from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.userModel import User
from flask_app.models.profileModel import Profile

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
        'title': 'Login & Registration'
    }
    if 'user_id' in session:
        flash("Your still logged in man")
        return redirect('/dashboard/')
    else:
        theUser = False
    return render_template('index.html', root=root, user=theUser)

@app.route('/logout/')
def logout():
    session.clear()
    flash("See Ya Sucker!")
    return redirect('/')

@app.route('/dashboard/')
def dashboard():
    root = {
        'title': 'The Dashboard'
    }
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        if 'zip_code' not in session:
            zip_code = False
        zip_code = session['zip_code']    
        return render_template('dashboard.html', root=root, user=theUser, zip=zip_code)

@app.route('/user/register/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
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
            flash("Not sure what but you dun screwed something up")
            return redirect('/')
        else:
            profile_id = {
                'user_id': id
            }
            Profile.save(profile_id)
            session['user_id'] = id
            flash("Hey man welcome to the app")
            return redirect('/dashboard')
        
@app.route('/user/login/', methods=['post'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("Yo maybe you should register first man!")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Dummy head you got the wrong password again")
        return redirect('/')
    else:
        userData = {
            'user_id': user.id
        }
        profile = Profile.get_by_user(userData)
        if not profile:
            Profile.save(userData)
        session['user_id'] = user.id
        flash("Hey you came back you must like it here")
        return redirect('/dashboard/')
    

@app.route('/new/')
def new():
    root = {
        'title': 'The Other Dashboard'
    }
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('dashboard.html', root=root, user=theUser)