from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Reply:
    db = 'userCommentReply'
    def __init__(self, data):
        self.id = data['id']
        self.reply = data['reply']
        self.replyer_id = data['replyer_id']
        self.comment_id = data['comment_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM reply;'
        results = connectToMySQL(cls.db).query_db(query)
        replys = []
        for row in results:
            replys.append(cls(row))
        return replys

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM reply WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO reply (reply, replyer_id, comment_id) VALUES(%(reply)s, %(sender_id)s, %(receiver_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE reply SET reply=%(reply)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM reply WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(reply):
        is_valid = True
        if len(reply['reply']) < 10:
            is_valid = False
            flash("Please use least least 10 characters for the reply")
        return is_valid