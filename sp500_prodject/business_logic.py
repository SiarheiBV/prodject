import heapq
from data_access import get_all_records
import pandas as pd
from faker import Faker
from random import uniform
from time import time
from typing import Callable, TypeVar, ParamSpec, Any
from pandas.core.frame import DataFrame

RT = TypeVar('RT')
P = ParamSpec('P')


csv_list = get_all_records()


def time_cash(del_time: int = 5) -> Callable[[Callable[P, RT]], Callable[P, RT]]:

    cash_db: dict[tuple, tuple] = {}

    def cash(func: Callable[P, RT]) -> Callable[P, RT]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT | Any:
            result = None
            if args in cash_db and time() - cash_db[args][1] < del_time:
                result = cash_db[args][0]
            else:
                result = func(*args, **kwargs)
                cash_db[args] = (result, time())
            return result

        return wrapper

    return cash


@time_cash(30)
def find_info_by_name(company_name: str) -> list[dict[str, Any]]:
    list_comp = []

    for row in csv_list:
        name = row["Name"].lower()

        if company_name in name:
            list_comp.append({
                "Symbol": row.get("Symbol"),
                "Name": row.get("Name"),
                "Sector": row.get("Sector"),
                "Stock price": row.get("Stock price")
            })
    return list_comp


@time_cash(30)
def find_info_by_symbol(symbol: str) -> list[dict[str, Any]]:
    list_symbol = []

    for row in csv_list:
        item_symbol = row["Symbol"].lower()

        if symbol in item_symbol:
            list_symbol.append({
                "Symbol": row.get("Symbol"),
                "Name": row.get("Name"),
                "Sector": row.get("Sector"),
                "Stock price": row.get("Stock price")
            })
    return list_symbol


@time_cash(30)
def get_all_companies_by_sector(sector: str) -> list[str]:
    list_name = []

    for row in csv_list:
        sector_list = row["Sector"].lower()

        if sector in sector_list:
            list_name.append(row["Name"])
    return list_name


def calculate_average_price() -> float:
    price = [float(row["Price"]) for row in csv_list]
    price_int = round(sum(price) / len(price), 2)

    return price_int


def get_top_10_companies() -> list:
    top = heapq.nlargest(10, csv_list, key=lambda row: float(row["Price"]))
    top_10_company = [(row["Name"], float(row["Price"])) for row in top]

    return top_10_company


def add_new_company(new_symbol: str, new_company: str, u_sector: str, u_price: str) -> str:

    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    new_row = pd.Series(
        {'Symbol': new_symbol, 'Name': new_company, 'Sector': u_sector, 'Price': u_price})
    date = date.append(new_row, ignore_index=True)
    date = date.fillna("None")
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Your company in list"


def update_company_name(symbol: str, company_name: str) -> str:
    date_file = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    comparison = date_file['Symbol'].str.lower() == symbol.lower()
    date_file.loc[comparison, 'Name'] = company_name
    date_file.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return f"Company name with {symbol} symbol updated to {company_name}"


def delete_company(symbol: str) -> str:
    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    date = date.drop(
        date[date["Symbol"].str.lower() == symbol].index)
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Removal completed successfully"


def truncate_all() -> str:
    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    date = date.drop(date.index, inplace=True)
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Data clearing completed successfully"


def populate_file_with_random_data(number: str) -> DataFrame:
    fake = Faker()
    int_number = int(number)
    data = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    data.drop(data.index, inplace=True)

    for i in range(0, int_number):
        symbol = fake.lexify(text='???').upper()
        name = fake.company()
        sector = fake.bs()
        price = round(uniform(1, 1000), 2)
        data = data.append({'Symbol': symbol, 'Name': name,
                           'Sector': sector, 'Price': price, }, ignore_index=True)
        data = data.fillna("None")

    data.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)
    return data
