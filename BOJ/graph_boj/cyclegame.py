# BOJ 사이클 게임
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


N, M = map(int, si().split(" "))
parents = [i for i in range(N)]
answer = 0
for i in range(M):
    a, b = map(int, si().split(" "))
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
    else:
        answer = i + 1
        break

print(answer)
