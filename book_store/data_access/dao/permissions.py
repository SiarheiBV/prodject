from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import PermissionsDTO


class PermissionsDAO(BaseDAO):

    def create(self, data: PermissionsDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Permissions (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Permissions;")
        return result.fetchall()
