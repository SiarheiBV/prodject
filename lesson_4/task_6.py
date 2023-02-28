a = int(input())
b = int(input())

if a > 10 and b > 10:
    print("Оба числа больше 10")
elif a > 10 or b > 10:
    print("Одно из чисел больше 10")

if not bool(a):
    print("Условие с помощью преобразования типов")
