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
        self.dojo_id = None

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_ninja_by_id(cls, id):
        data={"id":id}
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def update_ninja(cls, data):
        query="UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_ninja(cls, id):
        data = {"id":id}
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
