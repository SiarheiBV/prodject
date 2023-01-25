def func(n: str) -> str:
    if n.isdigit():
        if isinstance(n, float) == True:
            if float(n) < 0:
                return f"Вы ввели отрицательное дробное число: {n}"
            else:
                return f"Вы ввели положительное дробное число: {n}"
        else:
            if int(n) < 0:
                return f"Вы ввели отрицательное целое число: {n}"
            else:
                return f"Вы ввели положительное целое число: {n}"
    else:
        return f"Вы ввели некорректное число: {n}"


print(func(input("Enter numbers: ")))


# def func(n: str) -> str:
#     if n.isdigit():
#         return f"Вы ввели некорректное число: {n}"
#     else:
#         try:
#             float(n)
#             if float(n) < 0:
#                 return f"Вы ввели отрицательное дробное число: {n}"
#             else:
#                 return f"Вы ввели положительное дробное число: {n}"
#         except ValueError:
#             return None

#
#
# print(func(input("Enter numbers: ")))
