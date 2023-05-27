from __future__ import annotations
from data_access.dto import BankCardsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (RandomChoiceProvider,
                                   BankCardProvider,
                                   NameProvider,
                                   SurnameProvider,
                                   CVCProvider,
                                   ExpirationProvider
                                   )


class BankCardFactory:
    def __init__(self, cart_number_provider: BankCardProvider,
                 first_name_provider: NameProvider,
                 last_name_provider: SurnameProvider,
                 cvc_code_provider: CVCProvider,
                 expiration_provider: ExpirationProvider,
                 user_id_provider: RandomChoiceProvider
                 ) -> None:

        self._cart_number_provider = cart_number_provider
        self._first_name_provider = first_name_provider
        self._last_name_provider = last_name_provider
        self._cvc_code_provider = cvc_code_provider
        self._expiration_provider = expiration_provider
        self._user_id_provider = user_id_provider

    def generate(self) -> BankCardsDTO:
        return BankCardsDTO(card_number=self._cart_number_provider(),
                            first_name=self._first_name_provider(),
                            last_name=self._last_name_provider(),
                            cvc_code=self._cvc_code_provider(),
                            expiration_month_year=self._expiration_provider(),
                            user_id=self._user_id_provider())
