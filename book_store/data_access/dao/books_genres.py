from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BooksGenresDTO


class BooksGenresDAO(BaseDAO):

    def create(self, data: BooksGenresDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Books_Genres (genres_id, book_id ) VALUES (?, ?);", (data.genres_id, data.book_id))
        self._db_gateway.connection.commit()
