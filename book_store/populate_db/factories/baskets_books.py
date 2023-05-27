from __future__ import annotations
from data_access.dto import BasketsBooksDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RandomChoiceProvider


class BasketsBooksFactory:
    def __init__(self, baskets_id_provider: RandomChoiceProvider, books_id_provider: RandomChoiceProvider) -> None:
        self._baskets_id_provider = baskets_id_provider
        self._books_id_provider = books_id_provider

    def generate(self) -> BasketsBooksDTO:
        return BasketsBooksDTO(backets_id=self._baskets_id_provider(),
                               books_id=self._books_id_provider())
