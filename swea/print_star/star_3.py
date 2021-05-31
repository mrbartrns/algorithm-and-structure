import sys


def print_star(n):
    if n == 1:
        return "*"
    else:
        string = ""
        string += "*" * n + "\n"
        string += print_star(n - 1)
        return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n))