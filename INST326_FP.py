import csv
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
    
    def clear_all_contacts(self): #Alex
    #Deletes all contacts from the phonebook if the user chooses this option
        self.clear()

    def export_to_file(self): #Alex
        #Writes out the contents of the phonebook to a csv file named "phonebook.csv"
        with open('phonebook.csv', 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in self.items():
                writer.writerow([key, value])
        

"""def main():
    Will prompt the user to either add a contact, look up an existing contact, 
    delete a contact, update an existing contact, return all contacts
    get the number of contacts, delete all contacts, or export the contacts to a file.
"""

#def add_contact(name, number): Olivia DONE

#def remove_contact(name): Binta

#def search_contact(name): Binta

#def update_contact(name, new_number): Alison

#def get_all_contacts(): Olivia

#def get_contact_count(): Alison







"""def search():
    a function that can search the contacts dictionary and present the user with
    the specific contact and contact information they are looking for.
"""

"""unit tests (for methods and functions with no output):
unit test for add_contact
unit test for remove_contact
unit test for update_contact
unit test for clear_all_contacts"""