from datetime import datetime
from bson import ObjectId

class Group:
    def __init__(self, name, description=None):
        self._id = ObjectId()
        self._name = name
        self._description = description
        self.contact_ids = []
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def add_contact(self, contact):
        if contact._id not in self.contact_ids:
            self.contact_ids.append(contact._id)
            self.updated_at = datetime.now()

    def remove_contact(self, contact):
        if contact._id not in self.contact_ids:
            self.contact_ids.remove(contact._id)
            self.updated_at = datetime.now()


    def rename(self, new_name):
        self._name = new_name
        self.updated_at = datetime.now()


    def delete(self):
        self.deleted = True
        self.updated_at = datetime.now()


    @classmethod
    def to_document(cls, document):
        group = cls(
            name=document['name'],
            description=document['description']
        )

        group._id = document['_id']
        group.contact_ids = document['contact_ids']
        group.created_at = document['created_at']
        group.updated_at = document['updated_at']

        return group
