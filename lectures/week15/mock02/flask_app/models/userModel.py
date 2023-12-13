from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import fishModel

class User:
    db = 'fishFrenzy'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.fishes = []


    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
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
    def userFishes(cls, data):
        query = 'SELECT * FROM user LEFT JOIN fish ON user.id = fish.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print('the resutls', results)
        user = cls(results[0])
        for row in results:
            fishData = {
                'id': row['fish.id'],
                'fishtype': row['fishtype'],
                'theNum': row['theNum'],
                'url': row['url'],
                'createdAt': row['fish.createdAt'],
                'updatedAt': row['fish.updatedAt'],
                'user_id': row['user_id']
            }
            user.fishes.append(fishModel.Fish(fishData))
        return user

    @classmethod
    def userLike(cls, data):
        query = 'INSERT into likeFish (user_id, fish_id) values (%(user_id)s, %(fish_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

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