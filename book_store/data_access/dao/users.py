from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import UsersDTO


class UsersDAO(BaseDAO):

    def create(self, data: UsersDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Users (name, surname, user_name, email, age, password, phone) VALUES (?,?,?,?,?,?,?);",
                                        (data.name, data.surname, data.username, data.email, data.age, data.password, data.phone))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Users;")
        return result.fetchall()
