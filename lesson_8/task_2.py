""" записать текст в файл"""

str_1 = input()
str_2 = input()
str_3 = input()
str_4 = input()

with open('text.txt', 'w') as f_file:
    f_file.write(str_1 + '\n')
    f_file.write(str_2 + '\n')

with open('text.txt', 'a') as f_file:
    f_file.write(str_3 + '\n')
    f_file.write(str_4)
