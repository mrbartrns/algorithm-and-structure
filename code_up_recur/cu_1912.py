import sys


def get_fact(n):
    if n <= 1:
        res = 1
    else:
        res = n * get_fact(n - 1)
    return res


n = int(sys.stdin.readline())
print(get_fact(n))