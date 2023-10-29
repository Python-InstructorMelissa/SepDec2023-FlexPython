from flask_app import app
from flask import session, render_template, redirect, request
from datetime import datetime

sessionHistory = []

#  Rendering 1 html document at the root route
@app.route('/')
def index():
    # if session['image'] does not exist
    if 'image' not in session:
        # var theImage is = to False
        theImage = False
    # otherwise make the var theImage = to what is in session
    else:
        theImage = session['image']
    if 'letter' not in session:
        theLetter = False
    else:
        theLetter = session['letter']
    if 'count' not in session:
        theCount = 0
        session['count'] = theCount
    else:
        theCount = session['count']
    # make sure to pass theImage into the return so that the html can see it (image is what the html sees theImage is what image is equal to)
    theHistory = sessionHistory
    return render_template('index.html', image=theImage, letter=theLetter, history=theHistory, count=theCount)


# This route tells us we are posting something to the system
@app.route('/createImage/', methods=['post'])
def createImage():
    # taking the info from the form and putting it directly into session
    session['image'] = request.form['image']
    if 'letter' in session:
        session['letter'] += request.form['letter']
    else:
        session['letter'] = request.form['letter']
    timeStamp = datetime.now()
    data = {
        'time': timeStamp,
        'image': request.form['image'],
        'letter': request.form['letter']
    }
    sessionHistory.append(data)
    return redirect('/')

@app.route('/increase/')
def increase():
    session['count'] = int(session['count']) + 1
    return redirect('/')

@app.route('/increase/2/')
def increase2():
    session['count'] = int(session['count']) + 2
    return redirect('/')

@app.route('/clearSession/')
def clearSession():
    session.clear()
    return redirect('/')

# all post, delete and clearing functions will ALWAYS redirect to someplace
# all forms or displaying of data will render_template