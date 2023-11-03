from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User

# root = {
#     'title': 'title'
# }
# if 'user_id' in session:
#     return redirect('/')
# else:
#     theUser = False

@app.route('/reset/')
def reset():
    session.clear()
    root = {
        'title': 'Class Project'
    }
    if 'user_id' in session:
        theUser = session['user_id']
        return redirect('/')
    else:
        theUser = False
    return render_template('reset.html',root=root, user=theUser)

@app.route('/')
def index():
    root = {
        'title': 'Class Project'
    }
    if 'user_id' in session:
        return redirect('/reset/')
    else:
        theUser = False
    theUsers = User.getAll()
    return render_template('index.html', root=root, user=theUser, users=theUsers)