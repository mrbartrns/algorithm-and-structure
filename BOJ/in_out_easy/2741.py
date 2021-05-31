import sys


def print_n(n):
    string = ""
    if n == 1:
        return "1"
    string += print_n(n - 1) + "\n" + str(n)
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_n(n))