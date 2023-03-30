class Contact:
    def __init__(self, first_name: str, last_name: str, phone: str, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f" NAME: {self.first_name} {self.last_name}\n PHONE: {self.phone}\n EMAIL: {self.email}"

    def _valid_name(self, value: str) -> None:
        if not value.istitle:
            raise ValueError("must start with a capital letter")
        if len(value) not in range(5, 16):
            raise ValueError("length must be between 5 and 15 characters")

    def _valid_email(self, value: str) -> None:
        email = value.split("@")
        if len(email) != 2:
            raise ValueError("Email must contains only one @.")

        if email[1] not in ["gmail.com", "yandex.ru", "ya.ru", "yahoo.com"]:
            raise ValueError("Unsupported email provider.")

    def _valid_phone(self, value: str) -> None:
        if value[0] != "+":
            raise ValueError("number must start from +")

        if not value[1:].isdigit():
            raise ValueError("number incorrect")

        if value[1:4] not in ("375", "374") and value[1:3] != "48":
            raise ValueError("code must be start from 375 or 374 or 48")

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._valid_name(value)
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._valid_name(value)
        self._last_name = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._valid_phone(value)
        self._phone = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._valid_email(value)
        self._email = value


contact = Contact("Siarhei", "Baradauka", "+48451567081", "Borodavkasv666@gmail.com")
print(contact)
