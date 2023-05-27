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


class CVCProvider:

    def __call__(self) -> str:
        return random.randint(100, 1000)


class ExpirationProvider:

    def __call__(self) -> str:
        return f"0{random.randint(1, 32)}/{random.randint(23,33)}"


class CountryProvider:

    country_names = ["Belarus", "Poland", "Albania", "Argentina", "Austria",
                     "Belgium", "China", "Canada", "Costa Rica", "Egypt", "Estonia",
                     "Germany", "Greece", "Haiti", "Hungary", "Indonesia",
                     "Jamaica", "Japan", "Lebanon", "Malaysia", "Mexico", "Mongolia",
                     "Morocco", "Panama", "Peru", "Philippines", "Slovakia", "Slovenia",
                     "Sweden", "Syria", "Ukraine", "USA", "Uzbekistan", "Yemen"]

    def __call__(self) -> str:
        return random.choice(self.country_names)


class NameProvider:
    first_names = ["David", "Angus", "Mike", "John", "Chris", "Billy", "Chuck", "Jimi", "John", "Kirk"]

    def __call__(self) -> str:
        return random.choice(self.first_names)


class SurnameProvider:
    last_names = ["Bowie", "Lennon", "Johnson", "Lee", "Brown", "Young", "Gibbons", "Berry", "Hendrix", "Lennon", "Hammett"]

    def __call__(self) -> str:
        return random.choice(self.last_names)


class DateProvider:

    def __call__(self) -> str:
        return f"{random.randint(1,32)}.{random.randint(1,13)}.{random.randint(1850,1975)}"


class InfoProvider:

    letters = string.ascii_letters

    def __call__(self) -> str:
        rand_string = "".join(random.choice(self.letters) for _ in range(65))
        return rand_string


class NicknameProvider:

    nik_list = ["Beast", "Brave Spirit", "Chieftain", "Flame Host", "Flowers Lover", "Football Onlooker", "Gutsy Heart",
                "Help Bringer", "Caring Householder", "Hawk", "Lucky Guy", "Gold Cartel", "Gold Cartel",
                "Free Fire", "Pugilist", "Funny Bunny", "Secret Player", "Sunshine", "Tender Lionet", "Detector",
                "Muffin", "Fire Dragon", "Rock Star", "Charming Actor", "Sweet Peach", "Сool Fire", "Black Eagle", "Cuddly", "Cloud"]

    def __call__(self) -> str:
        return random.choice(self.nik_list)


class AgeProvider:

    def __call__(self) -> str:
        return random.randint(10, 60)


class PasswordProvider:

    letters = string.ascii_letters

    def __call__(self) -> str:
        password = "".join(random.choice(self.letters) for _ in range(8))
        return password


class RolesProvider:

    roles_list = ["seller", "buyer", "administrator", "manager", "customer", "admin", "owner", "support specialist"]

    def __call__(self) -> str:
        return random.choice(self.roles_list)


class PermissionsProvider:

    permissions = ["read-goods", "update-description", "admin-page"]

    def __call__(self) -> str:
        return random.choice(self.permissions)


