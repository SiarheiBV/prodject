import random
import string


class EmailProvider:
    def generate(self):
        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for _ in range(10))
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', "yandex.ru", "mail.ru"])
        return f'{username}@{domain}'


class PhoneProvider:
    def generate(self):
        digits = ''.join(random.choice(string.digits) for _ in range(7))
        prefix = ["33", "25", "29"]
        return f'+375({random.choice(prefix)}) {digits[:3]}-{digits[3:5]}-{digits[5:]}'


class BankCardProvider:
    def generate(self):
        digits = ''.join(random.choice(string.digits) for _ in range(16))
        return f'{digits[:4]}-{digits[4:8]}-{digits[8:12]}-{digits[12:]}'


class NameProvider:
    first_names = ["David", "Angus", "Mike", "John", "Chris", "Billy", "Chuck", "Jimi", "John", "Kirk"]
    last_names = ["Bowie", "Lennon", "Johnson", "Lee", "Brown", "Young", "Gibbons", "Berry", "Hendrix", "Lennon", "Hammett"]

    def generate(self):
        return f'{random.choice(self.first_names)} {random.choice(self.last_names)}'
