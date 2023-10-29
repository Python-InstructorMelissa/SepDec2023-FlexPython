from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'parkAnimals'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        

    # query
    # results
    # return

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM user WHERE id=%(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        # print('get one user results', results)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM user WHERE email=%(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        # print('get one user results', results)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);'
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