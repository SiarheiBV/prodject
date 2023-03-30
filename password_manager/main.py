from faker import Faker
from datetime import datetime
# import csv
from validators import validate_user_choice
from errors import IncorrectUserInputError

try:
    found_flag = open("data/flag.txt")
    print("флаг найден")
except FileNotFoundError:
    # первый запуск
    creat_flag = open("data/flag.txt", "w")

    def gen_word():
        fake = Faker()
        secret_word = fake.word()
        print("remember the word:", secret_word)
        return secret_word
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
            pass

        if choice == "2":
            pass

        if choice == "3":
            pass

        if choice == "4":
            pass

        if choice == "5":
            pass


main()