class BooksProvider:

    books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice",
             "The Catcher in the Rye", "Animal Farm", "Lord of the Flies", "Brave New World",
             "The Hobbit", "The Chronicles of Narnia", "Harry Potter and the Sorcerer's Stone",
             "The Da Vinci Code", "The Alchemist", "The Lord of the Rings", "The Little Prince",
             "Alice's Adventures in Wonderland", "The Odyssey", "Moby-Dick", "Jane Eyre",
             "The Grapes of Wrath", "The Adventures of Huckleberry Finn", "Wuthering Heights",
             "Don Quixote", "Crime and Punishment", "Gone with the Wind", "The Kite Runner",
             "The Divine Comedy", "The Picture of Dorian Gray", "Frankenstein", "To the Lighthouse",
             "Catch-22", "The Scarlet Letter", "One Hundred Years of Solitude", "The Count of Monte Cristo",
             "The Great Expectations", "The Old Man and the Sea", "The Sound and the Fury", "Les Misérables",
             "War and Peace", "Pippi Longstocking", "Anna Karenina", "The Adventures of Tom Sawyer",
             "David Copperfield", "The Secret Garden", "The Jungle Book", "A Tale of Two Cities",
             "The Sun Also Rises", "Little Women", "The Brothers Karamazov", "The Iliad", "The Metamorphosis",
             "The Gruffalo", "The Giving Tree", "The Hitchhiker's Guide to the Galaxy", "The Handmaid's Tale",
             "The Hunger Games", "The Girl with the Dragon Tattoo", "The Color Purple", "The Outsiders",
             "The Hobbit", "The Chronicles of Narnia", "Harry Potter and the Sorcerer's Stone", "The Da Vinci Code",
             "The Alchemist", "The Lord of the Rings", "The Little Prince", "Alice's Adventures in Wonderland",
             "The Odyssey", "Moby-Dick", "Jane Eyre", "The Grapes of Wrath", "The Adventures of Huckleberry Finn",
             "Wuthering Heights", "Don Quixote", "Crime and Punishment", "Gone with the Wind", "The Kite Runner",
             "The Divine Comedy", "The Picture of Dorian Gray", "Frankenstein", "To the Lighthouse", "Catch-22",
             "The Scarlet Letter", "One Hundred Years of Solitude", "The Count of Monte Cristo", "The Great Expectations",
             "The Old Man and the Sea", "The Sound and the Fury", "Les Misérables", "War and Peace", "Pippi Longstocking",
             "Anna Karenina", "The Adventures of Tom Sawyer", "David Copperfield", "The Secret Garden", "The Jungle Book",
             "A Tale of Two Cities", "The Sun Also Rises", "Little Women", "The Brothers Karamazov", "The Iliad",
             "The Metamorphosis", "The Gruffalo", "The Giving Tree", "The Hitchhiker's Guide to the Galaxy",
             "The Handmaid's Tale", "The Hunger Games", "The Girl with the Dragon Tattoo", "The Color Purple", "The Outsiders"]

    def __call__(self) -> str:
        return random.choice(self.books)


class AuthorsProvider:

    authors = ["Harper Lee", "George Orwell", "F. Scott Fitzgerald", "Jane Austen", "J.D. Salinger", "George Orwell",
               "William Golding", "Aldous Huxley", "J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "Dan Brown",
               "Paulo Coelho", "J.R.R. Tolkien", "Antoine de Saint-Exupéry", "Lewis Carroll", "Homer", "Herman Melville",
               "Charlotte Brontë", "John Steinbeck", "Mark Twain", "Emily Brontë", "Miguel de Cervantes", "Fyodor Dostoevsky",
               "Margaret Mitchell", "Khaled Hosseini", "Dante Alighieri", "Oscar Wilde", "Mary Shelley", "Virginia Woolf",
               "Joseph Heller", "Nathaniel Hawthorne", "Gabriel Garcia Marquez", "Alexandre Dumas", "Charles Dickens",
               "Ernest Hemingway", "William Faulkner", "Victor Hugo", "Leo Tolstoy", "Astrid Lindgren", "Leo Tolstoy",
               "Mark Twain", "Charles Dickens", "Frances Hodgson Burnett", "Rudyard Kipling", "Charles Dickens",
               "Ernest Hemingway", "Louisa May Alcott", "Fyodor Dostoevsky", "Homer", "Franz Kafka", "Julia Donaldson",
               "Shel Silverstein", "Douglas Adams", "Margaret Atwood", "Suzanne Collins", "Stieg Larsson", "Alice Walker",
               "S.E. Hinton", "J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "Dan Brown", "Paulo Coelho", "J.R.R. Tolkien",
               "Antoine de Saint-Exupéry", "Lewis Carroll", "Homer", "Herman Melville", "Charlotte Brontë", "John Steinbeck",
               "Mark Twain", "Emily Brontë", "Miguel de Cervantes", "Fyodor Dostoevsky", "Margaret Mitchell", "Khaled Hosseini",
               "Dante Alighieri", "Oscar Wilde", "Mary Shelley", "Virginia Woolf", "Joseph Heller", "Nathaniel Hawthorne",
               "Gabriel Garcia Marquez", "Alexandre Dumas", "Charles Dickens", "Ernest Hemingway", "William Faulkner", "Victor Hugo",
               "Leo Tolstoy", "Astrid Lindgren", "Leo Tolstoy", "Mark Twain", "Charles Dickens", "Frances Hodgson Burnett", "Rudyard Kipling",
               "Charles Dickens", "Ernest Hemingway", "Louisa May Alcott", "Fyodor Dostoevsky", "Homer", "Franz Kafka", "Julia Donaldson",
               "Shel Silverstein", "Douglas Adams", "Margaret Atwood", "Suzanne Collins", "Stieg Larsson", "Alice Walker", "S.E. Hinton"]

    def __call__(self) -> str:
        return random.choice(self.authors)


