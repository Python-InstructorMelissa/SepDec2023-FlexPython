from flask_app.config.mysqlconnection import connectToMySQL



class Tools:
    db = 'marketPlace'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.descp = data['descp']
        self.defensive = data['defensive'] # boolean
        self.strength = data['strength']
        self.price = data['price']
        self.img = data['img']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']



    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM tools;'
        results = connectToMySQL(cls.db).query_db(query)
        toolss = []
        for row in results:
            toolss.append(cls(row))
        return toolss

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM tools WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO tools (name, descp, defensive, strength, price, img, count, user_id) VALUES(%(name)s, %(descp)s, %(defensive)s, %(strength)s, %(price)s, %(img)s, %(count)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE tools SET name=%(name)s, descp=%(descp)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def reduceCount(cls, data):
        query = 'UPDATE tools SET count=count-1 WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM tools WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
