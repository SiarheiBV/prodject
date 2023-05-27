from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BooksDTO


class BooksDAO(BaseDAO):

    def create(self, data: BooksDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Books (title, price, description, authors, pages, format, age_restriction, available) VALUES (?,?,?,?,?,?,?,?);",
                                        (data.title, data.price, data.description, data.author, data.pages, data.format, data.age_restriction, data.available))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM Books;")
        return result.fetchall()
