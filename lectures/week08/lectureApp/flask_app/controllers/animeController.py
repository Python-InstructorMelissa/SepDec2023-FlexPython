from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.userModel import User
from flask_app.models.animeModel import Anime

@app.route('/allAnime/')
def allAnime():
    theAnimes = Anime.getAll()
    theUsers = User.getAll()
    return render_template('allAnime.html', animes=theAnimes, users=theUsers)

@app.route('/anime/<anime_id>/view')
def viewAnime(anime_id):
    data = {
        'id': anime_id
    }
    theAnime = Anime.getOne(data)
    return render_template('viewAnime.html', anime=theAnime)

@app.route('/addAnime/')
def addAnime():
    theUsers = User.getAll()
    return render_template('addAnime.html', users=theUsers)

@app.route('/createAnime/', methods=['post'])
def createAnime():
    data = {
        'name': request.form['name'],
        'tvShow': request.form['tvShow'],
        'alignment': request.form['alignment'],
        'power': request.form['power'],
        'user_id': request.form['user_id']
    }
    Anime.save(data)
    return redirect('/allAnime/')