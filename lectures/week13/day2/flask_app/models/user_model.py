from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import comments_model


class User:
    db = 'userCommentReply'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.receiver_comments = [] # This format is used to create a empty list where one users's items can go in this case comments.  This is typically used with a single left join statement
        self.sender_comments = []

    def full_name(self):
        return f'{self.firstName} {self.lastName}'
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES(%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def receiver_comments(cls, data):
        query = 'SELECT * FROM user LEFT JOIN comment ON user.id = comment.receiver_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            comment_data = {
                'id': row['comment.id'],
                'comment': row['comment'],
                'sender_id': row['sender_id'],
                'receiver_id': row['receiver_id']
            }
            user.receiver_comments.append(comments_model.Comment(comment_data))
        return user
    
    @classmethod
    def sender_comments(cls, data):
        query = 'SELECT * FROM user LEFT JOIN comment ON user.id = comment.sender_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            comment_data = {
                'id': row['comment.id'],
                'comment': row['comment'],
                'sender_id': row['sender_id'],
                'receiver_id': row['receiver_id']
            }
            user.sender_comments.append(comments_model.Comment(comment_data))
        return user

    @staticmethod
    def validate(user):
        is_valid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            is_valid = False
            flash("Email is already in use in our database")
        if len(user['firstName']) < 2:
            is_valid = False
            flash("Please use least least 2 characters for the first Name")
        if len(user['lastName']) < 2:
            is_valid = False
            flash("Please use least least 2 characters for the last Name")
        if len(user['password']) < 6:
            is_valid = False
            flash("Please use least least 6 characters for the password")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Please use proper email format")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords don't match")
        return is_valid