from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Comments:
    db = 'refresherComments'
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM comments;'
        results = connectToMySQL(cls.db).query_db(query)
        commentss = []
        for row in results:
            commentss.append(cls(row))
        return commentss

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM comments WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comments (comment, sender_id, receiver_id) VALUES(%(comment)s, %(sender_id)s, %(receiver_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE comments SET comment=%(comment)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM comments WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(comments):
        is_valid = True
        if len(comments['comment']) < 10:
            is_valid = False
            flash("Please use least least 10 characters for the comment")
        return is_valid