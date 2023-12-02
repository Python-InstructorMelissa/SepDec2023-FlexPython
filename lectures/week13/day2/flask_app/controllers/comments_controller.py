from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_app.models.comments_model import Comment
from flask_app.models.reply_model import Reply


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
    Comment.save(data)
    flash("Comment sent")
    return redirect('/dashboard/')


@app.route('/reply/add/<int:commentId>/')
def add_reply(commentId):
    if 'user_id' not in session:
        flash("Yo log in to see that page")
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        commentData = {
            'id': commentId
        }
        theComment = Comment.get_one(commentData)
        the_user = User.get_one(data)
        the_users = User.get_all()
    return render_template('add_reply.html', user=the_user, users=the_users, comment=theComment)


@app.route('/reply/create/<int:commentId>/', methods=['post'])
def create_reply(commentId):
    print(request.form)
    data = {
        'reply': request.form['reply'],
        'replyer_id': request.form['replyer_id'],
        # 'comment_id': request.form['comment_id']
        'comment_id': commentId
    }
    Reply.save(data)
    flash("Reply sent")
    return redirect('/dashboard/')