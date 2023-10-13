from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    theData = {
        "title": "Hello",
        "date": "10/10/2023"
    }
    return render_template("index.html", data=theData)

@app.route('/createName', methods=['POST'])
def createName():
    print(request.form)
    session['name'] = request.form['name']
    return redirect('/nameAdded')

@app.route('/nameAdded')
def nameAdded():
    if 'name' not in session:
        return redirect('/')
    else:
        theData = {
            "title": "Hello",
            "date": "10/10/2023"
        }
        return render_template("nameAdded.html", data=theData)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')