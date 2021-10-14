# BOJ 1774 우주신과의 교감
import math
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def kruskal(distance, parents):
    edges = 1
    ret = 0
    distance.sort(key=lambda x: x[2])
    for i in range(len(distance)):
        a, b, c = distance[i]
        if not find_parent(parents, a, b):
            union_parent(parents, a, b)
            ret += c
            edges += 1
        if edges == N - 1:
            break
    return ret


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return a == b


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def get_distance(y1, x1, y2, x2):
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


N, M = map(int, si().split(" "))
locations = [[0, 0] for _ in range(N + 1)]
parents = [i for i in range(N + 1)]
distance = []
for i in range(1, N + 1):
    locations[i] = list(map(int, si().split(" ")))
for _ in range(M):
    n1, n2 = map(int, si().split(" "))
    union_parent(parents, n1, n2)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        y1, x1 = locations[i]
        y2, x2 = locations[j]
        distance.append((i, j, get_distance(y1, x1, y2, x2)))
print("%.2f" % kruskal(distance, parents))
