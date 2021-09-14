# BOJ 10775 공항
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


n = int(si())
planes = int(si())
parents = [i for i in range(n + 1)]
cnt = 0

for _ in range(planes):
    t = int(si())
    p = get_parent(parents, t)
    if p != 0:
        union_parent(parents, p - 1, p)
        cnt += 1
    else:
        break

print(cnt)