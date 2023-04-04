from serialize_lib import (Serializer,
                           CSVProvider,
                           ExcelProvider,
                           TXTProvider
                           )
from typing import Any


def add_new_password(identifier: str, password: str, connector: Any, encode: Any) -> str:

    try:
        data = connector.read_file()
    except FileNotFoundError:
        data = {"passphrase": input("enter passphrase: ")}

    if identifier not in data:
        data[identifier] = encode.encryption(password)
        connector.write_file(data)
        return "Password added"
    else:
        choice = input("identifier already exists, update password? y/n: ")
        if choice == "y":
            data[identifier] = encode.encryption(password)
            connector.write_file(data)
            return "Password update"
        return "repeat input"


def get_identifier(connector: Any) -> None:
    data = connector.read_file()
    for identifier in data.keys():
        print(identifier)


def get_password(identifier: str, connector: Any, encode: Any) -> str:
    data = connector.read_file()

    if identifier not in data:
        return "there is no such entry in the database"
    else:
        passphrase = input("Enter passphrase: ")
        if passphrase == data["passphrase"]:
            return encode.decoding(data[identifier])
        else:
            return "invalid input"


def del_password(identifier: str, passphrase: str, connector: Any) -> str:
    data = connector.read_file()

    if identifier not in data:
        return "there is no such entry in the database"
    else:
        if passphrase == data["passphrase"]:
            del data[identifier]
            connector.write_file(data)
            return "delete"
        else:
            return "invalid input"


def get_all_records(passphrase: str, extension: str, connector: Any, encode: Any) -> str:
    data = connector.read_file()

    if data["passphrase"] != passphrase:
        return "invalid input"
    else:
        del data["passphrase"]
        data_decode = {}
        for key, value in data.items():
            data_decode[key] = encode.decoding(value)
        if extension == "txt":
            serialize = Serializer(TXTProvider("data/password.txt"))
            serialize.execute(data_decode)
        if extension == "csv":
            serialize = Serializer(CSVProvider("data/password.csv"))
            serialize.execute(data_decode)
        if extension == "xlsx":
            serialize = Serializer(ExcelProvider("data/password.xlsx"))
            serialize.execute(data_decode)
        return "File already"
