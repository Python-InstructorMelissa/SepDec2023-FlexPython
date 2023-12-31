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
        self.animals = []
        self.parks = []


    @classmethod
    def getAll(cls):
        q = 'select * from user;'
        res = connectToMySQL(cls.db).query_db(q)
        users = []
        for row in res:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        # This allows you to have your sql statement on multiple lines MUST BE 3 SETS OF DOUBLE QUOTES
        q = """
        SELECT *
        FROM user
        WHERE id = %(id)s;
        """
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])
    
    @classmethod
    def getOneEmail(cls, data):
        # This allows you to have your sql statement on multiple lines MUST BE 3 SETS OF DOUBLE QUOTES
        q = """
        SELECT *
        FROM user
        WHERE email = %(email)s;
        """
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    def fullName(self):
        return f'{self.firstName} {self.lastName}'