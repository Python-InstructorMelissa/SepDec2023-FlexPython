from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.userModel import User
from flask_app.models.imageModel import Image


# Load Add Image form
@app.route('/image/add/')
def addImage():
    if 'user_id' not in session:
        flash('You need to be logged in dork')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        thePage = {
            'title': 'Add Image'
        }
        theUser = User.getOne(data)
        return render_template('addImage.html', user=theUser, page=thePage)

# Create Image
@app.route('/image/create/', methods=['post'])
def createImage():
    newImg = Image.save(request.form)
    if not newImg:
        flash('You messed up someplace Melissa')
        return redirect('/image/add/')
    else:
        flash('See you can do this')
        return redirect('/')



# view 1 image





# load edit image form




# update image


# delete image
@app.route('/image/<int:imageID>/delete/')
def deleteImage(imageID):
    data = {
        'id': imageID
    }
    Image.delete(data)
    return redirect('/')