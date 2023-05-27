from dataclasses import dataclass


@dataclass
class BankCardsDTO:
    card_number: str
    first_name: str
    last_name: str
    cvc_code: int
    expiration_month_year: str
    user_id: int
