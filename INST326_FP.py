import csv
import sys
import argparse
"""Contact Management application code
Olivia Durán, Alison Wu, Alex Yang, Binta sanyang """

class Contact():
    """A class that represents a contact.

    Attributes:
        name (str): name of the contact
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
        
    def add_contact(self, name, address, phone, email): #Olivia
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
        
    def remove_contact(self, name): #Binta
        """ Removes a contact from the phonebook.

        Args:
            name: The name of the contact to remove. """
        if name in self.contacts:
            del self.contacts[name]
                
    def search_contact(self, name): #Binta
        """ Searches for a contact by name and returns their phone number.

        Args: name: The name of the contact to search for.

        Returns: The phone number of the contact if found, otherwise a message indicating 
        the contact is not found.
        """
        if name in self.contacts:
            print(f"Name: {name} Address: {self.contacts[name][0]} Phone: {self.contacts[name][1]} Email: {self.contacts[name][2]}")
        else:
            print(f"Contact {name} not found in phonebook.")
        

    def update_contact(self, name, new_number): # Alison
        """ Updates the phone number of an existing contact.
        
        Args:
            name (str): Name of the contact to update.
            new_number (str): New phone number to set.
             
        Returns:
            str: A message indicating the result of the operation."""
        
        if name in self.contacts:
            self.contacts[name] = (self.contacts[name][0], new_number, self.contacts[name][2])
            print(f"Contact '{name}' updated successfully with new phone number: {new_number}.")
        else:
            print(f"Contact '{name} could not be found in the phonebook.")
        
    def get_contact_count(self): #Alison
        """Get the total number of contacts in the phonebook.

        Returns:
            int: Total number of contacts.
        """
        print(len(self.contacts))
        
    def get_all_contacts(self): #Olivia
        """ Shows full contact list.
            
            Args: None
            
            Side effects: None
        """
        for name, information in self.contacts.items():
            print(f"Name: {name} Address: {information[0]} Phone: {information[1]} Email: {information[2]}")
    
    def clear_all_contacts(self): #Alex
    #Deletes all contacts from the phonebook if the user chooses this option
        self.contacts.clear()

    def export_to_file(self):
        """Writes out the contents of the phonebook to a csv file named 'phonebook.csv'."""
        with open('phonebook.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name', 'Address', 'Phone', 'Email'])  # Write header row
            for key, value in self.contacts.items():
                writer.writerow([key, *value])

def main():
    """Run the Phonebook methods based on what the user chooses.

    Args:
        None

    Returns:
        float or int: the area of the square.
    """
    p = Phonebook()
    run = True
    while run:
        print('Menu:\n'
         '1. add contact\n'
         '2. remove contact\n'
         '3. search contact\n'
         '4. update contact\n'
         '5. get all contacts\n'
         '6. get contact count\n'
         '7. clear all contacts\n'
         '8. export contacts to csv file\n')
        menu_input = input('Please input the item number you want. ')
        if menu_input == '1':
            name_input = input('Contact name? ')
            address_input = input('Contact address? ')
            phone_input = input('Contact phone? ')
            email_input = input('Contact email? ')
            p.add_contact(name_input, address_input, phone_input, email_input)
        if menu_input == '2':
            delete_input = input('Name of contact to delete: ')
            p.remove_contact(delete_input)
        if menu_input == '3':
            search_input = input('Name of contact you want to search: ')
            p.search_contact(search_input)
        if menu_input == '4':
            update_input = input('Name of contact you want to update: ')
            new_phone = input('New number of contact:')
            p.update_contact(update_input, new_phone)
        if menu_input == '5':
            p.get_all_contacts()
        if menu_input == '6':
            p.get_contact_count()
        if menu_input == '7':
            p.clear_all_contacts()
        if menu_input == '8':
            p.export_to_file()
        loop_input = input('Run again? y/n: ')
        if loop_input.lower() == 'y':
            pass
        if loop_input.lower() == 'n':
            run = False
            quit

if __name__ == '__main__':
    main()
