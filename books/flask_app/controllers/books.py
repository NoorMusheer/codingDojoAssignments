from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask import render_template, redirect, request

@app.route('/books')
def all_books():
    books = Book.all_books()
    return render_template('all_books.html', all_books = books)

@app.route('/add_fav_book/<int:id>', methods=['POST'])
def add_fav_book(id):
    data = {
        "book_id" : request.form['book_id'],
        "author_id" : id
    }
    Author.add_to_favs(data)
    return redirect('/author_show/' + str(id))

@app.route('/add_book', methods=['POST'])
def add_book():
    data = {
        "title" : request.form['title'],
        "num_of_pages" : request.form['num_of_pages']
    }
    Book.add_book(data)
    return redirect('/books')

@app.route('/favorited_books/<int:id>')
def favorited_books(id):
    favd_book = Book.get_book_by_id(id)
    authors_by_book = Book.get_authors_favd_by_book(id)
    all_authors = Author.all_authors()
    return render_template("book_show.html", favd_book = favd_book, authors = authors_by_book, all_authors = all_authors)

