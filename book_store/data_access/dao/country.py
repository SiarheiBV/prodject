from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import CountryDTO


class CountryDAO(BaseDAO):

    def create(self, data: CountryDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Countries (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Countries;")
        return result.fetchall()
