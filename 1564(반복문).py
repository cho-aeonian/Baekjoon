def gcd(n, m):
    if n >= m:
        i = m
    else:
        i = n

    num = 1
    for j in range(1, i + 1):
        if n % j == 0 and m % j == 0:
            num = j

    return num

# 메인 함수
a, b = map(int, input().split())
result = gcd(a, b)
print(result)