import sys


def print_star(n, k):
    string = ""
    if n == 1:
        return " " * (k) + "*"
    string += print_star(n - 1, k + 1) + "\n"
    string += " " * k
    for i in range(n):
        string += "*"
        if i < n - 1:
            string += " "
    return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 0))