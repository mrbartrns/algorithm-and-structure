import sys


def print_star(n, k):
    string = ""
    if n == 1:
        return " " * k + "*"

    if k == 0:
        string += print_star(n - 1, k + 1) + "\n"
        string += "*" * (2 * n - 1)
    else:
        string += print_star(n - 1, k + 1) + "\n"
        string += " " * k + "*" + " " * (2 * n - 3) + "*"
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 0))