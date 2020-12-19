import sys

sys.setrecursionlimit(1000000)


def get_sum(n):
    if n == 0:
        return 0
    else:
        value = n + get_sum(n - 1)
        return value


n = int(sys.stdin.readline())
print(get_sum(n))