from __future__ import annotations
from data_access.dto import CitiesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import CitiesProvider, RandomChoiceProvider


class CitiesFactory:
    def __init__(self, cities_provider: CitiesProvider, country_id_provider: RandomChoiceProvider) -> None:
        self._cities_provider = cities_provider
        self._country_id_provider = country_id_provider

    def generate(self) -> CitiesDTO:
        return CitiesDTO(name=self._cities_provider(), country_id=self._country_id_provider())
