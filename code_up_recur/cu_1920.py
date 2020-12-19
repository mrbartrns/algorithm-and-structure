import sys


def get_binary_number(n):
    if n == 0:
        return str(n % 2)
    else:
        binary_number = get_binary_number(n // 2) + str(n % 2)
        return binary_number


n = int(sys.stdin.readline())
binary_number = get_binary_number(n)
if len(binary_number) > 1 and binary_number[0] == "0":
    print(binary_number[1:])
else:
    print(binary_number)