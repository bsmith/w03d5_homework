from flask import Blueprint, request, render_template, url_for, redirect

from models.book import Book
from models.library import library, add_new_book, delete_book

# Blueprints! https://flask.palletsprojects.com/en/2.2.x/blueprints/
books = Blueprint("books", __name__)

@books.route('/books')
def books_list():
    return render_template("books_list.html.j2", title="All Books", books_list=library)

@books.route('/books/<int:index>')
def books_single(index: int):
    if index >= len(library):
        # 404 error instead?
        raise ValueError("books_single received index out of range of library")
    book = library[index]
    return render_template("books_single.html.j2", title="View Book", book=book, index=index)

@books.route('/books', methods=['POST'])
def books_create():
    # form validation
    book_data = {
        'title': request.form['title'],
        'author': request.form['author'],
        'genre': request.form['genre']
    }

    # build object
    new_book = Book(**book_data)
    library.append(new_book)
    new_index = len(library) - 1
    return redirect(url_for('books.books_single', index=new_index))

@books.route('/books/<int:index>/delete', methods=['POST'])
def books_delete(index: int):
    delete_book(library[index])
    return redirect(url_for('books.books_list'))
