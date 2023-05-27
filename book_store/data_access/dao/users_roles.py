from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import UsersRolesDTO


class UsersRolesDAO(BaseDAO):

    def create(self, data: UsersRolesDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Users_Roles (user_id, role_id ) VALUES (?, ?);", (data.users_id, data.roles_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Users_Roles;")
        return result.fetchall()
