# BOJ 1197 최소 스패닝 트리
import sys

sys.stdin = open("../input.txt")
si = sys.stdin.readline


def find(arr, a):
    if arr[a] == a:
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


def kruskal(routes):
    parents = [i for i in range(V + 1)]
    routes.sort(key=lambda x: x[2])
    edge = 0
    ret = 0
    for u, v, w in routes:
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            edge += 1
            ret += w
        if edge == V - 1:
            break
    return ret


V, E = map(int, si().split(" "))
edges = []
for _ in range(E):
    a, b, c = map(int, si().split(" "))
    edges.append((a, b, c))
print(kruskal(edges))
