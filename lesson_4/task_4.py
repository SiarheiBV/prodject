any_str = input("Enter: ")

even = ""
odd = ""
for i in range(len(any_str)):
    if i % 2 == 0:
        odd += any_str[i]
    else:
        even += any_str[i]
print("Enter string:", any_str, end="\n\n\n")
print(even, odd, sep="     ", end="\n!!!")
