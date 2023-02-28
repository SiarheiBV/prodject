name = input("What your name? ")
flag = True

while flag:

    age = input("how old are you? ")
    if not age.isnumeric():
        print("Error, repeat input!")
    else:
        age = float(age)

        if age <= 0:
            print("Error, repeat input!")
        else:
            flag = False

            if age < 10:
                print(f"Привет, шкет {name}")
            elif age <= 18:
                print(f"Как жизнь {name}?")
            elif age < 100:
                print(f"Что желаете {name}?")
            else:
                print(f"{name}, Вы лжете - в наше время столько не живут...")