class PriceProvider:

    def __call__(self) -> float:
        return round(random.uniform(10.5, 250.7), 2)


class PageProvider:

    def __call__(self) -> float:
        return random.randint(50, 450)


class FormatProvider:

    format = ["Softcover/Paperback", "Hardcover/Hardback", "Spiral-bound", "Leatherbound", "Clothbound", "Board Book", "Quarter-bound/Half-bound"]

    def __call__(self) -> str:
        return random.choice(self.format)


class AgeRestrictionProvider:

    age_restriction = ["0+", "3+", "6+", "9+", "12+", "14+", "18+"]

    def __call__(self) -> str:
        return random.choice(self.age_restriction)


class RandomIntProvider:

    def __call__(self) -> float:
        return random.randint(1, 50)


class GenresProvider:

    genres = ["Fantasy", "Science Fiction", "Mystery", "Romance", "Thriller", "Horror", "Historical Fiction", "Biography",
              "Non-fiction", "Young Adult",  "Children's", "Adventure", "Crime", "Drama", "Comedy", "Poetry"]

    def __call__(self) -> str:
        return random.choice(self.genres)


class RandomChoiceProvider:

    def __init__(self, value: list[int]) -> None:
        self._value = value

    def __call__(self) -> int:
        random_choice = random.choice(self._value)
        return random_choice[0]


class StatusProvider:

    status = ["Empty Cart", "Active Cart", "Checkout", "Order Placed", "Paid", "Shipped", "Delivered", "Return", "Completed"]

    def __call__(self) -> str:
        return random.choice(self.status)


class CitiesProvider:

    cities = ["New York", "London", "Paris", "Tokyo", "Sydney", "Berlin", "Moscow", "Rome", "Dubai", "Toronto", "Madrid",
              "Vienna", "Amsterdam", "Beijing", "Athens", "Cairo", "Stockholm", "Prague", "Barcelona", "Seoul", "Helsinki", "Lisbon",
              "Dublin", "Oslo", "Warsaw", "Budapest", "Singapore", "Istanbul", "Mumbai", "Bangkok", "Copenhagen", "Brussels", "Zurich",
              "Melbourne", "Rio de Janeiro", "Cape Town", "Los Angeles", "Vancouver", "Montreal", "San Francisco", "Chicago", "Sydney",
              "Seattle", "Boston", "Dublin", "Austin", "Dallas", "Denver", "Atlanta", "Miami", "Houston", "Phoenix", "Philadelphia",
              "Las Vegas", "New Orleans", "Honolulu", "Portland", "Stockholm", "Oslo", "Helsinki", "Copenhagen", "Reykjavik", "Berlin",
              "Munich", "Hamburg", "Frankfurt", "St. Petersburg", "Lisbon", "Barcelona", "Madrid", "Milan", "Rome", "Venice", "Athens",
              "Moscow", "Dubai", "Mumbai", "Delhi", "Kolkata", "Beijing", "Shanghai", "Tokyo", "Kyoto", "Sydney", "Melbourne", "Brisbane",
              "Perth", "Auckland", "Wellington", "Vancouver", "Toronto", "Montreal", "Calgary", "Mexico City", "São Paulo", "Buenos Aires", "Santiago"
              ]

    def __call__(self) -> str:
        return random.choice(self.cities)


class AddressProvider:

    streets = ["Main Street", "Park Avenue", "Broadway", "Oxford Street", "Abbey Road", "Fifth Avenue", "Wall Street", "Champs-Élysées",
               "Rodeo Drive", "Lombard Street", "Bourbon Street", "Sesame Street", "Baker Street", "Downing Street", "Kingsway", "Rue de Rivoli",
               "Sunset Boulevard", "Regent Street", "Bond Street", "Portobello Road", "Bourke Street", "George Street", "Orchard Road", "Nathan Road",
               "Elm Street", "Ginza", "Hollywood Boulevard", "Canal Street", "Savile Row", "Fleet Street", "Rue du Faubourg Saint-Honoré",
               "Haight Street", "Piccadilly", "Times Square", "Kurfürstendamm", "Via Veneto", "Carnaby Street", "Rue de la Paix", "Khaosan Road"
               ]

    def __call__(self) -> str:
        return random.choice(self.streets)


class PostCodeProvider:

    def __call__(self) -> float:
        return random.randint(100000, 1000000)
