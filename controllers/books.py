from flask import Blueprint, request, render_template, url_for, redirect

from models.book import Book
from models.library import library

# Blueprints! https://flask.palletsprojects.com/en/2.2.x/blueprints/
books = Blueprint("books", __name__)

@books.route('/books')
def books_list():
    return render_template("books_list.html.j2", title="All Books", books_list=library.get_all_books())

@books.route('/books/<int:accession_id>')
def books_single(accession_id: int):
    book = library.find_book_by_accession_id(accession_id)
    if book is None:
        # 404 error instead?
        raise ValueError("accession_id not found")
    return render_template("books_single.html.j2", title="View Book", book=book)

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
    library.add_new_book(new_book)
    new_accession_id = new_book.accession_id
    return redirect(url_for('books.books_single', accession_id = new_accession_id))

@books.route('/books/<int:accession_id>/delete', methods=['POST'])
def books_delete(accession_id: int):
    book = library.find_book_by_accession_id(accession_id)
    if book is None:
        raise ValueError("accession_id not found")
    library.delete_book(book)
    return redirect(url_for('books.books_list'))

@books.route('/books/<int:accession_id>/checkoutin', methods=['POST'])
def books_checkoutin(accession_id: int):
    book = library.find_book_by_accession_id(accession_id)
    if book is None:
        raise ValueError("accession_id not found")
    if request.form['direction'] == "in":
        book.check_in()
    elif request.form['direction'] == "out":
        book.check_out()
    else:
        raise ValueError("unknown direction")
    print(request.form['next_page'])
    # if ('next_page' in request.form and
    #         request.form['next_page'] in ['books.books_list', 'books.books_single']):
    #     return redirect(url_for(request.form['next_page'], index=index))
    if 'next_page' in request.form and request.form['next_page'] == 'books.books_single':
        return redirect(url_for('books.books_single', accession_id=accession_id))
    else:
        return redirect(url_for('books.books_list'))
