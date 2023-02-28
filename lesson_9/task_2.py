with open("text.txt") as file:
    for line in file:
        count_let = line.lower().count(input("Enter any letter: ").lower())
print(f"буква встречается {count_let} раза в тексте.")
