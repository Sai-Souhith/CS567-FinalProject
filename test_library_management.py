import unittest
from datetime import datetime, timedelta
from library_management import Book, Library

class TestBook(unittest.TestCase):
    def test_check_out(self):
        book = Book("001", "1984", "George Orwell", "9780451524935")
        book.check_out()
        self.assertTrue(book.is_checked_out)
        self.assertIsNotNone(book.due_date)

    def test_check_in(self):
        book = Book("001", "1984", "George Orwell", "9780451524935")
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)
        self.assertIsNone(book.due_date)

    def test_str_representation(self):
        book = Book("001", "1984", "George Orwell", "9780451524935")
        self.assertEqual(str(book), "001: 1984 by George Orwell, ISBN: 9780451524935")

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("001", "1984", "George Orwell", "9780451524935")
        self.book2 = Book("002", "To Kill a Mockingbird", "Harper Lee", "9780060935467")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn("001", self.library.books)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book("001")
        self.assertNotIn("001", self.library.books)

    def test_find_book(self):
        self.library.add_book(self.book1)
        found_book = self.library.find_book("001")
        self.assertEqual(found_book, self.book1)

    def test_check_out_book(self):
        self.library.add_book(self.book1)
        self.library.check_out_book("001")
        self.assertTrue(self.book1.is_checked_out)

    def test_check_in_book(self):
        self.library.add_book(self.book1)
        self.library.check_out_book("001")
        self.library.check_in_book("001")
        self.assertFalse(self.book1.is_checked_out)

    # def test_list_books(self):
    #     self.library.add_book(self.book1)
    #     self.library.add_book(self.book2)
    #     #expected_output = "001: 1984 by George Orwell, ISBN: 9780451524935 - Available\n" \
    #                       #"002: To Kill a Mockingbird by Harper Lee, ISBN: 9780060935467 - Available\n"
    #     self.assertEqual(self.library.list_books(), "expected_output")

if __name__ == '__main__':
    unittest.main()
