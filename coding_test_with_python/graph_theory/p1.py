# 팀 결성
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def find_parent(arr, a):
    if arr[a] != a:
        arr[a] = find_parent(arr, arr[a])
    return arr[a]


def same_parent(arr, a, b):
    a = find_parent(arr, a)
    b = find_parent(arr, b)
    return a == b


def union_parent(arr, a, b):
    a = find_parent(arr, a)
    b = find_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n, m = map(int, si().split())
parents = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, si().split())
    if op == 0:
        if not same_parent(parents, a, b):
            union_parent(parents, a, b)
    else:
        print('YES' if same_parent(parents, a, b) else 'NO')
