n_1 = (1, 1)
n_2 = (1, 1)
n_3 = (1, 1)

print(id(n_1), id(n_2), id(n_3), id(n_1) == id(n_2) == id(n_3), sep="\n")
n_1_1 = str(n_1)
n_2_2 = str(n_2)
n_3_3 = str(n_3)
print(id(n_1_1), id(n_2_2), id(n_3_3), id(
    n_1_1) == id(n_2_2) == id(n_3_3), sep="\n")

n_4 = [1]
n_5 = [1]
print(id(n_4), id(n_5), id(n_4) == id(n_5), sep='\n')

n_4_4 = bool(n_4)
n_5_5 = bool(n_5)
print(id(n_4_4), id(n_5_5), id(tuple(n_4)) == id(tuple(n_5)), sep="\n")
