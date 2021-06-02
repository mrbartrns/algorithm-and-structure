# kruskal algorithms
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, si().split())))  # a -> b : c


def kruskal():
    graph.sort(key=lambda x: x[2])
    tot = 0
    edges = 0
    parent = [i for i in range(n + 1)]
    for i in range(m):
        if i == n - 1:
            break
        cur = graph[i][0]
        next_node = graph[i][1]
        cost = graph[i][2]
        if not find_parent(parent, cur, next_node):
            union_parent(parent, cur, next_node)
            edges += 1
            tot += cost
    return tot


def get_parent(arr, a):
    if a == arr[a]:
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
