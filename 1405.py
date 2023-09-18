n = int(input())  # 숫자의 개수를 입력 받음
numbers = input().split()  # 숫자들을 공백으로 구분하여 입력 받음

# 입력된 숫자들을 리스트에 저장
numbers_list = list(numbers)

# 입력한 횟수만큼 로테이션하며 출력
for _ in range(n):
    for j in range(n):
        print(numbers_list[j], end=' ')
    print()
    
    # 리스트에서 첫 번째 요소를 pop하여 끝에 append
    numbers_list.append(numbers_list.pop(0))