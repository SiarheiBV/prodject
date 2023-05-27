from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import TransactionsDTO


class TransactionsDAO(BaseDAO):

    def create(self, data: TransactionsDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Transactions (basket_id, bank_card_id, amount, address_id) VALUES (?,?,?,?);",
                                        (data.basket_id,
                                         data.bankcard_id,
                                         data.amount,
                                         data.address_id)
                                        )
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Transactions;")
        return result.fetchall()
