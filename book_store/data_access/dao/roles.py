from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import RolesDTO


class RolesDAO(BaseDAO):

    def create(self, data: RolesDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Roles (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Roles;")
        return result.fetchall()
