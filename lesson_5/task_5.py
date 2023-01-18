import timeit
import time


""" task Fibonachchi metode one"""


test = """def fib(n):
    a, b = 0, 1

    for _ in range(1, n + 1):
        print(a, end=' ')
        a, b = b, a + b"""



print(f'Время вычесления чисел Фибоначчи заняло: {timeit.timeit(stmt=test)} сек')
"""не хватило времени разобраться как правильно проверять время работы функции, разберусь с этим на выходных"""




""" task Fibonachchi metode two"""


def fib(n):
    a, b = 0, 1

    for _ in range(1, n + 1):
        print(a, end=' ')
        a, b = b, a + b


start = time.perf_counter()
result = fib(10)
end_ = time.perf_counter()
print(f"Вычисление заняло {end_ - start:0.9f} секунд",)



