def reverse(num):
    result = 0
    while num != 0:
        result = result * 10 + num % 10
        num //= 10
    return result

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():

    num = int(input())
    reversed_num = reverse(num)

    sum_num = num + reversed_num

    if is_palindrome(sum_num):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
