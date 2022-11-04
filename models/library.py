from models.book import Book

# The 'Global Object Pattern'.
# https://python-patterns.guide/python/module-globals/

# library: set[Book] = set()
library = []

library.append(Book("Equal Rites", "Terry Pratchett", "fantasy", True))
library.append(Book("The Art Of Statistics", "David Spiegelhalter", "popular mathematics", True))
library.append(Book("Flatterland", "Ian Stewart", "popular mathematics"))
library.append(Book("Mother Tongue: The English Language", "Bill Bryson", "language & reference"))
library.append(Book("The Joy of Abstraction", "Eugenia Cheng", "popular mathematics", True))
library.append(Book("The Periodic Table", "Primo Levi", "fiction"))
library.append(Book("The Secret Agent", "Joseph Conrad", "fiction"))

def add_new_book(book: Book):
    library.append(book)

def delete_book(book: Book):
    library.remove(book)