import sys


"""
def print_star(n):
    string = ""
    k = n - 1
    for y in range(1, n):
        string += " " * k + "*" * (2 * y - 1) + "\n"
        k -= 1
    string += "*" * (2 * n - 1)
    k += 1
    for y in range(n - 1, 0, -1):
        string += "\n" + " " * k + "*" * (2 * y - 1)
        k += 1
    return string
"""


def print_star(n, k):
    if k == n:
        return "*" * (2 * n - 1) + "\n"
    else:
        string = ""
        string += " " * (n - k) + "*" * (2 * k - 1) + "\n"
        string += print_star(n, k + 1)
        string += " " * (n - k) + "*" * (2 * k - 1) + "\n"
        return string


n = int(sys.stdin.readline())
sys.stdout.write(print_star(n, 1))
