from __future__ import annotations
from data_access.dto import RolesPermDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RandomChoiceProvider


class RolesPermFactory:
    def __init__(self, roles_id_provider: RandomChoiceProvider, perm_id_provider: RandomChoiceProvider) -> None:
        self._roles_id_provider = roles_id_provider
        self._perm_id_provider = perm_id_provider

    def generate(self) -> RolesPermDTO:
        return RolesPermDTO(roles_id=self._roles_id_provider(), perm_id=self._perm_id_provider(), )
