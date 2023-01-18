import random

a = random.randint(1, 10)
tries = 3
print("you have 3 tries")
while True:
    n = int(input("enter number:"))
    if n != a:
        print(f"{tries-1} tries left")
        tries -= 1
        if tries == 0:
            print("You lose!")
            break
    else:
        print("Congratulations you won!")
        break
