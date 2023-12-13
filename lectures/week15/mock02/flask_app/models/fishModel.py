from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import userModel


class Fish:
    db = 'fishFrenzy'
    def __init__(self, data):
        self.id = data['id']
        self.fishtype = data['fishtype']
        self.theNum = data['theNum']
        self.url = data['url']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM fish;'
        results = connectToMySQL(cls.db).query_db(query)
        fishs = []
        for row in results:
            fishs.append(cls(row))
        return fishs

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM fish WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO fish (fishtype, theNum, url, user_id) VALUES(%(fishtype)s, %(theNum)s, %(url)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE fish SET fishtype=%(fishtype)s, theNum=%(theNum)s, url=%(url)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM fish WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    