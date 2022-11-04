from models.book import Book

# The 'Global Object Pattern'.
# https://python-patterns.guide/python/module-globals/

library: set[Book] = set()

library.add(Book("Equal Rites", "Terry Pratchett", "fantasy", True))
library.add(Book("The Art Of Statistics", "David Spiegelhalter", "popular mathematics", True))
library.add(Book("Flatterland", "Ian Stewart", "popular mathematics"))
library.add(Book("Mother Tongue: The English Language", "Bill Bryson", "language & reference"))
library.add(Book("The Joy of Abstraction", "Eugenia Cheng", "popular mathematics", True))
library.add(Book("The Periodic Table", "Primo Levi", "fiction"))
library.add(Book("The Secret Agent", "Joseph Conrad", "fiction"))
