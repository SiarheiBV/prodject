"""string"""
import random


a = 'вот так работает'
b = ' конкантенация строк'
print(a + b)

st = 'строка '
print(5 * st)

st = 'строка'
print(len(st))  # длина строки

s = 'hello'
print(s[0:5:1],s[::1],s[0:5:2],s[::2])


a = random.randint(100,999)
print(a)
a = str(a)
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = b + c + d
print(e)

s = '1313'
print(s[::3])
print(s[0],s[-1])
print(s.upper())
print(s[::-1])
print(s.isdigit())

"""intenger and float"""

a = 6
b = 3.14
c = a + b
d = a - b
f = a / b
n = a * b
g = a % b
h = a ** b
v = a // b

int_ = 674
rint_ = 674//10 # нахождение последней цифры числа (в больших числах лучше применять циклы)

print(c)
print(d)
print(f)
print(n)
print(g)
print(h)
print(v)

"""bool"""

number = 1
number_2 = 1
print(number == number_2)
my_name = "Sergei"
your_name = "Vacya"
print(my_name == your_name)

