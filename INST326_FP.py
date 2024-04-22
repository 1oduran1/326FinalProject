import csv
"""Contact Management application code
Olivia Durán, Alison Wu, Alex Yang, Binta sanyang """

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

    def remove_contact(name): #Binta
        """ Removes a contact from the phonebook.

        Args:
            name: The name of the contact to remove. """
        if name in phonebook:
                del phonebook[name]
                
    
    def search_contact(name): #Binta
        """ Searches for a contact by name and returns their phone number.

        Args: name: The name of the contact to search for.

        Returns: The phone number of the contact if found, otherwise a message indicating 
        the contact is not found.
        """
        if name in phonebook:
            return phonebook[name]
        else:
            return f"Contact {name} not found in phonebook."

    def update_contact(self, name, new_number): # Alison
        """ Updates the phone number of an existing contact.
        
        Args:
            name (str): Name of the contact to update.
            new_number (str): New phone number to set.
             
        Returns:
            str: A message indicating the result of the operation."""
        
        if name in self.contacts:
            self.contacts[name] = (self.contacts[name][0], new_number, self.contacts[name][2])
            return (f"Contact '{name}' updated successfully with new phone number: {new_number}.")
        else:
            return (f"Contact '{name} could not be found in the phonebook.")
        
    def get_contact_count(self): #Alison
        """Get the total number of contacts in the phonebook.

        Returns:
            int: Total number of contacts.
        """
        return len(self.contacts)
        
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



"""if name = __main__"""

"""parse_args"""
