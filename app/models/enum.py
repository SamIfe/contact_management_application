from enum import Enum, auto

class PhoneType(Enum):
    MOBILE = auto()
    HOME = auto()
    WORK = auto()
    OTHER = auto()

class EmailType(Enum):
    PERSONAL = auto()
    WORK = auto()
    OTHER = auto()

class AddressType(Enum):
    HOME = auto()
    WORK = auto()
    OTHER = auto()
