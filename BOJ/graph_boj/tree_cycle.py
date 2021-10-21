# BOJ 4803 트리
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


def dfs(node, parent):
    for nxt in graph[node]:
        if nxt == parent:
            continue
        if get_parent(parents, node) != get_parent(parents, nxt):
            union_parent(parents, node, nxt)
            if not dfs(nxt, node):
                return 0
        elif not finished[nxt]:
            return 0
    finished[node] = True
    return 1


tc = 0
while True:
    N, M = map(int, si().split(" "))
    if N == 0 and M == 0:
        break
    tc += 1
    parents = [i for i in range(N + 1)]
    finished = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, si().split(" "))
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    for i in range(1, N + 1):
        if get_parent(parents, i) == i:
            cnt += dfs(i, 0)
    answer = ""
    if cnt == 0:
        answer = "No trees."
    elif cnt == 1:
        answer = "There is one tree."
    else:
        answer = "A forest of " + str(cnt) + " trees."
    print(f"Case {tc}: {answer}")
