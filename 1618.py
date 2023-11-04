# 숫자 입력
a, b, c = map(int, input().split())

# 숫자를 오름차순으로 정렬
sorted_numbers = [a, b, c]
sorted_numbers.sort()

# 정렬된 숫자 출력
print(*sorted_numbers)
