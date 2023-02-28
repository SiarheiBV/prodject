from business_logic import (find_info_by_name,
                            find_info_by_symbol,
                            get_all_companies_by_sector,
                            calculate_average_price,
                            add_new_company,
                            update_company_name,
                            delete_company,
                            truncate_all,
                            populate_file_with_random_data
                            )
from data_access import (valid_new_company,
                         CorrectNewCompany,
                         valid_new_name,
                         valid_del_company,
                         get_top_10_companies
                         )
from validators import validate_user_choice
from errors import IncorrectUserInputError


def main() -> None:
    print("Choose t action from menu\n"
          "0 - Exit\n"
          "1 - Find info by name\n"
          "2 - Find info by symbol\n"
          "3 - Get all companies by sector\n"
          "4 - Calculate average price\n"
          "5 - Get top 10 companies\n"
          "6 - Add new company\n"
          "7 - Update company name\n"
          "8 - Delete company\n"
          "9 - Truncate all\n"
          "10 - Populate file with random data"
          )

    while True:
        choice = input("Your choice: ").strip()

        try:
            validate_user_choice(choice)

        except IncorrectUserInputError as err:
            print(err)
            continue

        if choice == "1":
            company_name = input("enter company name: ").lower()
            comp_list = find_info_by_name(company_name)
            print(comp_list)

        if choice == "2":
            symbol = input("enter company symbol: ").lower()
            symbol_list = find_info_by_symbol(symbol)
            print(symbol_list)

        elif choice == "3":
            sector_name = input("enter sector name: ").lower()
            s_comp_name = get_all_companies_by_sector(sector_name)
            print(s_comp_name)

        elif choice == "4":
            calculate_price = calculate_average_price()
            print(calculate_price)

        elif choice == "5":
            exp_compan = get_top_10_companies()
            print(exp_compan)

        elif choice == "6":

            new_symbol = input("enter your symbol: ").strip()
            new_company = input("enter your company: ").strip()
            u_sector = input("enter sector: ").strip()
            u_price = input("enter price: ")

            try:
                valid_new_company(new_symbol, new_company, u_sector, u_price)
            except CorrectNewCompany as err:
                print(err)
                continue
            add_comp = add_new_company(
                new_symbol, new_company, u_sector, u_price)
            print(add_comp)

        elif choice == "7":
            symbol = input("enter symbol: ")
            company_name = input("enter new company name: ")
            try:
                valid_new_name(symbol, company_name)
            except CorrectNewCompany as arr:
                print(arr)
                continue

            update_name = update_company_name(symbol, company_name)
            print(update_name)

        elif choice == "8":
            symbol = input("enter symbol company: ").lower()
            try:
                valid_del_company(symbol)
            except CorrectNewCompany as arr:
                print(arr)
                continue

            result = delete_company(symbol)
            print(result)

        elif choice == "9":
            result = truncate_all()
            print(result)

        elif choice == "10":
            number = input("enter the number of companies: ")
            result = populate_file_with_random_data(number)
            print(result)

        elif choice == "0":
            print("you exit from the program")
            break


main()
