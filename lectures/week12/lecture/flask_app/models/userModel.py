from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = 'logRegGames'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']


    @classmethod
    def getAll(cls):
        q = 'select * from user;'
        res = connectToMySQL(cls.db).query_db(q)
        users = []
        for row in res:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        q = "SELECT * FROM user WHERE id = %(id)s;"
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])
    
    @classmethod
    def getEmail(cls, data):
        # This allows you to have your sql statement on multiple lines MUST BE 3 SETS OF DOUBLE QUOTES
        q = """
        SELECT *
        FROM user
        WHERE email = %(email)s;
        """
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
    @staticmethod
    def validate(user):
        isValid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash("Email is already in use in our database")
        if len(user['firstName']) < 2:
            isValid = False
            flash("Please use least least 2 characters for the first Name")
        if len(user['lastName']) < 2:
            isValid = False
            flash("Please use least least 2 characters for the last Name")
        if len(user['password']) < 6:
            isValid = False
            flash("Please use least least 6 characters for the password")
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Please use proper email format")
        if user['password'] != user['confirm']:
            isValid = False
            flash("Passwords don't match")
        return isValid