# 원하는 합계 입력받음
sum = int(input())

# 1부터 6까지 반복하는 for문
for i in range(1, 7):
    # 1부터 6까지 반복하는 for문
    for j in range(1, 7):
        # i와 j의 값의 합이 입력받은 수랑 같은지 확인하는 if문
        if i + j == sum:
            # if문 통과하면 i와 j의 값을 출력
            print(f"{i} {j}")
