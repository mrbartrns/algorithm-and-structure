# BOJ 10971
import sys

si = sys.stdin.readline

"""
필요한 것
visited 배열
최솟값을 저장할 수 있는 배열
자기 자신으로 돌아오는 길이 0이 아니라면, values 배열에 추가하기
"""


def dfs(start, v, value, k):
    ret = 10000000
    if k == n and graph[v][start] > 0:
        return min(ret, value + graph[v][start])

    for i in range(n):
        if not visited[i] and graph[v][i] > 0:
            visited[i] = True
            ret = min(ret, dfs(start, i, value + graph[v][i], k + 1))
            visited[i] = False
    return ret


graph = []

n = int(si())

for _ in range(n):
    graph.append(list(map(int, si().split())))

ret = 10000000
for i in range(n):
    visited = [False] * n
    visited[i] = True
    ret = min(ret, dfs(i, i, 0, 1))


print(ret)