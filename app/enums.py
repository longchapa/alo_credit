from enum import Enum


class Product(str, Enum):
    PHONE = "PHONE"
    TWIST = "TWIST"
    CARD = "CARD"


class Decision(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
