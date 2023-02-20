import csv
from string import ascii_letters


class CorrectNewCompany(Exception):
    ...


def get_all_records():
    with open("/home/siarhei/Disk/PY35/prodject/sp500_prodject/sp500.csv", "r") as f_csv:
        return list(csv.DictReader(f_csv))


def valid_new_company(new_symbol, new_company, u_sector, u_price):
    if new_symbol.isdigit():
        raise CorrectNewCompany("symbol must be letters")

    for letter in new_symbol:
        if letter not in ascii_letters:
            raise CorrectNewCompany("symbol must be english letters")

    if len(new_symbol) not in range(3, 7):
        raise CorrectNewCompany("symbol must be len 3-6 letters")

    if len(new_company) not in range(3, 51):
        raise CorrectNewCompany("company name must be len 3-50 letters")

    for row in get_all_records():
        if new_symbol.lower() == row["Symbol"].lower():
            raise CorrectNewCompany("symbol is not unique")

        if new_company.lower() == row["Name"].lower():
            raise CorrectNewCompany("company name is not unique")

    flag = False
    for row in get_all_records():
        if u_sector.lower() in row["Sector"].lower():
            flag = True

    if flag is False:
        raise CorrectNewCompany("wrong sector name")

    if len(u_price.split('.')) == 2:
        if 0 > float(u_price) or float(u_price) > 1000:
            raise CorrectNewCompany("price in the invalid range")

    else:
        raise CorrectNewCompany("price not float")


def valid_new_name(symbol, company_name):
    flag = False
    for row in get_all_records():
        if symbol.lower() == row["Symbol"].lower():
            flag = True
    if flag is False:
        raise CorrectNewCompany("no such company")
    for row in get_all_records():
        if company_name.lower() == row["Name"].lower():
            raise CorrectNewCompany("company name is not unique")


def valid_del_company(symbol):

    flag = False
    for row in get_all_records():
        if symbol.lower() == row["Symbol"].lower():
            flag = True
    if flag is False:
        raise CorrectNewCompany("no such company")
