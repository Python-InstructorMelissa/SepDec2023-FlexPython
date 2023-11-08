from flask_app.config.mysqlconnection import connectToMySQL


class Anime:
    db = "anime"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.tvShow = data["tvShow"]
        self.alignment = data["alignment"]
        self.power = data["power"]
        self.img = data['img']
        self.createdAt = data["createdAt"]
        self.updatedAt = data["updatedAt"]
        self.user_id = data["user_id"]

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM anime;"
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
        query = "INSERT INTO anime (name, tvShow, alignment, power, img, user_id) VALUES (%(name)s, %(tvShow)s, %(alignment)s, %(power)s, %(img)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, formData):
        """Updates an anime in the database."""

        query = """
        UPDATE anime
        SET name=%(name)s, tvShow=%(tvShow)s, alignment=%(alignment)s, power=%(power)s
        WHERE id = %(id)s;
        """
        connectToMySQL(cls.db).query_db(query, formData)
        return

    @classmethod
    def delete(cls, anime_id):
        """Deletes an anime from the database."""

        query = "DELETE FROM anime where id = %(id)s;"
        data = {"id": anime_id}

        connectToMySQL(cls.db).query_db(query, data)
        return
