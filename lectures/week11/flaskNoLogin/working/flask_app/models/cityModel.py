from flask_app.config.mysqlconnection import connectToMySQL


class City:
    db = 'debugCitysGood'
    def __init__(self, data):
        self.id = data['id']
        self.cityName = data['cityName']
        self.cityState = data['cityState']
        self.addedBy = data['addedBy']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM city;'
        # let results = connect to the database send above query and return with results
        results = connectToMySQL(cls.db).query_db(query)
        cities = []
        for row in results:
            cities.append(cls(row))
        return cities

    @classmethod
    def getOne(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM city WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getCityName(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM city WHERE cityName = %(cityName)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO city (cityName, cityState, addedBy) VALUES (%(cityName)s, %(cityState)s, %(addedBy)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE city SET cityName=%(cityName)s, cityState=%(cityState)s, addedBy=%(addedBy)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM city WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)