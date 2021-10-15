# BOJ 1922 네트워크 연결
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


def kruskal(edges):
    parents = [i for i in range(N + 1)]
    edge = 0
    ret = 0
    edges.sort(key=lambda x: x[2])
    for i in range(M):
        a, b, c = edges[i]
        if get_parent(parents, a) != get_parent(parents, b):
            union_parent(parents, a, b)
            ret += c
            edge += 1
        if edge == N - 1:
            break
    return ret


N = int(si())  # 연결할 수 있는 컴퓨터의 수
M = int(si())  # 연결할 수 있는 선의 수

edges = []
for _ in range(M):
    a, b, c = map(int, si().split(" "))  # a b를 연결하는데 필요한 비용
    edges.append((a, b, c))
print(kruskal(edges))
