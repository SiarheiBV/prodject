from __future__ import annotations
from data_access.dto import BooksDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.provider import (BooksProvider,
                                   AuthorProvider,
                                   PageProvider,
                                   PriceProvider,
                                   FormatProvider,
                                   RandomIntProvider,
                                   AgeRestrictionProvider,
                                   InfoProvider
                                   )


class BooksFactory:
    def __init__(self,
                 title_provider: BooksProvider,
                 price_provider: PriceProvider,
                 descriptions_provider: InfoProvider,
                 author_provider: AuthorProvider,
                 pages_provider: PageProvider,
                 format_provider: FormatProvider,
                 age_restriction_provider: AgeRestrictionProvider,
                 available_provider: RandomIntProvider
                 ) -> None:

        self._title_provider = title_provider
        self._price_provider = price_provider
        self._descriptions_provider = descriptions_provider
        self._author_provider = author_provider
        self._pages_provider = pages_provider
        self._format_provider = format_provider
        self._age_restriction_provider = age_restriction_provider
        self._available_provider = available_provider

    def generate(self) -> BooksDTO:
        return BooksDTO(title=self._title_provider(),
                        price=self._price_provider(),
                        description=self._descriptions_provider(),
                        author=self._author_provider(),
                        pages=self._pages_provider(),
                        format=self._format_provider(),
                        age_restriction=self._age_restriction_provider(),
                        available=self._available_provider()
                        )
