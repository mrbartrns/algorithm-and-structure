# BOJ 16562 친구비
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def find(arr, a):
    if arr[a] == a:
        return a
    arr[a] = find(arr, arr[a])
    return arr[a]


def union(arr, a, b):
    a = find(arr, a)
    b = find(arr, b)
    if costs[a] < costs[b]:
        arr[b] = a
    else:
        arr[a] = b


N, M, K = map(int, si().split(" "))
costs = [0] + list(map(int, si().split(" ")))
parents = [i for i in range(N + 1)]
answer = 0
for _ in range(M):
    a, b = map(int, si().split(" "))
    union(parents, a, b)
for i in range(1, N + 1):
    p = find(parents, i)
    if find(parents, 0) != p:
        union(parents, 0, i)
        answer += costs[p]

print(answer if answer <= K else "Oh no")
