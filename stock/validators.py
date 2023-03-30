from errors import IncorrectUserInputError


def validate_user_choice(choice: str) -> None:
    if not choice.isdigit():
        raise IncorrectUserInputError("you entered an invalid value, re-enter")
    if choice not in map(str, range(0, 7)):
        raise IncorrectUserInputError("Please correct choice")
