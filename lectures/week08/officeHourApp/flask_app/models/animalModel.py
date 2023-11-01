from flask_app.config.mysqlconnection import connectToMySQL


class Animal:
    db = "parkAnimals"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.species = data["species"]
        self.appendages = data["appendages"]
        self.willToLive = data["willToLive"]
        self.isDead = data["isDead"]
        self.health = data["health"]
        self.createdAt = data["createdAt"]
        self.updatedAt = data["updatedAt"]
        self.user_id = data["user_id"]
        self.park = None

    # query
    # results
    # return

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM animal;"
        results = connectToMySQL(cls.db).query_db(query)
        animals = []
        for row in results:
            animals.append(cls(row))
        return animals

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM animal WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO animal (name, species, appendages, willToLive, isDead, health, user_id)
        VALUES (%(name)s, %(species)s, %(appendages)s, %(willToLive)s, %(isDead)s, %(health)s, %(user_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass

    @classmethod
    def animalWithAnimals():
        pass
