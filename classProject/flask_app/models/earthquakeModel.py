from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.userModel import User


class Earthquake:
    db = 'classProjSep23'
    def __init__(self, data):
        self.id = data['id']
        self.lat = data['lat']
        self.lon = data['lon']
        self.richter = data['richter']
        self.country = data['country']
        self.city = data['city']
        self.state = data['state']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        q = 'select * from earthquake;'
        res = connectToMySQL(cls.db).query_db(q)
        earthquakes = []
        for row in res:
            earthquakes.append(cls(row))
        return earthquakes

    @classmethod
    def getOne(cls, data):
        q = "SELECT * FROM earthquake WHERE id = %(id)s; "
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO earthquake (lat, lon, richter, country, city, state, user_id) VALUES (%(lat)s, %(lon)s, %(richter)s, %(country)s, %(city)s, %(state)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE earthquake SET lat=%(lat)s, lon=%(lon)s richter=%(richter)s, country=%(country)s, city=%(city)s, state=%(state)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM earthquake WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)