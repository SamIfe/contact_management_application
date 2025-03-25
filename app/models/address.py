from datetime import datetime
from .enum import AddressType


class Address:
    def __init__(self, street, city, state, postal_code, country,
                 type=AddressType.ADDRESS, is_primary=False):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.type = type
        self.is_primary = is_primary
        self.created_at = datetime.now()


    def format(self ):
        return f"{self.street} {self.city} {self.state} {self.postal_code} {self.country}"


    def to_dict(self):
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "postal_code": self.postal_code,
            "country": self.country,
            "type": self.type,
            "is_primary": self.is_primary,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["street"],
            data["city"],
            data["state"],
            data["postal_code"],
            data["country"],
            data["type"],
            data["is_primary"],
           data.get("created at", datetime.now)
        )
