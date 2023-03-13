from time import time
import re


class Censored:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        new_value = re.sub(r'\b[fF][uU][cC][kK]\b', '****', value)
        setattr(instance, self.name, new_value)


class Message:
    text = Censored()

    def __init__(self, text):
        self.text = text
        self.__created_at = time()

    def __str__(self):
        return f"{self.text}"


class Song:
    name = Censored()
    author = Censored()

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.__created_at = time()

    def __str__(self):
        return f"{self.author}: {self.name}"


song_text = """Fuck the police, fuck
fuck-Fuck the police, fuck, fuck
Fuck the police, fuck the, fuck the
Fuck the police"""


song = Song("Fuck the police", "N.W.A")
print(song)
print()
message_1 = Message(song_text)
print(message_1)
