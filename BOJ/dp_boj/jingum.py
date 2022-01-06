# BOJ 21317 징검다리 건너기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def cross(y, x):
    if y < 0 or x > N:
        return INF
    if x == N:
        return 0
    if cache[y][x] < INF:
        return cache[y][x]
    cache[y][x] = min(
        cache[y][x],
        small[x] + cross(y, x + 1),
        big[x] + cross(y, x + 2),
        ENERGY + cross(y - 1, x + 3),
    )
    return cache[y][x]


N = int(si().strip())
small = [INF] * (N + 20)
big = [INF] * (N + 20)
cache = [[INF for _ in range(N + 1)] for _ in range(2)]
for i in range(1, N):
    a, b = map(int, si().strip().split(" "))
    small[i] = a
    big[i] = b
ENERGY = int(si().strip())
print(cross(1, 1))
