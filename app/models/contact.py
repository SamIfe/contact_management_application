from datetime import datetime
from bson import ObjectId
from .phone_number import PhoneNumber
from .email import Email
from .address import Address


class Contact:
    def __init__(self, first_name, last_name, display_name = None, profile_photo_url=None):
        self.id = ObjectId()
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = f"{first_name} {last_name}"
        self.profile_photo_url = profile_photo_url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.phone_numbers = []
        self.emails = []
        self.addresses = []
        self.group_ids = []


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def merge_with(self, other_contact):
        if other_contact.created_at < self.created_at:
            self.created_at = other_contact.created_at

        for phone in other_contact.phone_numbers:
            if not any(p.number == phone.number for p in self.phone_numbers):
                self.phone_numbers.append(phone)

        for address in other_contact.addresses:
            if not any(a.format() == address.format() for a in self.addresses):
               self.addresses.append(address)

        for group_id in other_contact.group_ids:
            if group_id not in self.group_ids:
                self.group_ids.append(group_id)

        self.updated_at = datetime.now()


    def add_phone_number(self, phone_number):
        if not isinstance(phone_number, PhoneNumber):
            raise TypeError("Expected phone number object")

        if phone_number.is_primary:
            for phone in self.phone_numbers:
                if phone.is_primary:
                    phone_number.is_primary = False
        self.phone_numbers.append(phone_number)
        self.updated_at = datetime.now()


    def add_email(self, email):
        if not isinstance(email, Email):
            raise TypeError("Expected email object")

        if email.is_primary:
            for email in self.emails:
                if email.is_primary:
                    email.is_primary = False

        self.emails.append(email)
        self.updated_at = datetime.now()

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Expected address object")

        if address.is_primary:
            for address in self.addresses:
                if address.is_primary:
                    address.is_primary = False

        self.addresses.append(address)
        self.updated_at = datetime.now()


    def add_to_group(self, group):
        if group.id not in self.group_ids:
            self.group_ids.append(group.id)
            self.updated_at = datetime.now()


    def remove_from_group(self, group):
        if group.id not in self.group_ids:
            self.group_ids.append(group.id)
            self.updated_at = datetime.now()


    def to_document(self):
        return{
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "display_name": self.display_name,
            "profile_photo_url": self.profile_photo_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "phone_numbers": self.phone_numbers,
            "emails": self.emails,
            "addresses": self.addresses,
            "group_ids": self.group_ids,
        }


    @classmethod
    def from_document(cls, document):
        contact = cls(
            first_name=document["first_name"],
            last_name=document["last_name"],
            display_name=document["display_name"],
            profile_photo_url=document["profile_photo_url"],
        )

        contact.id = document["id"]
        contact.created_at = document["created_at"]
        contact.updated_at = document["updated_at"]

        contact.phone_numbers = [PhoneNumber.from_dict(phone) for phone in document.get("phone_numbers", [])]

        contact.emails = [Email.from_dict(email) for email in document.get("emails", [])]

        contact.addresses = [Address.from_dict(address) for address in document.get("addresses", [])]

        contact.group_ids = document.get("group_ids", [])

        return contact





