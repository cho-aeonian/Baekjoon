n=int(input())

def func(n):
    if n==1:
        print(n)
    else:
        print(n)
        func(n-1)
func(n)