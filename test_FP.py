"""unit tests (for methods and functions with no output):
unit test for add_contact
unit test for remove_contact
unit test for update_contact
unit test for clear_all_contacts
unit test for main"""

from INST326_FP import Phonebook
import unittest

#unit test for main
class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()
        
    def test_add_contact(self):
        self.phonebook.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com")
        self.assertTrue("John Doe" in self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts["John Doe"], ("123 Main St", "555-1234", "john@example.com"))