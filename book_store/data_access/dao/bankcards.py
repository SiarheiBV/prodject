from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BankCardsDTO


class BankCardsDAO(BaseDAO):

    def create(self, data: BankCardsDTO) -> None:
        self._db_gateway.cursor.execute(
            "INSERT INTO BankCards (card_number, first_name, last_name, cvc_code, expiration_month_year, user_id) VALUES (?,?,?,?,?,?);",
            (data.card_number, data.first_name, data.last_name, data.cvc_code, data.expiration_month_year, data.user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM BankCards;")
        return result.fetchall()
