from __future__ import annotations
from data_access.dto import RolesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import RolesProvider


class RolesFactory:
    def __init__(self, roles_provider: RolesProvider) -> None:
        self._roles_provider = roles_provider

    def generate(self) -> RolesDTO:
        return RolesDTO(name=self._roles_provider())
