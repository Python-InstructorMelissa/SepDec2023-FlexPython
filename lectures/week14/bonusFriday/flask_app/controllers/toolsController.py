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

@app.route('/tool/<int:toolID>/view/')
def viewTool(toolID):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': toolID
    }
    theTool = Tools.getOne(data)
    userData = {
        'id': session['user_id']
    }
    theUser = User.getOne(userData)
    theUsers = User.getAll()
    return render_template('viewTool.html', user=theUser, tool=theTool, users=theUsers)

@app.route('/tool/<int:toolID>/<int:userID>/purchase/', methods=['post'])
def purchaseTool(toolID, userID):
    toolData = {
        'id': toolID
    }
    updatedCount = Tools.reduceCount(toolData)
    print('count reduced?', updatedCount.count)
    theTool = Tools.getOne(toolData)
    pass
