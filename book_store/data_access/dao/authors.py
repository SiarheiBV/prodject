from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import AuthorsDTO


class AuthorsDAO(BaseDAO):

    def create(self, data: AuthorsDTO) -> None:
        self._db_gateway.cursor.execute(
            "INSERT INTO Authors (name, surname, birth_date, death_date, information) VALUES (?,?,?,?,?);",
            (data.name, data.surname, data.birth_date, data.death_date, data.information))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Authors;")
        return result.fetchall()
