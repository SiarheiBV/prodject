""" dict """

price = {'eggs': 1, "apple": 2, 'orange': 5}
print(price.keys())  # выводит список ключей
print(price.values()) # выводит список значений

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 100, 'b': 200, 'c': 400}
print(d1['b'] == d2['b'])