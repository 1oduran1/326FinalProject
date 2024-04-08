"""Contact Management application code
Olivia Durán, Alison Wu, """

class Phonebook:
  """ An application for Contact Management and phone book logging
  
    Attributes:
          name (str): the user's name.
          
          contacts (dict of str: Contact): dictionary where keys are the contact
          name and values are their contact information
          
          book (list of contacts): list of contact objects that the user 
          communicates with
  """
  def __init__ (self, name):
    """ Initalize new Phonebook objects.

    Args:
        name (str): the user's name.

    Side effects:
        sets attributes name, contacts, and book
    """
    self.name = name
    self.contacts = dict()
    self.book = list()

  def add_contact(self, contact):
    """ Add contact to contacts.
        
        Args:
            contact (Phonebook): Phonebook log of a contact to add
    """
    self.contacts[contact.name] = contact