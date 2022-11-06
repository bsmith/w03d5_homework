import unittest
from models.library import library
from models.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book = Book("The Platform Edge", "Mike Ashley", "fiction")

    def test_library_has_demo_data(self):
        self.assertTrue(library.count_books() > 3)

    def test_library_get_all_books_returns_list(self):
        all_books = library.get_all_books()
        self.assertIsInstance(all_books, list)

    def test_add_new_book(self):
        library.add_new_book(self.book)
        self.assertIn(self.book, library.get_all_books())

    def test_add_new_book__allocates_correct_accession_id(self):
        all_accession_ids = [book.accession_id for book in library.get_all_books()]
        book_to_delete = library.get_all_books()[3]
        library.delete_book(book_to_delete)
        library.add_new_book(self.book)
        self.assertIsNotNone(self.book.accession_id)
        self.assertNotIn(self.book.accession_id, all_accession_ids)

    def test_delete_book(self):
        book = library.get_all_books()[3]
        library.delete_book(book)
        self.assertNotIn(book, library.get_all_books())

    def test_find_book_by_accession_id(self):
        book = library.get_all_books()[3]
        book2 = library.find_book_by_accession_id(book.get_accession_id())
        self.assertIs(book, book2)