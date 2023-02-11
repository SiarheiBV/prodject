with open("text.txt") as file:
    count_let = file.read().lower().count(input("Enter any letter: ").lower())
print(f"буква встречается {count_let} раза в тексте.")
