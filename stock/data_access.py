import json


class IStorage:

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value.split(".")[1] not in self.AVAILABLE_EXTENSIONS:
            raise ValueError("Invalid file extension.")

        self._file_name = value


class JSONStorage(IStorage):
    AVAILABLE_EXTENSIONS = ('json')

    def read_file(self):
        with open(self.file_name, "r+", encoding="utf-8") as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.file_name, "w+", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
