from validators import validate_user_choice
from errors import IncorrectUserInputError
from providers import provide_db
from business_logic import (create_category,
                            add_product,
                            get_all,
                            get_product,
                            place_an_order,
                            get_status
                            )
from config import TYPE_JSON, DB_STOCK, CATEGORY_LIST, ORDER_LIST


def main() -> None:
    print("Choose t action from menu\n"
          "0 - Exit\n"
          "1 - Сreate a product category\n"
          "2 - Added new product\n"
          "3 - List of all products\n"
          "4 - Get goods by id\n"
          "5 - Make an order\n"
          "6 - Get statistics\n"
          )
    while True:
        choice = input("Your choice: ").strip()

        try:
            validate_user_choice(choice)

        except IncorrectUserInputError as err:
            print(err)
            continue

        if choice == "1":
            category = input("Enter category: ").upper().strip()
            parametrs = input("Enter parameters: ").title().strip().split(" ")
            create = create_category(category, parametrs, provide_db(TYPE_JSON, CATEGORY_LIST))
            print(create)

        if choice == "2":
            category = input("Enter category: ").upper().strip()
            quantity = input("Enter quantity product: ")
            if not quantity.isdigit():
                raise IncorrectUserInputError("quantity must be integer.")
            addproduct = add_product(category, quantity, provide_db(TYPE_JSON, CATEGORY_LIST), provide_db(TYPE_JSON, DB_STOCK))
            print(addproduct)

        if choice == "3":
            category = input("Enter category: ").upper().strip()
            min_date = input("Enter date from: ").strip()
            max_date = input("Enter date before: ").strip()
            getall = get_all(category, provide_db(TYPE_JSON, DB_STOCK), min_date, max_date)
            print(getall)

        if choice == "4":
            pr_code = input("Enter product code (id): ").strip()
            if not pr_code.isdigit():
                raise IncorrectUserInputError("quantity must be integer.")
            get_product(pr_code, provide_db(TYPE_JSON, DB_STOCK))

        if choice == "5":
            basket = {}
            while True:
                if basket:
                    cont_shopping = input("continue shopping (1)/ go to purchase (0): ")
                    if cont_shopping == "0":
                        break
                    elif cont_shopping == "1":
                        print("add items to basket!")
                    else:
                        print("Value Error")
                        continue
                    code_pr = input("enter product code: ")
                    basket[code_pr] = input("enter quantity product: ")
                    if not basket[code_pr].isdigit():
                        raise IncorrectUserInputError("quantity must be integer.")
                else:
                    print("add items to basket!")
                    code_pr = input("enter product code: ")
                    basket[code_pr] = input("enter quantity product: ")
                    if not basket[code_pr].isdigit():
                        raise IncorrectUserInputError("quantity must be integer.")
            place = place_an_order(basket, provide_db(TYPE_JSON, DB_STOCK), provide_db(TYPE_JSON, ORDER_LIST))
            print(place)

        if choice == "6":
            min_date = input("Enter date from: ").strip()
            max_date = input("Enter date before: ").strip()
            status = get_status(provide_db(TYPE_JSON, ORDER_LIST), min_date, max_date)
            print(status)

        elif choice == "0":
            print("Exit")
            break


main()
