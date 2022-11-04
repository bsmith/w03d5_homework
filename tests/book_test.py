from unittest import TestCase

from models.book import Book

class TestBook(TestCase):
    def setUp(self):
        self.book = Book("The Platform Edge", "Mike Ashley", "fiction")

    def test_book_has_title(self):
        self.assertEqual("The Platform Edge", self.book.title)

    def test_book_has_author(self):
        self.assertEqual("Mike Ashley", self.book.author)

    def test_book_has_genre(self):
        self.assertEqual("fiction", self.book.genre)

    def test_book_is_checked_in_by_default(self):
        self.assertFalse(self.book.checked_out)