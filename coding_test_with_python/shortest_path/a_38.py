# 정확한 순위
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def dfs(idx, graph):
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            dfs(i, graph)


n, m = map(int, si().split())
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, si().split())
    graph1[a].append(b)
    graph2[b].append(a)

answer = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    check = True
    dfs(i, graph1)
    dfs(i, graph2)
    for j in range(1, n + 1):
        if not visited[j]:
            check = False
            continue
    if check:
        answer += 1
print(answer)
