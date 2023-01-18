n = int(input())
for i in range(1, n+1):
    print(i**3, sep=" ", end=" ")


count = 1
while count != n + 1:
    print(count ** 3, sep=" ", end=" ")
    count += 1
