from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask import render_template, redirect, request

@app.route('/')
def index():
    authors = Author.all_authors()
    return render_template("index.html", authors = authors)

@app.route('/add_author', methods=['POST'])
def add_author():
    data = {
        'name' : request.form['name']
    }
    Author.add_author(data)
    return redirect('/')

@app.route('/author_show/<int:id>')
def author_show(id):
    books = Book.all_books()
    author_info = Author.get_author_by_id(id)
    author_favs = Author.get_fav_books_by_author(id)
    return render_template("author_show.html", author = author_info, author_favs = author_favs, all_books = books)

@app.route('/add_fav_auth/<int:id>', methods=['POST'])
def add_fav_auth(id):
    print("----------ID ---------")
    print(id)
    data ={
        "book_id" : id,
        "author_id" : request.form['author_id']
    }
    print(data)
    Author.add_to_favs(data)
    return redirect ('/favorited_books/'+ str(id))