import sys


def print_star(n, k):
    string = ""
    if n == k:
        string = "*" * k
        return string
    string += " " * (n - k) + "*" * k + "\n"
    string += print_star(n, k + 1)
    string += "\n" + " " * (n - k) + "*" * k
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 1))