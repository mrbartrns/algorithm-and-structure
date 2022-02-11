# BOJ 2600 구슬 게임
import sys


# sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(100000)
si = sys.stdin.readline
INF = 10


def solve(p, k1, k2):
    if k1 < 0 or k2 < 0:
        print("here")
        return 1 - p
    if cache[p][k1][k2] < INF:
        print("visited")
        return cache[p][k1][k2]
    for c in arr:
        cache[p][k1][k2] = min(
            cache[p][k1][k2], solve(1 - p, k1 - c, k2), solve(1 - p, k1, k2 - c)
        )
    return cache[p][k1][k2]


# arr = map(int, si().strip().split(" "))
arr = [1, 3, 4]
# cache = [[[-1 for _ in range(501)] for _ in range(501)] for _ in range(501)]
# for _ in range(5):
#     a, b = map(int, si().strip().split(" "))
#     print(so lve(1, a, b))
a, b = 10, 2
cache = [[[INF for _ in range(b + 1)] for _ in range(a + 1)] for _ in range(2)]
print(solve(1, a, b))
