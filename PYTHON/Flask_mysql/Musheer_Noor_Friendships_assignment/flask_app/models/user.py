from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    DB = "friendships"
    def __init__(self, user_data):
        self.id = user_data['id']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.created_at = user_data['created_at']
        self.update_at = user_data['updated_at']


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.DB).query_db(query)
        

    @classmethod
    def add_user(cls, user_data):
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW() ); "
        return connectToMySQL(cls.DB).query_db(query, user_data)