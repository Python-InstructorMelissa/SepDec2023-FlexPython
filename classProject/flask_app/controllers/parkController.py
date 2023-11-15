from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User
from flask_app.models.parkModel import Park

# theRoot = {
#     'title': 'title'
# }
# if 'user_id' not in session:
#     return redirect('/')
# else:
#     theUser = session['user_id']

@app.route('/parks/add/park/')
def addPark():
    theRoot = {
        'title': 'Add Park'
    }
    print('what is session', session['user_id'])
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    return render_template('parkFiles/addPark.html', root=theRoot, user=theUser)

@app.route('/parks/create/park/', methods=['post'])
def createPark():
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'user_id': request.form['user_id']
    }
    Park.save(data)
    return redirect('/')

@app.route('/parks/')
def allParks():
    theRoot = {
        'title': 'Add Park'
    }
    print('what is session', session['user_id'])
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
    theUsers = User.getAll()
    theParks = Park.getAll()
    return render_template('parkFiles/parks.html', root=theRoot, user=theUser, users=theUsers, parks=theParks)