n = int(input())

number = n * (n + 1) // 2

for i in range(n, 0, -1):
    for j in range(n, i - 1, -1):
        print(number, end=" ")
        number -= 1
    print()