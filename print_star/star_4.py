import sys


def print_star(n, k):
    if n == 1:
        return "*"
    else:
        string = ""
        string += "*" * n + "\n"
        string += " " * k + print_star(n - 1, k + 1)
        return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 1))