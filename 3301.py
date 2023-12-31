# 금액을 저장하는 num에 가격 입력
num = int(input())

# 리스트에 돈 단위 저장
coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 동전의 갯수 세는 변수
count = 0

# 돈 단위의 각 갯수 계산하는 for문
for i in coin:
    # 동전 몇 개 쓰는지 계산에서 count에 저장
    count += num // i
     
    # num에 쓴 동전 값 뺀 값을 저장
    num %= i

# 총 사용한 동전의 갯수 출력
print(count)
