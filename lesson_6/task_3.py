a = [1, 2, 3, 3, 4, 4, 4]


def count_():
    b = {}
    for i in a:
        b[i] = a.count(i)
    return b


print(count_())
