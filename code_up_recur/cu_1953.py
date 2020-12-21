import sys


def print_triangle(n):
    if n == 1:
        print("*")
    else:
        print_triangle(n - 1)
        print("*" * n)


n = int(sys.stdin.readline())
print_triangle(n)
