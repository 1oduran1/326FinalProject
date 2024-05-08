"""unit tests (for methods and functions with no output):
unit test for add_contact
unit test for remove_contact
unit test for clear_all_contacts
use 'pytest -s  test_FP.py' to test tests"""

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
        
    def test_add_another_contact(self):
        self.phonebook.add_contact("Samantha Purdue", "501 Arctic St", "222-9876", "sam@example.com")
        self.assertTrue("Samantha Purdue" in self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts["Samantha Purdue"], ("501 Arctic St", "222-9876", "sam@example.com"))
        
    def test_remove_contact(self):
        self.phonebook.remove_contact("John Doe")
        self.assertFalse("John Doe" in self.phonebook.contacts)

    def test_clear_all_contacts(self):
        self.phonebook.clear_all_contacts()
        self.assertEqual(len(self.phonebook.contacts), 0)
        self.assertEqual(self.phonebook.contacts, {})