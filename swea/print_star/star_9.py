import sys


def print_star(n, k):
    if n == 1:
        string = " " * k + "*" + "\n"
    else:
        string = " " * k + "*" * (2 * n - 1) + "\n"
        string += print_star(n - 1, k + 1)
        string += " " * k + "*" * (2 * n - 1) + "\n"
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 0))