from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.userModel import User


class Weather:
    db = 'classProjSep23'
    def __init__(self, data):
        self.id = data['id']
        self.temp = data['temp']
        self.humidity = data['humidity']
        self.description = data['description']
        self.pressure = data['pressure']
        self.icon = data['icon']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']


    @classmethod
    def getAll(cls):
        q = 'select * from weather;'
        res = connectToMySQL(cls.db).query_db(q)
        weathers = []
        for row in res:
            weathers.append(cls(row))
        return weathers

    @classmethod
    def getOne(cls, data):
        q = "SELECT * FROM weather WHERE id = %(id)s; "
        res = connectToMySQL(cls.db).query_db(q, data)
        if len(res) < 1:
            return False
        return cls(res[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO weather (temp, humidity, description, pressure, icon,user_id) VALUES (%(temp)s, %(humidity)s, %(description)s, %(pressure)s, %(icon)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE weather SET temp=%(temp)s, humidity=%(humidity)s, description=%(description)s , pressure=%(pressure)s , icon=%(icon)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM weather WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)