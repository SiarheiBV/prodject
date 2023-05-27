from __future__ import annotations
from data_access.dto import TransactionsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (RandomIntProvider,
                                   RandomChoiceProvider
                                   )


class TransactionsFactory:
    def __init__(self, basket_id_provider: RandomChoiceProvider,
                 bankcard_id_provider: RandomChoiceProvider,
                 amoutd_provider: RandomIntProvider,
                 address_id_provider: RandomChoiceProvider
                 ) -> None:

        self._basket_id_provider = basket_id_provider
        self._bankcard_id_provider = bankcard_id_provider
        self._amoutd_provider = amoutd_provider
        self._address_id_provider = address_id_provider

    def generate(self) -> TransactionsDTO:
        return TransactionsDTO(basket_id=self._basket_id_provider(),
                               bankcard_id=self._bankcard_id_provider(),
                               amount=self._amoutd_provider(),
                               address_id=self._address_id_provider()
                               )
