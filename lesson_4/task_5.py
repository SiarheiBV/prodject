a = int(input())
b = int(input())


if a == b:
    print("Числа равны")
elif a > b:
    print("Первое число больше второго")
elif a != b or a < b:
    print("Отработала секция else")
