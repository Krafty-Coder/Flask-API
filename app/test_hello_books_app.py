from books import Book
import unittest


class BookMethodsTest(unittest.TestCase):
    def setUp(self):
        self.book_test = Book('Me', 'Peter', 676, 'Longhorn')
        self.book_test2 = Book('Think Like Me', 'Krafty', 315, 'Oxford')

    def test_correct_book_title(self):
        self.assertEqual(self.book_test.title, 'Me', msg="Bad title")
        self.assertEqual(self.book_test2.title, 'Think Like Me', msg="Bad title")

    def test_correct_author_name(self):
        self.assertEqual(self.book_test.author, 'Peter', msg="Error on author book name")
        self.assertEqual(self.book_test2.author, 'Krafty', msg="Error on author book name")

    def test_correct_book_number(self):
        self.assertEqual(self.book_test.book_number, 676, msg="Error on book number")
        self.assertEqual(self.book_test2.book_number, 315, msg="Error on book number")

    def test_correct_publisher_name(self):
        self.assertEqual(self.book_test.publisher, 'Longhorn', msg="Error on publisher name")
        self.assertEqual(self.book_test2.publisher, 'Oxford', msg="Error on publisher name")


