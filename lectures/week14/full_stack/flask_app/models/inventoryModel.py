from flask_app.config.mysqlconnection import connectToMySQL



class Inventory:
    db = 'good_vs_not_good'
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.tools_id = data['tools_id']



    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM inventory;'
        results = connectToMySQL(cls.db).query_db(query)
        inventorys = []
        for row in results:
            inventorys.append(cls(row))
        return inventorys

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM inventory WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO inventory (user_id, tools_id) VALUES(%(user_id)s, %(tools_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE inventory SET tools_id=%(tools_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM inventory WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
