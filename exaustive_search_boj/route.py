# BOJ 11403
# 플루이드 알고리즘을 이용한다면?
# 먼저 dfs 방식으로 풀어보기
import sys


def dfs(node):
    for i in range(n):
        if not visited[i] and graph[node][i] == 1:
            visited[i] = True
            dfs(i)


si = sys.stdin.readline

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i)
    for j in range(n):
        if visited[j]:
            ans[i][j] = 1

for i in range(n):
    print(" ".join(list(map(str, ans[i]))))
