"""unit tests (for methods and functions with no output):
unit test for add_contact
unit test for remove_contact
unit test for update_contact
unit test for clear_all_contacts"""

from INST326_FP import Phonebook
import unittest

#unit test for add_contact
class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_contact(self):
        # Test adding a contact
        self.phonebook.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com")
        self.assertTrue("John Doe" in self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts["John Doe"], ("123 Main St", "555-1234", "john@example.com"))

        # Test adding another contact
        self.phonebook.add_contact("Jane Smith", "456 Oak St", "555-5678", "jane@example.com")
        self.assertTrue("Jane Smith" in self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts["Jane Smith"], ("456 Oak St", "555-5678", "jane@example.com"))