from flask_app.config.mysqlconnection import connectToMySQL



class Profile:
    db = 'marketPlace'
    def __init__(self, data):
        self.id = data['id']
        self.strength = data['strength'] # default = 85
        self.money = data['money'] # default = 100
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']



    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM profile;'
        results = connectToMySQL(cls.db).query_db(query)
        profiles = []
        for row in results:
            profiles.append(cls(row))
        return profiles

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM profile WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO profile (user_id) VALUES(%(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def updateStrength(cls, data):
        query = 'UPDATE profile SET strength=%(strength)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def updateMoney(cls, data):
        query = 'UPDATE profile SET money=%(money)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM profile WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
