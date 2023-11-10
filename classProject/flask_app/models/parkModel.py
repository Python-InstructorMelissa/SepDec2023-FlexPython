from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.userModel import User


class Park:
    db = 'parkAnimals'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        q = 'select * from park;'
        res = connectToMySQL(cls.db).query_db(q)
        parks = []
        for row in res:
            parks.append(cls(row))
        return parks

    @classmethod
    def getOne(cls, data):
        # This allows you to have your sql statement on multiple lines MUST BE 3 SETS OF DOUBLE QUOTES
        q = """
        SELECT *
        FROM park
        WHERE id = %(id)s;
        """
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO park (name, location, user_id) VALUES (%(name)s, %(location)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE park SET name=%(name)s, location=%(location)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM park WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
