"""Contact Management application code
Olivia Durán, Alison Wu"""

class Phonebook:
  """ An application for Contact Management and phone book logging
  
    Attributes:
          name (str): the user's name.
          contacts (dict of str: Contact): the list of contacts that the users communicates with.
  """
  def __init__ (self, name):
    """ Initalize new Phonebook objects.

    Attributes:
      Sets attributes to name, contacts, book .
    """
    self.name = name
    self.contacts = dict()
    self.book = list()

  def add_contact(self, contact):
    """ Add contact to contacts.
        
        Args:
            contact (Phonebook): Phonebook log of a contact to add
    """
