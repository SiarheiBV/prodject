from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from data_access import RecordsList, RecordsList2


class StorageProto(Protocol):
    def read_file(self) -> 'RecordsList' | 'RecordsList2':
        raise NotImplementedError

    def write_file(self, data: 'RecordsList' | 'RecordsList2') -> None:
        raise NotImplementedError
