import sys


def print_star(n, k):
    if n == 1:
        return " " * k + "*"
    else:
        string = ""
        string += print_star(n - 1, k + 1) + "\n"
        string += " " * k + "*" * (2 * n - 1)
        return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 0))