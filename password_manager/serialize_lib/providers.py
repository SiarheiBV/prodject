import csv
import openpyxl
from .errors import InvalidDataError


class BaseProvider:
    """
    NOT FOR CREATING OBJECTS!
    """

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value.split(".")[1] not in self.AVAILABLE_EXTENSIONS:
            print(value.split(".")[1])
            raise ValueError("Invalid file extension.")

        self._file_name = value


class ConvertDataMixin:
    def _convert_data(self, data):
        res = []
        res.append(list(data.keys()))
        if list(data.keys()) != res[0]:
            raise InvalidDataError("Can't serialize this data.")

        res.append(list(data.values()))

        return res


class CSVProvider(BaseProvider, ConvertDataMixin):
    AVAILABLE_EXTENSIONS = ('csv')

    def serialize(self, data):
        data_converted = self._convert_data(data)
        with open(self.file_name, "w") as file:
            writer = csv.writer(file, delimiter=",")
            for row in data_converted:
                writer.writerow(row)


class ExcelProvider(BaseProvider, ConvertDataMixin):
    AVAILABLE_EXTENSIONS = ('xlsx')

    def serialize(self, data):
        data_converted = self._convert_data(data)
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for row in data_converted:
            worksheet.append(row)
        workbook.save(self.file_name)


class TXTProvider(BaseProvider, ConvertDataMixin):
    AVAILABLE_EXTENSIONS = ('txt')

    def serialize(self, data):
        data_converted = self._convert_data(data)
        db = {}
        count = 0
        for i in range(len(data_converted[0])):
            db[data_converted[0][count]] = data_converted[1][count]
            count += 1
        with open(self.file_name, "w") as file:
            for key, value in db.items():
                file.write(f"{key} {value} \n")
