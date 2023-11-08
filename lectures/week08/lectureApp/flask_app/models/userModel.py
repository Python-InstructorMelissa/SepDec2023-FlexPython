from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import animeModel

class User:
    db = 'anime'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.username = data['username']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.animes = []
        # Remember to loop through this list name to display the animes on the view one user

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        # let results = connect to the database send above query and return with results
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getUsername(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM user WHERE username = %(username)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (firstName, lastName, username) VALUES (%(firstName)s, %(lastName)s, %(username)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, username=%(username)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def userAnimes(cls, data):
        # This is how you can do a multi line query but it MUST BE 3 SETS OF DOUBLE QUOTES TO WORK
        q = """
            SELECT * FROM user
            LEFT JOIN anime
            ON user.id = anime.user_id
            WHERE user.id = %(id)s;
            """
        # left join user to anime
        # 1 user to many anime
        #  create an empty list in constructor to store the users anime
        # return the list with the user attached
        res = connectToMySQL(cls.db).query_db(q, data)
        user = cls(res[0])
        for row in res:
            animeData = {
                'id': row['anime.id'],
                'name': row['name'],
                'tvShow': row['tvShow'],
                'alignment': row["alignment"],
                'power': row['power'],
                'img': row['img'],
                'createdAt': row['anime.createdAt'],
                'updatedAt': row["anime.updatedAt"],
                'user_id':row["user_id"],
            }
            # self.animes = the list user.animes
            user.animes.append(animeModel.Anime(animeData))
        return user