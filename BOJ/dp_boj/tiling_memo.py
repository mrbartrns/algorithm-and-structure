# 타일링(메모이제이션)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def tile(n):
    if n == N:
        return 1
    elif n > N:
        return 0

    ret = tile(n + 1) + tile(n + 2)
    return ret


N = int(si())
print(tile(0))
