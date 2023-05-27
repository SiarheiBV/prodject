from __future__ import annotations
from data_access.dto import BooksGenresDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RandomChoiceProvider


class BooksGenresFactory:
    def __init__(self, genres_id_provider: RandomChoiceProvider, book_id_provider: RandomChoiceProvider, ) -> None:
        self._genres_id_provider = genres_id_provider
        self._book_id_provider = book_id_provider

    def generate(self) -> BooksGenresDTO:
        return BooksGenresDTO(genres_id=self._genres_id_provider(), book_id=self._book_id_provider())
