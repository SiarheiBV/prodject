from __future__ import annotations
from data_access.dto import AddressDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (RandomChoiceProvider,
                                   PostCodeProvider,
                                   AddressProvider,
                                   RandomIntProvider
                                   )


class AddressFactory:
    def __init__(self, citi_id_provider: RandomChoiceProvider,
                 street_provider: AddressProvider,
                 house_number_provider: RandomIntProvider,
                 postal_code_provider: PostCodeProvider,
                 user_id_provider: RandomChoiceProvider) -> None:

        self._citi_id_provider = citi_id_provider
        self._street_provider = street_provider
        self._house_number_provider = house_number_provider
        self._postal_code_provider = postal_code_provider
        self._user_id_provider = user_id_provider

    def generate(self) -> AddressDTO:
        return AddressDTO(city_id=self._citi_id_provider(),
                          street=self._street_provider(),
                          house_number=self._house_number_provider(),
                          postal_code=self._postal_code_provider(),
                          user_id=self._user_id_provider())
