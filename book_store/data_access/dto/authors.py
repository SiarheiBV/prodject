from dataclasses import dataclass


@dataclass
class AuthorsDTO:
    name: str
    surname: str
    birth_date: str
    death_date: str
    information: str
