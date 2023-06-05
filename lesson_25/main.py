from errors import IncorrectUserInputError
from validators import (validate_user_choice,
                        validate_id)
from business_logic import (get_users_list,
                            get_user_info,
                            update_user_email,
                            update_user_phone,
                            get_books_list,
                            get_book_info,
                            delete_book,
                            update_book_name,
                            get_authors_list,
                            get_authors_info,
                            get_transactions,
                            cursor)


def main() -> None:
    print("Choose action from menu\n"
          "0 - Exit\n"
          "1 - Users\n"
          "2 - Books\n"
          "3 - Authors\n"
          "4 - Transactions\n"
          )

    while True:
        choice = input("Your choice: ").strip()

        try:
            validate_user_choice(choice)

        except IncorrectUserInputError as err:
            print(err)
            continue

        if choice == "0":
            break

        elif choice == "1":
            print("Choose action from menu\n"
                  "1 - List of all users\n"
                  "2 - Get user info\n"
                  "3 - Update user email\n"
                  "4 - Update user phone\n"
                  )
            choice = input("Your choice: ").strip()
            if choice == "1":
                user_list = get_users_list()
                for user in sorted(user_list, key=lambda x: (x[1], x[2])):
                    print(*user)
            elif choice == "2":
                user_id = input("input user id: ")
                try:
                    validate_id(user_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                user_info = get_user_info(user_id)
                roles_list = []
                for roles in user_info:
                    roles_list.append(roles[7])
                print("\n"
                      f"id: {user_info[0][0]}\n"
                      f"name: {user_info[0][1]}\n"
                      f"surname: {user_info[0][2]}\n"
                      f"Email: {user_info[0][3]}\n"
                      f"Phone: {user_info[0][4]}\n"
                      f"Age: {user_info[0][5]}\n"
                      f"Registration_date: {user_info[0][6]}\n"
                      f"Roles: {roles_list}\n")

            elif choice == "3":
                user_id = input("input user id: ")
                try:
                    validate_id(user_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                email = input("input new email: ")
                update_user_email(user_id, email)
                print("user email updated")

            elif choice == "4":
                user_id = input("input user id: ")
                try:
                    validate_id(user_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                phone = input("input new email: ")
                update_user_phone(user_id, phone)
                print("user phone updated")

        elif choice == "2":
            print("Choose action from menu\n"
                  "1 - List of all books\n"
                  "2 - Get book info\n"
                  "3 - Delete book\n"
                  "4 - Update book Name\n"
                  )
            choice = input("Your choice: ").strip()
            if choice == "1":
                books_list = get_books_list()
                for book in sorted(books_list, key=lambda x: (x[1], x[2])):
                    print(*book)
            elif choice == "2":
                book_id = input("input book id: ")
                try:
                    validate_id(book_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                book_info = get_book_info(book_id)
                genres_list = []
                for genres in book_info:
                    genres_list.append(genres[11])
                print("\n"
                      f"ID: {book_info[0][0]}\n"
                      f"Name: {book_info[0][1]}\n"
                      f"Age: {book_info[0][2]}\n"
                      f"Price: {book_info[0][3]}\n"
                      f"Decription: {book_info[0][4]}\n"
                      f"Authors: {book_info[0][9]} {book_info[0][10]}\n"
                      f"Pages: {book_info[0][5]}\n"
                      f"Format: {book_info[0][6]}\n"
                      f"Genres: {genres_list}\n"
                      f"Quantity: {book_info[0][7]}\n"
                      f"Added to shop: {book_info[0][8]}")

            elif choice == "3":
                book_id = input("input book id: ")
                try:
                    validate_id(book_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                delete_book(book_id)
                print("book delete")

            elif choice == "4":
                book_id = input("input book id: ")
                try:
                    validate_id(book_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue
                book_name = input("input new name for book: ")
                update_book_name(book_id, book_name)
                print("update name")
        elif choice == "3":
            print("1 - List of all authors\n"
                  "2 - Get author info"
                  )
            choice = input("Your choice: ").strip()

            if choice == "1":
                authors = get_authors_list()
                for author in sorted(authors, key=lambda x: (x[1], x[2])):
                    print(*author)
            if choice == "2":
                author_id = input("input author id: ")
                try:
                    validate_id(author_id)
                except IncorrectUserInputError as err:
                    print(err)
                    continue

                author_info = get_authors_info(author_id)
                print(f"Id: {author_info[0][0]}\n"
                      f"Name: {author_info[0][1]} {author_info[0][2]}\n"
                      f"Birthday: {author_info[0][3]}\n"
                      f"Deathday: {author_info[0][4]}\n"
                      f"Info: {author_info[0][5]}\n"
                      )

        elif choice == "4":
            transactions = get_transactions()
            for item in transactions:
                print(*item)


main()
cursor.close()
