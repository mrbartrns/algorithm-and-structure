import sys


def print_star(n, k):
    if k == n:
        string = "*" * (2 * n) + "\n"
    else:
        string = "*" * k + " " * (2 * (n - k)) + "*" * k + "\n"
        string += print_star(n, k + 1)
        string += "*" * k + " " * (2 * (n - k)) + "*" * k + "\n"
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 1))