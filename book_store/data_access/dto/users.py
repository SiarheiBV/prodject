from dataclasses import dataclass


@dataclass
class UsersDTO:
    name: str
    surname: str
    username: str
    email: str
    age: int
    password: str
    phone: str
