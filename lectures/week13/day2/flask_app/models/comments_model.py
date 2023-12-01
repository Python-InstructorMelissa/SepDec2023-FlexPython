from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Comment:
    db = 'userCommentReply'
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM comment;'
        results = connectToMySQL(cls.db).query_db(query)
        comments = []
        for row in results:
            comments.append(cls(row))
        return comments

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM comment WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comment (comment, sender_id, receiver_id) VALUES(%(comment)s, %(sender_id)s, %(receiver_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE comment SET comment=%(comment)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM comment WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(comment):
        is_valid = True
        if len(comment['comment']) < 10:
            is_valid = False
            flash("Please use least least 10 characters for the comment")
        return is_valid