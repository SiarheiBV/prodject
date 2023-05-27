from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import CitiesDTO


class CitiesDAO(BaseDAO):

    def create(self, data: CitiesDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Cities (name, country_id ) VALUES (?, ?);", (data.name, data.country_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Cities;")
        return result.fetchall()
