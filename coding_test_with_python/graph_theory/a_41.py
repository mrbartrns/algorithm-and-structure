# 여행 계획
import sys

sys.stdin = open('../input.txt', 'r')
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


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return a == b


def check(arr, plan):
    parent = arr[plan[0]]
    for i in range(len(plan)):
        if parent != arr[plan[i]]:
            return False
    return True


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
plan = list(map(int, si().split()))
parents = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not find_parent(parents, i, j):
            union_parent(parents, i, j)

print("YES" if check(parents, plan) else "NO")
