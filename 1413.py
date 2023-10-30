#말하는 앵무새
#문자열을 거꾸로 출력하기

#for문을 이용하는 방법
str = input()

for i in range(len(str)-1, -1, -1):
    print(str[i], end='')