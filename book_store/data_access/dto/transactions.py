from dataclasses import dataclass


@dataclass
class TransactionsDTO:
    basket_id: int
    bankcard_id: int
    amount: int
    address_id: int
