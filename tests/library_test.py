import unittest
import models.library as library
from models.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book = Book("The Platform Edge", "Mike Ashley", "fiction")

    def test_library_has_demo_data(self):
        self.assertTrue(len(library.library) > 3)

    def test_add_new_book(self):
        library.add_new_book(self.book)
        self.assertIn(self.book, library.library)

    def test_delete_book(self):
        book = library.library[3]
        library.delete_book(book)
        self.assertNotIn(book, library.library)