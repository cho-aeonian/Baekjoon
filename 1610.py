def mysubstr(s, start, count):
    if start < 0:
        start = 0
    if count < 0:
        count = 0
    return s[start:start+count]

if __name__ == "__main__":
    s = input()
    start, count = map(int, input().split())
    
    result = mysubstr(s, start, count)
    print(result)