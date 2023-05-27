from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import RolesPermDTO


class RolesPermDAO(BaseDAO):

    def create(self, data: RolesPermDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Roles_Permissions (role_id, permission_id ) VALUES (?, ?);", (data.roles_id, data.perm_id))
        self._db_gateway.connection.commit()
