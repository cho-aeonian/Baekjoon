def f_sum(n):
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits
    return n

if __name__ == "__main__":
    i = int(input())
    result = f_sum(i)
    print(result) 