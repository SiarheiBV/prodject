from dataclasses import dataclass


@dataclass
class BooksDTO:
    title: str
    price: float
    description: str
    author: str
    pages: int
    format: str
    age_restriction: int
    available: int
