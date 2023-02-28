from time import time


def decorator(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        print(
            "\n", f"function execution time: {round(end - start, 10)} second")

    return wrapper


@decorator
def fib_for(n):
    a, b = 0, 1

    for _ in range(1, n + 1):
        print(a, end=' ')
        a, b = b, a + b


@decorator
def romb(n):
    for i in range(n):
        print(' ' * (n - i) + ' *' * (i + 1))
    for j in range(n - 1):
        print(' ' * (j + 2) + ' *' * (n - 1 - j))


fib_for(50)
romb(5)
