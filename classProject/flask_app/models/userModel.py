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
    def save(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass