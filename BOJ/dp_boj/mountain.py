# BOJ 14699 관악산
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def climb(n):
    if cache[n] > -1:
        return cache[n]
    cache[n] = 1
    ret = 0
    for nxt in adj[n]:
        if heights[n] < heights[nxt]:
            ret = max(ret, climb(nxt))
    cache[n] += ret
    return cache[n]


N, M = map(int, si().strip().split(" "))
heights = [0] + list(map(int, si().strip().split(" ")))
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, si().strip().split(" "))
    adj[a].append(b)
    adj[b].append(a)
cache = [-1 for _ in range(N + 1)]
for i in range(1, N + 1):
    if cache[i] == -1:
        climb(i)
for i in range(1, N + 1):
    print(cache[i])
