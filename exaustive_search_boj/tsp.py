# BOJ 10971
import sys

si = sys.stdin.readline


n = int(si())
graph = []
for _ in range(n):
    graph.append(list(map(int, si().split())))
visited = [False] * n


def dfs(s, v, value, stack):
    ret = 100000000
    # 이 형태에 익숙해지기 > 다른조건과 관계없이 무조건 v -> start로 간다면 검사할필요 x but graph[v][s]가 0일때 다른 길로 가야 한다는것을 생각하지 못함
    if stack == n and graph[v][s] > 0:
        return min(ret, value + graph[v][s])
    for i in range(n):
        if graph[v][i] > 0 and not visited[i]:
            visited[i] = True
            ret = min(ret, dfs(s, i, value + graph[v][i], stack + 1))
            visited[i] = False
    return ret


"""
n = 4
graph = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 3, 0, 12],
    [8, 8, 9, 0],
]
"""
val = 100000000
for i in range(n):
    visited = [False] * n
    if not visited[i]:
        visited[i] = True
        val = min(val, dfs(i, i, 0, 1))
print(val)
