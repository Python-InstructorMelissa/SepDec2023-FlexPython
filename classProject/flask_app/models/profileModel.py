from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.userModel import User


class Profile:
    db = 'classProjSep23'
    def __init__(self, data):
        self.id = data['id']
        self.lat = data['lat']
        self.lon = data['lon']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        q = 'select * from profile;'
        res = connectToMySQL(cls.db).query_db(q)
        profiles = []
        for row in res:
            profiles.append(cls(row))
        return profiles

    @classmethod
    def getOne(cls, data):
        q = "SELECT * FROM profile WHERE id = %(id)s; "
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO profile (lat, lon, user_id) VALUES (%(lat)s, %(lon)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE profile SET lat=%(lat)s, lon=%(lon)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM profile WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)