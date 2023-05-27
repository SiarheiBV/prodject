from __future__ import annotations
from data_access.dto import UsersRolesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RandomChoiceProvider


class UsersRolesFactory:
    def __init__(self, users_id_provider: RandomChoiceProvider, roles_id_provider: RandomChoiceProvider) -> None:
        self._users_id_provider = users_id_provider
        self._roles_id_provider = roles_id_provider

    def generate(self) -> UsersRolesDTO:
        return UsersRolesDTO(users_id=self._users_id_provider(), roles_id=self._roles_id_provider())
