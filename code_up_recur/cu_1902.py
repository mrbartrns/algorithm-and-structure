import sys


def print_number_reverse(n):
    if n == 1:
        string = str(1)
    else:
        string = str(n) + "\n" + print_number_reverse(n - 1)
    return string


n = int(sys.stdin.readline())
print(print_number_reverse(n))