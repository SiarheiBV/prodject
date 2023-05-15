import random
import string


class EmailProvider:
    def __call__(self) -> str:
        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for _ in range(10))
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', "yandex.ru", "mail.ru"])
        return f'{username}@{domain}'


class PhoneProvider:
    def __call__(self) -> str:
        digits = ''.join(random.choice(string.digits) for _ in range(7))
        prefix = ["33", "25", "29"]
        return f'+375({random.choice(prefix)}) {digits[:3]}-{digits[3:5]}-{digits[5:]}'


class BankCardProvider:
    def __call__(self) -> str:
        digits = ''.join(random.choice(string.digits) for _ in range(16))
        return f'{digits[:4]}-{digits[4:8]}-{digits[8:12]}-{digits[12:]}'


class NameProvider:
    first_names = ["David", "Angus", "Mike", "John", "Chris", "Billy", "Chuck", "Jimi", "John", "Kirk"]
    last_names = ["Bowie", "Lennon", "Johnson", "Lee", "Brown", "Young", "Gibbons", "Berry", "Hendrix", "Lennon", "Hammett"]

    def __call__(self) -> str:
        return f'{random.choice(self.first_names)} {random.choice(self.last_names)}'


class CountryProvider:

    country_names = ["Belarus", "Poland", "Albania", "Argentina", "Austria",
                     "Belgium", "China", "Canada", "Costa Rica", "Egypt", "Estonia",
                     "Germany", "Greece", "Haiti", "Hungary", "Indonesia",
                     "Jamaica", "Japan", "Lebanon", "Malaysia", "Mexico", "Mongolia",
                     "Morocco", "Panama", "Peru", "Philippines", "Slovakia", "Slovenia",
                     "Sweden", "Syria", "Ukraine", "USA", "Uzbekistan", "Yemen"]

    def __call__(self) -> str:
        return random.choice(self.country_names)
