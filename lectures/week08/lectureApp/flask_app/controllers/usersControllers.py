from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User


@app.route('/')
def index():
    theUsers = User.getAll()
    return render_template('index.html', users=theUsers)