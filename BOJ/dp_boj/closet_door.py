# BOJ 2666 벽장문의 이동
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(100000)
si = sys.stdin.readline
INF = 987654321


def move(idx, left, right):
    if left >= right:
        return INF
    if idx >= M:
        return 0
    if cache[idx][left][right] < INF:
        return cache[idx][left][right]
    cache[idx][left][right] = min(
        cache[idx][left][right],
        abs(left - arr[idx]) + move(idx + 1, arr[idx], right),
        abs(right - arr[idx]) + move(idx + 1, left, arr[idx]),
    )
    return cache[idx][left][right]


N = int(si().strip())
a, b = map(int, si().strip().split(" "))
M = int(si().strip())
arr = []
for _ in range(M):
    arr.append(int(si().strip()))
cache = [[[INF for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(M)]
print(move(0, min(a, b), max(a, b)))
