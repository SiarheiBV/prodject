from faker import Faker
from datetime import datetime
from validators import validate_user_choice
from errors import IncorrectUserInputError
from business_logic import (add_new_password,
                            get_identifier,
                            get_password,
                            del_password,
                            get_all_records
                            )
from providers import provide_db
from encoding import Cripto
from config import TYPE_JSON, PLIST, KEY

try:
    found_flag = open("data/flag.txt")
except FileNotFoundError:
    # первый запуск
    creat_flag = open("data/flag.txt", "w")

    def gen_word(N) -> str:
        fake = Faker()
        passphrase = fake.word()
        print("remember the word:", passphrase.upper())
        return passphrase
    word = gen_word()
    creat_flag.write(f"{word} - {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("work programm")


def main() -> None:
    print("Choose action from menu\n"
          "0 - Exit\n"
          "1 - Added new password\n"
          "2 - Get password list\n"
          "3 - Get specific password\n"
          "4 - Delete password\n"
          "5 - Export password"
          )
    while True:

        choice = input("Your choice: ").strip()

        try:
            validate_user_choice(choice)

        except IncorrectUserInputError as err:
            print(err)
            continue

        if choice == "0":
            break

        if choice == "1":
            identifier = input("Enter password identifier: ").lower().strip()
            password = input("Enter password: ").lower().strip()
            print(add_new_password(identifier, password, provide_db(TYPE_JSON, PLIST), Cripto(KEY)))

        if choice == "2":
            get_identifier(provide_db(TYPE_JSON, PLIST))

        if choice == "3":
            identifier = input("Enter password identifier: ").lower().strip()
            print(get_password(identifier, provide_db(TYPE_JSON, PLIST), Cripto(KEY)))

        if choice == "4":
            identifier = input("Enter password identifier: ").lower().strip()
            passphrase = input("Enter passphrase: ").lower().strip()
            print(del_password(identifier, passphrase, provide_db(TYPE_JSON, PLIST)))

        if choice == "5":
            passphrase = input("Enter passphrase: ").lower().strip()
            extension = input("Enter csv, txt, xlsx: ").lower().strip()
            print(get_all_records(passphrase, extension, provide_db(TYPE_JSON, PLIST), Cripto(KEY)))


if __name__ == "__main__":
    main()
