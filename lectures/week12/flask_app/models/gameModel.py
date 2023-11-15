from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.userModel import User


class Game:
    db = 'logRegGames'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.desc = data['desc']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        q = 'select * from game;'
        res = connectToMySQL(cls.db).query_db(q)
        games = []
        for row in res:
            games.append(cls(row))
        return games

    @classmethod
    def getOne(cls, data):
        # This allows you to have your sql statement on multiple lines MUST BE 3 SETS OF DOUBLE QUOTES
        q = """
        SELECT *
        FROM game
        WHERE id = %(id)s;
        """
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO game (name, desc, user_id) VALUES (%(name)s, %(desc)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE game SET name=%(name)s, desc=%(desc)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM game WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
