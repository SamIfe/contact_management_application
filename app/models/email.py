from datetime import datetime
from .enum import EmailType
import re

class Email:
    def __init__(self, address, type=EmailType.PERSONAL, is_primary=False):
        self.address = address
        self.type = type
        self.is_primary = is_primary
        self.created_at = datetime.now()

    def validate(self):
        email_regex_filter = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex_filter, self.address))


    def to_dict(self):
        return {
            'address': self.address,
            'type': self.type.name,
            'is_primary': self.is_primary,
            'created_at': self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['address'],
            data['type'],
            data['is_primary'],
            data.get('created_at', datetime.now())
        )



