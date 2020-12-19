import sys


def print_number(n):
    if n == 1:
        string = str(1)
    else:
        string = print_number(n - 1) + "\n" + str(n)
    return string


n = int(sys.stdin.readline())
print(print_number(n))