"""
1. 각 구간은 한 개 이상의 연속된 수들로 이루어진다.
2. 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
3. 정확히 M개의 구간이 있어야 한다.
-1 3 1 2 4 -1
총 N + 1개의 요소가 존재
"""
# BOJ 2228 구간 나누기
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
INF = 987654321


def pre_sum():
    for i in range(1, N + 1):
        psum[i] = psum[i - 1] + arr[i]


def section(cnt, start):
    if cnt == 0:
        return 0
    if start > N or cnt < 0:
        return -INF
    if cache[cnt][start] > -INF:
        return cache[cnt][start]
    cache[cnt][start] = max(cache[cnt][start], section(cnt, start + 1))
    for i in range(N - start + 1):
        cache[cnt][start] = max(
            cache[cnt][start],
            section(cnt - 1, start + i + 2) + psum[start + i] - psum[start - 1],
        )
    return cache[cnt][start]


N, M = map(int, si().split(" "))
arr = [0] + [int(si()) for _ in range(N)]
cache = [[-INF for _ in range(N + 1)] for _ in range(M + 1)]
psum = [0] * (N + 1)
pre_sum()
print(section(M, 1))
