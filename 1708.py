num_students = int(input())  # 학생 수 입력

scores = list(map(int, input().split()))  # 각 학생의 점수를 리스트로 저장

ranks = []   # 순위를 저장할 리스트 초기화

# 순위 계산
for i in range(num_students):
    rank = 1  # 초기 순위는 1로 설정
    
    for j in range(num_students):
        if scores[j] > scores[i]:  # 다른 학생의 점수가 더 높으면 순위 증가
            rank += 1
    
    ranks.append(rank)  # 해당 학생의 순위를 리스트에 추가

# 결과 출력
for score, rank in zip(scores, ranks):
    print(score, rank)