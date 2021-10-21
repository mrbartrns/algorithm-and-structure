# BOJ 4386 별자리 만들기
import math
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def kruskal(routes):
    edge = 0
    parents = [i for i in range(N)]
    ret = 0
    routes.sort(key=lambda x: x[2])
    for a, b, c in routes:
        if get_parent(parents, a) != get_parent(parents, b):
            union_parent(parents, a, b)
            edge += 1
            ret += c
        if edge == N - 1:
            break
    return ret


N = int(si())
info = []
edges = []
for _ in range(N):
    a, b = map(float, si().split(" "))
    info.append((a, b))
for i in range(N):
    for j in range(i + 1, N):
        y1, x1 = info[i]
        y2, x2 = info[j]
        edges.append((i, j, math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)))
print("%.2f" % kruskal(edges))
