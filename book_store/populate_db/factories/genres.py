from __future__ import annotations
from data_access.dto import GenresDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import GenresProvider, InfoProvider


class GenresFactory:
    def __init__(self, genres_provider: GenresProvider, descriptions_provider: InfoProvider) -> None:
        self._genres_provider = genres_provider
        self._descriptions_provider = descriptions_provider

    def generate(self) -> GenresDTO:
        return GenresDTO(name=self._genres_provider(), decriptions=self._descriptions_provider())
