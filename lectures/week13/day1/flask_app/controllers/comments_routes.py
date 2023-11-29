from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_app.models.comments_model import Comments


@app.route('/comment/add/')
def add_comment():
    if 'user_id' not in session:
        flash("Yo log in to see that page")
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        the_user = User.get_one(data)
        the_users = User.get_all()
    return render_template('add_comment.html', user=the_user, users=the_users)


@app.route('/comment/create/', methods=['post'])
def create_comment():
    data = {
        'comment': request.form['comment'],
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id']
    }
    Comments.save(data)
    flash("Comment sent")
    return redirect('/dashboard/')