a,b=input().split()
a=int(a)
b=int(b)

def func(a,b):
    if a>b:
        return 0
    elif b%2:
        func(a,b-1)
        print(b,end=" ")
    elif not b%2:
        func(a,b-1)
        
func(a,b)