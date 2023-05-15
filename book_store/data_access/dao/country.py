from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import DBGateWayProtocol
    from dto import CountryDTO


class CountryDAO:
    def __init__(self, db_gateway: DBGateWayProtocol) -> None:
        self._db_gateway = db_gateway

    def create(self, data: CountryDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO Countries (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()
