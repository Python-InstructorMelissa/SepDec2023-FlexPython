from flask_app.config.mysqlconnection import connectToMySQL

class Park:
    db = 'parkAnimals'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.animals = []

    # query
    # results
    # return

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM park;'
        results = connectToMySQL(cls.db).query_db(query)
        parks = []
        for row in results:
            parks.append(cls(row))
        return parks

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM park WHERE id=%(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO park (name, location, user_id) VALUES (%(name)s, %(location)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass

    @classmethod
    def parkWithAnimals():
        pass