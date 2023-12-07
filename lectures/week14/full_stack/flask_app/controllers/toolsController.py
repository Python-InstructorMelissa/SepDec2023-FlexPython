from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.userModel import User
from flask_app.models.profileModel import Profile
from flask_app.models.toolsModel import Tools


@app.route('/tool/add/')
def addTool():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addTool.html', user=theUser)
    
@app.route('/tool/create/', methods=['post'])
def createTool():
    Tools.save(request.form)
    flash("Yay Tool added")
    return redirect('/')