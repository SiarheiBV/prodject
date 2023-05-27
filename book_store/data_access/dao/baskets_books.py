from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseDAO
if TYPE_CHECKING:
    from dto import BasketsBooksDTO


class BasketsBooksDAO(BaseDAO):

    def create(self, data: BasketsBooksDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Baskets_Books (basket_id, book_id ) VALUES (?, ?);", (data.backets_id, data.books_id))
        self._db_gateway.connection.commit()
