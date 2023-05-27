from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import AddressDTO


class AddressDAO(BaseDAO):

    def create(self, data: AddressDTO) -> None:
        self._db_gateway.cursor.execute(
            "INSERT INTO Addresses (city_id, street, house_number, postal_code, user_id) VALUES (?,?,?,?,?);",
            (data.city_id, data.street, data.house_number, data.postal_code, data.user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Addresses;")
        return result.fetchall()
