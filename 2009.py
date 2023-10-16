a,b=map(int, input().split())
sum=0
while a/b>=1:
    sum+=1
    a-=b
    a+=1
print(sum)