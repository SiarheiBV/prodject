from serialize_lib import (Serializer,
                           CSVProvider,
                           ExcelProvider,
                           TXTProvider
                           )


def add_new_password(identifier, password, connector):

    try:
        data = connector.read_file()
    except FileNotFoundError:
        data = {"passphrase": input("enter passphrase: ")}

    if identifier not in data:
        data[identifier] = password
        connector.write_file(data)
        return "Password added"
    else:
        choice = input("identifier already exists, update password? y/n: ")
        if choice == "y":
            data[identifier] = password
            connector.write_file(data)
            return "Password update"
        return


def get_identifier(connector):
    data = connector.read_file()
    for identifier in data.keys():
        print(identifier)


def get_password(identifier, connector):
    data = connector.read_file()

    if identifier not in data:
        return "there is no such entry in the database"
    else:
        passphrase = input("Enter passphrase: ")
        if passphrase == data["passphrase"]:
            print(data[identifier])
        else:
            print("invalid input")


def del_password(identifier, passphrase, connector):
    data = connector.read_file()

    if identifier not in data:
        return "there is no such entry in the database"
    else:
        if passphrase == data["passphrase"]:
            del data[identifier]
            connector.write_file(data)
            print("delete")
        else:
            print("invalid input")


def get_all_records(passphrase, extension, connector):
    data = connector.read_file()

    if data["passphrase"] != passphrase:
        print("invalid input")
    else:
        del data["passphrase"]
        if extension == "txt":
            serialize = Serializer(TXTProvider("data/password.txt"))
            serialize.execute(data)
        if extension == "csv":
            serialize = Serializer(CSVProvider("data/password.csv"))
            serialize.execute(data)
        if extension == "xlsx":
            serialize = Serializer(ExcelProvider("data/password.xlsx"))
            serialize.execute(data)

    """5. Экспортировать все пароли - запрашиваем кодовую фразу и название файла (доступные форматы excel, csv, txt, xml) и если она подходит и файл с нужным расширением,
то записываем в этот файл все пароли в расшифрованном виде их идентификаторы."""
