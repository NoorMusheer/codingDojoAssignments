from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Friendship:
    DB = "friendships"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.user2_id = data['user2_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_friendships(cls):
        query = "SELECT users.first_name, users.last_name, users2.first_name AS fr_first, users2.last_name as fr_last FROM users JOIN friendships ON users.id = friendships.user_id JOIN users AS users2 ON users2.id = friendships.user2_id;"
        result = connectToMySQL(cls.DB).query_db(query)
        friendships = []
        for each_one in result:
            friendships.append(each_one)
        return result
        
    @classmethod
    def add_friendship(cls, data):
        query = "INSERT INTO friendships (user_id, user2_id, created_at , updated_at) VALUES (%(id1)s, %(id2)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)