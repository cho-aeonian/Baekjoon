# a,b,c의 최대공약수 계산하는 함수
def three_numbers(a, b, c):
    def gcd(x, y):
        # 유클리드를 이용하여 최대공약수 구하기
        while y:
            x, y = y, x % y
        return x
    
    # 두 수의 최대공약수 result에 넣기
    result = gcd(a, b)
    
    # 두 수의 최대공약수와 세번째 정수 비교해서 최대공약수 result에 넣기
    result = gcd(result, c)
    
    # 세 수의 최대공약수 반환
    return result

# a,b,c에 입력받기
a, b, c = map(int, input().split())

# 재귀함수 사용해서 a,b,c 최대공약수 출력
result = three_numbers(a, b, c)
print(f"{result}")
