# 최대공약수를 계산하는 함수
def gcd(n, m):
    # n이 m보다 크거나 같으면 i=m, 아니면 i=n
    if n >= m:
        i = m
    else:
        i = n

    # 최대공약수 저장하는 변수를 1로 초기화
    num = 1

    # 1부터 i까지 반복하는 for문
    for j in range(1, i + 1):
        # 만약 n과 m이 j로 나눴을 때 나머지가 0이면 num=j
        if n % j == 0 and m % j == 0:
            num = j
    return num #최대공약수반환

# a,b 입력 받기
a, b = map(int, input().split())

# 함수로 최대공약수 계산해서 a,b 출력
result = gcd(a, b)
print(result)
