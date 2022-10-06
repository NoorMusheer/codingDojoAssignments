from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_author_by_id(cls, id):
        data={"id" : id}
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_fav_books_by_author(cls, id):
        data = {"id":id}
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def add_to_favs(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)