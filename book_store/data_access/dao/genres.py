from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import GenresDTO


class GenresDAO(BaseDAO):

    def create(self, data: GenresDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Genres (name, description) VALUES (?, ?);", (data.name, data.decriptions))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Genres;")
        return result.fetchall()
