import sqlite3


connection = sqlite3.connect("book_store.db")
cursor = connection.cursor()


def get_users_list() -> list[str]:
    cursor.execute("SELECT id, name, surname,email, created_at FROM Users")
    data = cursor.fetchall()
    return data


def get_user_info(user_id: str) -> list[tuple]:
    cursor.execute("SELECT Users.id, Users.name, Users.surname, Users.email, Users.phone, Users.age, Users.created_at, Roles.name "
                   "FROM Users "
                   "JOIN Users_Roles "
                   "ON Users.id = Users_Roles.user_id "
                   "JOIN Roles "
                   "ON Users_Roles.role_id = Roles.id "
                   "WHERE Users.id=?", (user_id,))

    data = cursor.fetchall()
    return data


def update_user_email(user_id: str, email: str) -> None:
    cursor.execute("UPDATE Users SET email=? WHERE id = ?", (email, user_id))
    connection.commit()


def update_user_phone(user_id: str, phone: str) -> None:
    cursor.execute("UPDATE Users SET phone=? WHERE id = ?", (phone, user_id))
    connection.commit()


def get_books_list() -> list[tuple]:
    cursor.execute("SELECT id, title, pages, price, age_restriction, available FROM Books")
    data = cursor.fetchall()
    return data


def get_book_info(book_id: str) -> list[tuple]:
    cursor.execute("SELECT Books.id, Books.title, Books.age_restriction, Books.price, "
                   "Books.description, Books.pages, Books.format, Books.available, Books.created_at, Authors.name, Authors.surname, Genres.name "
                   "FROM Books "
                   "JOIN Books_Authors "
                   "ON Books.id = Books_Authors.book_id "
                   "JOIN Authors "
                   "ON Books_Authors.author_id = Authors.id "
                   "JOIN Books_Genres "
                   "ON Books.id = Books_Genres.book_id "
                   "JOIN Genres "
                   "ON Books_Genres.genres_id = Genres.id "
                   "WHERE Books.id=?", (book_id,))

    data = cursor.fetchall()
    return data


def delete_book(book_id: str) -> None:
    cursor.execute("DELETE FROM Books WHERE id=?", (book_id,))
    connection.commit()


def update_book_name(book_id: str, name: str) -> None:
    cursor.execute("UPDATE Books SET title=? WHERE id = ?", (name, book_id))
    connection.commit()


def get_authors_list() -> list[tuple]:
    cursor.execute("SELECT id, name, surname FROM Authors")
    data = cursor.fetchall()
    return data


def get_authors_info(author_id: str) -> list[tuple]:
    cursor.execute("SELECT id, name, surname, birth_date, death_date, information FROM Authors WHERE id=?", (author_id,))
    data = cursor.fetchall()
    return data


def get_transactions() -> list[tuple]:
    cursor.execute("SELECT Users.name, Users.surname, BankCards.card_number, "
                   "\"Transactions\".amount, \"Transactions\".created_at, Countries.name, Cities.name, Addresses.street, Addresses.house_number "
                   "FROM Users "
                   "JOIN BankCards ON Users.id = BankCards.user_id "
                   "JOIN \"Transactions\" ON BankCards.id = \"Transactions\".bank_card_id "
                   "JOIN Addresses ON Users.id = Addresses.id "
                   "JOIN Cities ON Addresses.city_id = Cities.id "
                   "JOIN Countries ON Cities.country_id = Countries.id")

    data = cursor.fetchall()
    return data
