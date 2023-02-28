class EmptyLibraryError(Exception):
    pass


class Book:
    def __init__(self, name, description, pages, author, price):
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "pages": self.pages,
            "author": self.author,
            "price": self.price
        }

    def contains_word(self, word):
        if word in self.name.lower() or word in self.description.lower():
            return True
        return False

    def __lt__(self, other):
        return self.page < other.page

    def __gt__(self, other):
        return self.page > other.page

    def __le__(self, other):
        return self.page <= other.page

    def __ge__(self, other):
        return self.page >= other.page

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


class Library:

    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def get_books(self):
        return [book.to_dict() for book in self.book]

    def remove_book(self, book):
        self.book.remove(book)

    def find_the_biggest_book(self):
        if not self.book:
            raise EmptyLibraryError("this book is not on the list")
        return max(self.book, key=lambda book: book.pages).to_dict()

    def __len__(self):
        return len(self.book)


book1 = Book("1984", "Some description", 500, "Orwell", 10)
book2 = Book("Learn Python", "This book will teach you how to learn python", 1000, "Luhts", 49)


lib = Library()
lib.add_book(book1)
lib.add_book(book2)
print(lib.get_books())
print(lib.find_the_biggest_book())
print(len(lib))
