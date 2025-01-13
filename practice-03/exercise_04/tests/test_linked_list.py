import unittest
from src.LinkedList import LinkedList
from src.Book import Book
from src.CompactDisk import CompactDisk


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.linked_list = LinkedList()

        cls.book1 = Book(
            title="Title 1",
            category="Category 1",
            base_price=100,
            author="Author 1",
            publication_date="01-01-2019",
            quantity_pages=100,
        )
        cls.book2 = Book(
            title="Title 2",
            category="Category 2",
            base_price=100,
            author="Author 2",
            publication_date="01-01-2005",
            quantity_pages=100,
        )
        cls.cd1 = CompactDisk(
            title="Title 3",
            category="Category 2",
            base_price=100,
            duration=240,
            narrator="Narrator 1",
        )
        cls.cd2 = CompactDisk(
            title="Title 4",
            category="Category 3",
            base_price=100,
            duration=180,
            narrator="Narrator 2",
        )

        cls.linked_list.add_post(cls.book1)
        cls.linked_list.add_post(cls.book2)
        cls.linked_list.add_post(cls.cd1)
        cls.linked_list.add_post(cls.cd2)

    def test_get_post_type(self):
        first_actual_post_type = self.linked_list.get_post_type(3)
        first_expected_post_type = "Book"

        self.assertEqual(first_expected_post_type, first_actual_post_type, "test_get_post_type")

        second_actual_post_type = self.linked_list.get_post_type(0)
        second_expected_post_type = "Compact Disk"

        self.assertEqual(second_expected_post_type, second_actual_post_type, "test_get_post_type")

        self.assertIsNone(self.linked_list.get_post_type(5), "test_get_post_type")

    def test_get_items_quantity(self):
        (actual_books_quantity, actual_compact_disk_quantity) = self.linked_list.get_items_quantity()
        self.assertEqual(2, actual_books_quantity)
        self.assertEqual(2, actual_compact_disk_quantity)

    def test_show_post_data(self):
        self.linked_list.show_post_data()


if __name__ == '__main__':
    unittest.main()
