# BOJ 2610 회의 준비
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def find(arr, a):
    if a == arr[a]:
        return a
    arr[a] = find(arr, arr[a])
    return arr[a]


def union(arr, a, b):
    a = find(arr, a)
    b = find(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


N = int(si())
M = int(si())
parents = [i for i in range(N + 1)]
s = [INF for _ in range(N + 1)]
cache = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    cache[i][i] = 0
for _ in range(M):
    a, b = map(int, si().split(" "))
    union(parents, a, b)
    cache[a][b] = 1
    cache[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cache[i][j] = min(cache[i][j], cache[i][k] + cache[k][j])

for i in range(1, N + 1):
    c = 0
    for j in range(1, N + 1):
        if cache[i][j] < INF:
            c = max(c, cache[i][j])
    s[i] = c

count = 0
min_idx = [-1] * (N + 1)
min_values = [INF] * (N + 1)
for i in range(1, N + 1):
    p = find(parents, i)
    if i == p:
        count += 1
    if min_values[p] > s[i]:
        min_values[p] = s[i]
        min_idx[p] = i
print(count)
min_idx = list(filter(lambda x: x != -1, min_idx))
min_idx.sort()
for idx in min_idx:
    print(idx)
