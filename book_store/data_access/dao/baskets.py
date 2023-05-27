from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BasketsDTO


class BasketsDAO(BaseDAO):

    def create(self, data: BasketsDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Baskets (user_id, status) VALUES (?, ?);", (data.users_id, data.status))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Baskets;")
        return result.fetchall()
