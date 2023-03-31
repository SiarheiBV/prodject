from typing import TypeAlias
from provider import (NameProvider,
                      BankCardProvider,
                      PhoneProvider,
                      EmailProvider
                      )


CL: TypeAlias = NameProvider | BankCardProvider | PhoneProvider | EmailProvider


class FakeFactory:
    def __init__(self, provider: CL, count: int) -> None:
        if count <= 0:
            raise ValueError('Count must be greater than zero')
        self.provider = provider
        self.count = count

    def generate(self) -> str:
        return self.provider.generate()

    def __iter__(self) -> 'FakeFactory':
        return self

    def __next__(self) -> str:
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return self.generate()


# Example usage
fake_1 = FakeFactory(PhoneProvider(), 5)
fake_2 = FakeFactory(NameProvider(), 3)
fake_3 = FakeFactory(BankCardProvider(), 2)
fake_4 = FakeFactory(EmailProvider(), 7)
for email in fake_4:
    print(email)
