# [카카오] 동굴 탐험 풀이 1
import sys

sys.setrecursionlimit(1000000)


def dfs(node, visited, prev_visit, next_visit, graph):
    if visited[node]:
        return
    if not visited[prev_visit[node]]:
        next_visit[prev_visit[node]] = node
        return
    visited[node] = True
    if next_visit[node]:
        dfs(next_visit[node], visited, prev_visit, next_visit, graph)
    for i in graph[node]:
        dfs(i, visited, prev_visit, next_visit, graph)


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    prev_visit = [0 for _ in range(n)]  # prev_visit[next] = prev
    next_visit = [0 for _ in range(n)]  # next_visit[prev] = next

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in order:
        prev_visit[b] = a

    if prev_visit[0] > 0:  # 0을 방문하기 전에 선 방문 노드가 존재한다면
        return False

    visited[0] = True
    for i in graph[0]:
        dfs(i, visited, prev_visit, next_visit, graph)

    chk = 0
    for i in range(n):
        if visited[i]:
            chk += 1
    return True if chk == n else False


if __name__ == '__main__':
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    print(solution(n, path, order))
