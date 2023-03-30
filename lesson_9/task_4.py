import csv
import heapq
from typing import Callable, TypeVar, ParamSpec

RT = TypeVar('RT')
P = ParamSpec('P')


cash_db = {}

with open("/home/siarhei/Disk/PY35/prodject/lesson_9/sp500.csv") as f_csv:
    cvs_file = csv.DictReader(f_csv)
    csv_list = list(cvs_file)


def cash(func: Callable[P, RT]) -> Callable[P, RT]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
        if args in cash_db:
            return cash_db[args]
        else:
            result = func(*args, **kwargs)
            cash_db[args] = result
            return result
    return wrapper


@cash
def find_info_by_name(name_lookup: str) -> list:

    list_comp = []

    for row in csv_list:
        name = row["Name"].lower()

        if name_lookup in name:
            list_comp.append(row)
    return list_comp


@cash
def find_info_by_symbol(symbol: str) -> list:

    list_symbol = []

    for row in csv_list:
        item_symbol = row["Symbol"].lower()

        if symbol in item_symbol:
            list_symbol.append(row)
    return list_symbol


@cash
def get_all_companies_by_sector(sector: str) -> list:

    list_name = []

    for row in csv_list:
        sector_list = row["Sector"].lower()

        if sector in sector_list:
            list_name.append(row["Name"])
    return list_name


@cash
def calculate_average_price() -> int:

    price = [float(row["Price"]) for row in csv_list]
    price_int = round(sum(price) / len(price), 2)

    return price_int


@cash
def get_top_10_companies() -> list:

    top = heapq.nlargest(10, csv_list, key=lambda row: float(row["Price"]))
    top_10_company = [(row["Name"], float(row["Price"])) for row in top]

    return top_10_company


def main() -> None:
    print("""Choose t action from menu:
    1 - Find info by name
    2 - Find info by symbol
    3 - Get all companies by sector
    4 - Calculate average price
    5 - Get top 10 companies
    6 - Exit""")

    while True:
        choice = input("Your choice: ")

        if choice.isdigit():
            choice = int(choice)

            if choice > 6:
                print("Please correct choice")
            else:
                if choice == 1:
                    company_name = input("enter company name: ").lower()
                    comp_list = find_info_by_name(company_name)
                    print(comp_list)

                if choice == 2:
                    symbol = input("enter company symbol: ").lower()
                    symbol_list = find_info_by_symbol(symbol)
                    print(symbol_list)

                elif choice == 3:
                    sector_name = input("enter sector name: ").lower()
                    s_comp_name = get_all_companies_by_sector(sector_name)
                    print(s_comp_name)

                elif choice == 4:
                    calculate_price = calculate_average_price()
                    print(calculate_price)

                elif choice == 5:
                    exp_compan = get_top_10_companies()
                    print(exp_compan)

                elif choice == 6:
                    print("exit from the program")
                    break

        else:
            print("you entered an invalid value, re-enter")


main()
