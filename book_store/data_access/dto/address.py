from dataclasses import dataclass


@dataclass
class AddressDTO:
    city_id: int
    street: str
    house_number: int
    postal_code: str
    user_id: int
