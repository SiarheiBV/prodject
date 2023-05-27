from __future__ import annotations
from data_access.dto import BasketsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (RandomChoiceProvider,
                                   StatusProvider
                                   )


class BasketsFactory:
    def __init__(self, user_id_provider: RandomChoiceProvider,
                 status_provider: StatusProvider) -> None:

        self._user_id_provider = user_id_provider
        self._status_provider = status_provider

    def generate(self) -> BasketsDTO:
        return BasketsDTO(users_id=self._user_id_provider(),
                          status=self._status_provider())
