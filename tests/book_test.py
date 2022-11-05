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

    def test_check_out(self):
        self.book.check_out()
        self.assertTrue(self.book.checked_out)

    def test_check_in(self):
        self.book.check_out()
        self.assertTrue(self.book.checked_out)
        self.book.check_in()
        self.assertFalse(self.book.checked_out)

    def test_get_accession_id_none_by_default(self):
        self.assertIsNone(self.book.get_accession_id())

    def test_update_accession_id(self):
        self.book.update_accession_id(123)
        self.assertEqual(123, self.book.get_accession_id())
    
    def test_remove_accession_id(self):
        self.book.update_accession_id(123)
        self.assertEqual(123, self.book.get_accession_id())
        self.book.remove_accession_id()
        self.assertIsNone(self.book.get_accession_id())
