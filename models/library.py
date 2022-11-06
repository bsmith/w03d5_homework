from models.book import Book

# The 'Global Object Pattern'.
# https://python-patterns.guide/python/module-globals/

# library: set[Book] = set()

class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_new_book(self, new_book: Book):
        if new_book.accession_id is None:
            if len(self.books) == 0:
                new_accession_id = 100
            else:
                new_accession_id = 1 + max([book.accession_id for book in self.books])
            new_book.update_accession_id(new_accession_id)
            self.books.append(new_book)

    def delete_book(self, book: Book):
        self.books.remove(book)
        book.remove_accession_id()

    def find_book_by_accession_id(self, accession_id: int):
        for book in self.books:
            if book.get_accession_id() == accession_id:
                return book
        return

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
