""" set """

sett = set("hello")
print(sett)

sett_2 = {'a', 'b', 'c', 'd'}
print(sett_2)

months = {'Jan', 'Feb', 'March', 'Apr', 'May'}

months.add('June')
print(months)

# объединение
months_a = {'Jan', 'Feb', 'March', 'Apr', 'May', 'June'}
months_b = {'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

all_months = months_a.union(months_b)
print(all_months)


# Пересечение
# &- ампенсан
x = {1, 2, 3}
y = {4, 3, 6}
print(x & y)
print(x.intersection(y))