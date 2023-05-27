from __future__ import annotations
from data_access.dto import BooksAuthorsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RandomChoiceProvider


class BooksAuthorsFactory:
    def __init__(self, authors_id_provider: RandomChoiceProvider, books_id_provider: RandomChoiceProvider) -> None:
        self._authors_id_provider = authors_id_provider
        self._books_id_provider = books_id_provider

    def generate(self) -> BooksAuthorsDTO:
        return BooksAuthorsDTO(authors_id=self._authors_id_provider(), books_id=self._books_id_provider(), )
