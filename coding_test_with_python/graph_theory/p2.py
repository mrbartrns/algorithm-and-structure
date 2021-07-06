# 마을 분할하기
"""
스패닝 트리로 가장 큰 비용을 자르기
"""
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def get_parent(arr, a):
    if arr[a] != a:
        arr[a] = get_parent(arr, arr[a])
    return arr[a]


def same_parent(arr, a, b):
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


def kruskal(edges):
    edge = 0
    result = 0
    parents = [i for i in range(n + 1)]
    edges.sort(key=lambda x: x[2])
    for i in range(m):
        a, b, c = edges[i]
        if not same_parent(parents, a, b):
            union_parent(parents, a, b)
            edge += 1
            result += c
        if edge == n - 1:
            result -= c
            break
    return result


n, m = map(int, si().split())
edges = []
for _ in range(m):
    a, b, c = map(int, si().split())
    edges.append((a, b, c))
print(kruskal(edges))
