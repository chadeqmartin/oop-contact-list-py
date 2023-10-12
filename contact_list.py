class ContactList:
    def __init__(self, name, contacts):
        self._name = name
        self._contacts = sorted(contacts, key=lambda c: c['name'])

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_contacts(self):
        return self._contacts
    
    @get_contacts.setter
    def set_contacts(self, contacts):
        self._contacts = contacts

    def add_contact(self, contact):
        contacts = self._contacts
        contacts.append(contact)
        self._contacts = sorted(contacts, key=lambda c: c['name'])

    def remove_contact(self, name):
        contacts = [cont for cont in self._contacts if cont['name'] != name]
        self._contacts = contacts
    
    def find_shared_contacts(self, list_two):
        shared_contacts = []
        for contact in self._contacts:
            if contact in list_two.get_contacts:
                shared_contacts.append(contact)

        return shared_contacts
    
coworkers = [
    {"name": "Missy", "number": "301-345-4567"},
    {"name": "Bob", "number": "301-332-7655"}
]
good_friends = [
    {"name": "Missy", "number": "301-345-4567"},
    {"name": "Betsy", "number": "301-885-9067"}
]

coworkers_list = ContactList("Coworkers' Contacts", coworkers)
friends_list = ContactList("Friends' Contacts", good_friends)

coworkers_who_are_friends_list = friends_list.find_shared_contacts(coworkers_list)

print(coworkers_who_are_friends_list)
    

    

    