from __future__ import annotations
from data_access.dto import AuthorsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (NameProvider,
                                   SurnameProvider,
                                   DateProvider,
                                   InfoProvider
                                   )


class AuthorsFactory:
    def __init__(self, name_provider: NameProvider,
                 surname_provider: SurnameProvider,
                 b_date_provider: DateProvider,
                 d_date_provider: DateProvider,
                 info_provider: InfoProvider) -> None:

        self._name_provider = name_provider
        self._surname_provider = surname_provider
        self._b_date_provider = b_date_provider
        self._d_date_provider = d_date_provider
        self._info_provider = info_provider

    def generate(self) -> AuthorsDTO:
        return AuthorsDTO(name=self._name_provider(),
                          surname=self._surname_provider(),
                          birth_date=self._b_date_provider(),
                          death_date=self._d_date_provider(),
                          information=self._info_provider()
                          )
