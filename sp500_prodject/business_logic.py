from data_access import get_all_records
import pandas as pd
from faker import Faker
from random import uniform
from time import time


def time_cash(del_time=5):

    cash_db = {}

    def cash(func):
        def wrapper(*args, **kwargs):
            if args in cash_db and time() - cash_db[args][1] < del_time:
                return cash_db[args][0]
            else:
                result = func(*args, **kwargs)
                cash_db[args] = (result, time())
                return result

        return wrapper

    return cash


@time_cash(30)
def find_info_by_name(company_name: str) -> list:
    list_comp = []

    for row in get_all_records():
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
def find_info_by_symbol(symbol: str) -> list:
    list_symbol = []

    for row in get_all_records():
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
def get_all_companies_by_sector(sector: str) -> list:
    list_name = []

    for row in get_all_records():
        sector_list = row["Sector"].lower()

        if sector in sector_list:
            list_name.append(row["Name"])
    return list_name


def calculate_average_price() -> None:
    price = [float(row["Price"]) for row in get_all_records()]
    price_int = round(sum(price) / len(price), 2)

    return price_int


def add_new_company(new_symbol, new_company, u_sector, u_price):

    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    new_row = pd.Series(
        {'Symbol': new_symbol, 'Name': new_company, 'Sector': u_sector, 'Price': u_price})
    date = date.append(new_row, ignore_index=True)
    date = date.fillna("None")
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Your company in list"


def update_company_name(symbol, company_name):
    date_file = pd.read_csv(
        '/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    comparison = date_file['Symbol'].str.lower() == symbol.lower()
    date_file.loc[comparison, 'Name'] = company_name
    date_file.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return f"Company name with {symbol} symbol updated to {company_name}"


def delete_company(symbol):
    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    date = date.drop(
        date[date["Symbol"].str.lower() == symbol].index)
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Removal completed successfully"


def truncate_all():
    date = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    date = date.drop(date.index, inplace=True)
    date.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)

    return "Data clearing completed successfully"


def populate_file_with_random_data(number):
    fake = Faker()
    number = int(number)
    data = pd.read_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv')
    data.drop(data.index, inplace=True)

    for i in range(0, number):
        symbol = fake.lexify(text='???').upper()
        name = fake.company()
        sector = fake.bs()
        price = round(uniform(1, 1000), 2)
        data = data.append({'Symbol': symbol, 'Name': name,
                           'Sector': sector, 'Price': price, }, ignore_index=True)
        data = data.fillna("None")

    data.to_csv('/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv', index=False)
    return data
