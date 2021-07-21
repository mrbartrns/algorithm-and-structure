# 어두운 길
import sys
from functools import reduce

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def kruskal(arr, n, m):
    edges = 0
    ret = 0
    arr.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    for i in range(m):
        a, b, c = arr[i]
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            edges += 1
            ret += c
        if edges == n - 1:
            break
    return ret


def find_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = find_parent(arr, arr[a])
    return arr[a]


def union_parent(arr, a, b):
    a = find_parent(arr, a)
    b = find_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n, m = map(int, si().split())
arr = [list(map(int, si().split())) for _ in range(m)]
tot = reduce(lambda acc, cur: acc + cur[2], arr, 0)
print(tot - kruskal(arr, n, m))
