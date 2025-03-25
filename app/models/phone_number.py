import re
from datetime import datetime
from .enum import PhoneType


class PhoneNumber:
    def __init__(self, number, type=PhoneType.MOBILE, is_primary=False):
        self.number = number
        self.type = type
        self.is_primary = is_primary
        self.created_at = datetime.now()


    def format_number(self):
        cleaned_number = re.sub(r'\D', '', self.number)
        if len(cleaned_number) == 11:
            return f"({cleaned_number[:3]} {cleaned_number[3:6]}){cleaned_number[6:]})"
        return self.number

    def validate(self):
        cleaned_number = re.sub(r'\D', '', self.number)
        return len(cleaned_number) >= 11 and cleaned_number.isdigit()


    def to_dict(self):
        return{
            "number": self.number,
            "type": self.type.name,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["number"],
            data["type"],
            data["is_primary"],
            data.get("created_at", datetime.now())
        )

