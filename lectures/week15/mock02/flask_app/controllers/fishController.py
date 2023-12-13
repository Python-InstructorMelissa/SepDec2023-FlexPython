from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.userModel import User
from flask_app.models.fishModel import Fish

# fish form

@app.route('/fish/add/')
def addFish():
    thePage = {
        'title': 'Fish Frenzy'
    }
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addFish.html', page=thePage, user=theUser)

# create fish
@app.route('/fish/create/', methods=['post'])
def createFish():
    # fish = Fish.save(request.form)
    fish = {
        'fishtype': request.form['fishtype'],
        'theNum': request.form['theNum'],
        'url': request.form['url'],
        'user_id': int(session['user_id'])
    }
    newFish = Fish.save(fish)
    if newFish:
        fishID = newFish
        flash("Fish Added")
        return redirect(f'/fish/{fishID}/view/')
    else:
        flash('check terminal')
        return redirect('/fish/add/')

# view fish
@app.route('/fish/<int:fishID>/view/')
def viewFish(fishID):
    if 'user_id' not in session:
        return redirect('/')
    fishData = {
        'id': fishID
    }
    theFish = Fish.getOne(fishData)
    thePage = {
        'title': f'{theFish.fishtype}'
    }
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('viewFish.html', page=thePage, user=theUser, fish=theFish)

# edit fish form
@app.route('/fish/<int:fishID>/edit/')
def editFish(fishID):
    if 'user_id' not in session:
        return redirect('/')
    fishData = {
        'id': fishID
    }
    theFish = Fish.getOne(fishData)
    thePage = {
        'title': f'Edit {theFish.fishtype}'
    }
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('editFish.html', page=thePage, user=theUser, fish=theFish)

# update fish
@app.route('/fish/<int:fishID>/update/', methods=['post'])
def updateFish(fishID):
    fishData = {
        'id': fishID,
        'fishtype': request.form['fishtype'],
        'theNum': request.form['theNum'],
        'url': request.form['url']
    }
    Fish.update(fishData)
    return redirect(f'/fish/{fishID}/view/')

# delete fish
@app.route('/fish/<int:fishID>/delete/')
def deleteFish(fishID):
    fishData = {
        'id': fishID
    }
    Fish.delete(fishData)
    flash('That fish is flushed')
    return redirect('/')


@app.route('/like/', methods=['post'])
def likeFish():
    theLike = User.userLike(request.form)
    return redirect('/')