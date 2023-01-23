from datetime import datetime
from time import sleep


def func_sleep():
    time_now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    sleep(1)
    return time_now


def time_list(n):
    date_list = [func_sleep() for _ in range(n)]
    return date_list


print(time_list(int(input("Enter number: "))))


""" Вариант решение через цикл for"""

# def time_now(n):
#     a = []
#     for _ in range(n):
#         a.append(datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
#         sleep(1)
#     return a
#
#
# print(time_now(5))
