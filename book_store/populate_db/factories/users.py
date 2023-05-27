from __future__ import annotations
from data_access.dto import UsersDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (NameProvider,
                                   SurnameProvider,
                                   NiknameProvider,
                                   EmailProvider,
                                   AgeProvider,
                                   PasswordProvider,
                                   PhoneProvider
                                   )


class UsersFactory:
    def __init__(self,
                 name_provider: NameProvider,
                 surname_provider: SurnameProvider,
                 nikname_provider: NiknameProvider,
                 email_provider: EmailProvider,
                 age_provider: AgeProvider,
                 password_provider: PasswordProvider,
                 phone_provider: PhoneProvider
                 ) -> None:

        self._name_provider = name_provider
        self._surname_provider = surname_provider
        self._nikname_provider = nikname_provider
        self._email_provider = email_provider
        self._age_provider = age_provider
        self._password_provider = password_provider
        self._phone_provider = phone_provider

    def generate(self) -> UsersDTO:
        return UsersDTO(name=self._name_provider(),
                        surname=self._surname_provider(),
                        username=self._nikname_provider(),
                        email=self._email_provider(),
                        age=self._age_provider(),
                        password=self._password_provider(),
                        phone=self._phone_provider()
                        )
