from models.book import Book

# The 'Global Object Pattern'.
# https://python-patterns.guide/python/module-globals/

# library: set[Book] = set()

class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_new_book(self, book: Book):
        if book.accession_id is None:
            self.books.append(book)
            book.update_accession_id(len(self.books) - 1)

    def delete_book(self, book: Book):
        self.books.remove(book)
        book.remove_accession_id()

    def count_books(self):
        return len(self.books)

    def get_all_books(self):
        return [*self.books]

library = Library("The CodeClan Library")

library.add_new_book(Book("Equal Rites", "Terry Pratchett", "fantasy", True))
library.add_new_book(Book("The Art Of Statistics", "David Spiegelhalter", "popular mathematics", True))
library.add_new_book(Book("Flatterland", "Ian Stewart", "popular mathematics"))
library.add_new_book(Book("Mother Tongue: The English Language", "Bill Bryson", "language & reference"))
library.add_new_book(Book("The Joy of Abstraction", "Eugenia Cheng", "popular mathematics", True))
library.add_new_book(Book("The Periodic Table", "Primo Levi", "fiction"))
library.add_new_book(Book("The Secret Agent", "Joseph Conrad", "fiction"))
