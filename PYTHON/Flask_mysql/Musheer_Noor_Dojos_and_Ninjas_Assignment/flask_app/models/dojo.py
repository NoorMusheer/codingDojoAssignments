from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []
        # The above line is setting an empty list to eventually take in all the ninjas that belong to the particular dojo. Because one dojo can have many ninjas.

    @classmethod
    def create_a_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)  
            # The above return line is returning the updated database. #

    @classmethod
    def display_all_records(cls):
        query = "SELECT * FROM dojos;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def display_dojo_by_id(cls, id):
        data = {"id": id}
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def ninjas_by_dojo(cls, id):
        data = {"id":id}
        query = "SELECT *, ninjas.id AS NinID FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

