from flask_app.config.mysqlconnection import connectToMySQL

class Anime:
    db = 'anime'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.tvShow = data['tvShow']
        self.alignment = data['alignment']
        self.power = data['power']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM anime;'
        # let results = connect to the database send above query and return with results
        results = connectToMySQL(cls.db).query_db(query)
        animes = []
        for row in results:
            animes.append(cls(row))
        return animes

    @classmethod
    def getOne(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM anime WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO anime (name, tvShow, alignment, power, user_id) VALUES (%(name)s, %(tvShow)s, %(alignment)s, %(power)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass