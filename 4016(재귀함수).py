def three_numbers(a, b, c):
    # 세 수의 최대공약수를 구하는 함수
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # 세 수의 최대공약수를 차례대로 계산
    result = gcd(a, b)
    result = gcd(result, c)
    
    return result

# 사용자로부터 세 개의 숫자를 입력받음
a,b,c=map(int,input().split())

# 최대공약수 계산 및 결과 출력
result = three_numbers(a, b, c)
print(f"{result}")


a,b-map(int, input().split())

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

print(gcd(a,b))