from Flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    DB = "users_cr"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['fname']) < 2:
            flash("* First name should be at least two characters.")
            is_valid = False
        
        if len(user['lname']) < 2:
            flash("* Last name should be at least two characters. ")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash("* Invalid E-mail address. ")
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)
            
    @classmethod
    def delete(cls, id):
        data = {"id": id}
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, id):
        data = {"id" : id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_most_recent_record(cls):
        query= "SELECT * FROM users ORDER BY id DESC;"
        results = connectToMySQL(cls.DB).query_db(query)
        return cls(results[0])