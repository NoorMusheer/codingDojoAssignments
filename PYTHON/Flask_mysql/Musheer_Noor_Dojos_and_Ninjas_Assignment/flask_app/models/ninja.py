from flask_app.config.mysqlconnection import connectToMySQL

class Ninja :
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['create_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at) VALUE (%(first_name)s, %(last_name)s, %(age)s, NOW (), NOW ());"
        return connectToMySQL(cls.DB).query_db(query, data)