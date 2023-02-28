from datetime import datetime
from time import sleep


def time_list(n):
    date_list = [datetime.strftime(datetime.now(
        sleep(1)), '%Y-%m-%d %H:%M:%S') for _ in range(n)]
    return date_list


print(time_list(int(input("Enter number: "))))
