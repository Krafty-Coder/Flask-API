import unittest
import json
from app.book_model import Book


class BookModelTestCase(unittest.TestCase):
    """
    This test dwells more on the book model
    """
    def setUp(self):
        """Instantiating book object"""
        self.book_model = Book()

    def test_should_return_all_the_books(self):
        response = self.book_model.view_all_available_books('/api/book/')
        self.assertEqual(response.status, 200)

    def test_should_return_one_business(self):
        response = self.book_model.get_a_particular_book('/api/book/1')
        self.assertEqual(response.status, 200)

    def test_should_delete_business(self):
        response = self.book_model.delete_book('api/book/2')
        self.assertEqual(response.status, 200)

    def test_add_a_book(self):
        response = self.book_model.add_book('api/book/2')
        self.assertEqual(response.status, 200)

