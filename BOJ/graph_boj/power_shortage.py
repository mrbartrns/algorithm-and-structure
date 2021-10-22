# BOJ 6497 전력난
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
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def kruskal(maps):
    parents = [i for i in range(M)]
    maps.sort(key=lambda x: x[2])
    edge = 0
    ret = 0
    for a, b, c in maps:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            ret += c
            edge += 1
            if edge == M - 1:
                break
    return ret


while True:
    M, N = map(int, si().split(" "))
    if M == 0 and N == 0:
        break
    edges = []
    s = 0
    for _ in range(N):
        a, b, c = map(int, si().split(" "))
        edges.append((a, b, c))
        s += c
    print(s - kruskal(edges))
