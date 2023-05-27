from __future__ import annotations
from data_access.dto import PermissionsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import PermissionsProvider


class PermissionsFactory:
    def __init__(self, permissions_provider: PermissionsProvider) -> None:
        self._permissions_provider = permissions_provider

    def generate(self) -> PermissionsDTO:
        return PermissionsDTO(name=self._permissions_provider())
