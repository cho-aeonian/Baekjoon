inputNumber = int(input())
temp = inputNumber
digit = 0

while temp > 0:
    digit += 1
    temp //= 10

digit2 = digit

for i in range(digit):
    if inputNumber % 10 == 0:
        digit2 -= 1
        inputNumber //= 10
    else:
        result = inputNumber
        reversed_str = ""
        for i in range(digit2):
            rem = result % 10
            result //= 10
            reversed_str += str(rem)
        print(reversed_str[::-1])
        print(sum(int(digit) for digit in reversed_str))
        break
