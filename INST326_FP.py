"""Contact Management application code
Olivia Durán, Alison Wu, Alex Yang, """

class Contact():
    """A class that represents a contact.

    Attributes:
        first_name (str): first name of the contact
        last_name (str): last name of the contact
        address (str): address of the contact
        phone (str): phone number of the contact
        email (str): email of the contact
    """
    def __init__(self, name, address, phone, email) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

class Phonebook():
    """ An application for Contact Management and phone book logging

    Attributes:
        contacts (dict of str: Contact): dictionary where keys are the contact
        name and values are their contact information   
    """
    def __init__ (self):
        """ Initalize new Phonebook objects.
        Args:
            None

        Side effects:
            sets contacts attribute
        """
        self.contacts = dict()

    def add_contact(self, name, address, phone, email):
        """ Add contact to contacts.
            
            Args:
                name (str): name of contact
                address (str): address of contact
                phone (str): phone number of contact
                email (str): email of contact
                
            Side effects: 
                creates Contact object and adds contact information to
            contacts dictionary
        """
        contact = Contact(name, address, phone, email)
        self.contacts[contact.name] = (contact.address, contact.phone, contact.email)
    
    def show(self):
        """ Shows full contact list.
            
            Args: None
            
            Side effects: None
        """
        return self.contacts
    
"""def main():
    Will prompt the user to either add a contact, look up an existing contact, 
    look up the entire phonebook, delete a contact, modify an existing contact,
    or return the entire phonebook.
"""

"""def search():
    a function that can search the contacts dictionary and present the user with
    the specific contact and contact information they are looking for.
"""

"""unit tests:
test 1: checks if contact objects are properly created
test 2: checks if Phone book objects are created
test 3: checks if contacts are added
test 4: checks that search function returns correct information
    edge cases would be typos"""