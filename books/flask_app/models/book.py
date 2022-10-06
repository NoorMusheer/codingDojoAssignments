from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author = []

    @classmethod
    def all_books(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES(%(title)s, %(num_of_pages)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_authors_favd_by_book(cls,id):
        data={"id":id}
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_book_by_id(cls, id):
        data = {"id":id}
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
