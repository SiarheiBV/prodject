from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BooksAuthorsDTO


class BooksAuthorsDAO(BaseDAO):

    def create(self, data: BooksAuthorsDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Books_Authors (author_id, book_id ) VALUES (?, ?);", (data.authors_id, data.books_id))
        self._db_gateway.connection.commit()
