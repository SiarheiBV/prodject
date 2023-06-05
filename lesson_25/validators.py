from errors import IncorrectUserInputError
import sqlite3


def validate_user_choice(choice: str) -> None:
    if not choice.isdigit():
        raise IncorrectUserInputError("you entered an invalid value, re-enter")
    if choice not in map(str, range(0, 7)):
        raise IncorrectUserInputError("Please correct choice")


def validate_id(user_id):
    connetion = sqlite3.connect("book_store.db")
    cursor = connetion.cursor()
    cursor.execute("SELECT id FROM Users")
    data = cursor.fetchall()
    user_id = int(user_id)
    flag = False
    for item in data:
        if item[0] == int(user_id):
            flag = True
            break
        else:
            flag = False
            continue
    if not flag:
        raise IncorrectUserInputError("this's ID no in list")
    cursor.close()
    connetion.close()
