# [카카오] 동굴 탐험
import sys

sys.setrecursionlimit(1000000)


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    prev_visit = [0] * n
    next_visit = [0] * n
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in order:
        prev_visit[b] = a

    if prev_visit[0]:
        return False

    visited[0] = True
    dfs(0, visited=visited, prev_visit=prev_visit, next_visit=next_visit, graph=graph)
    cnt = 0
    for i in range(n):
        if visited[i]:
            cnt += 1
    return True if cnt == n else False


def dfs(node, **kwargs):
    if not kwargs['visited'][kwargs['prev_visit'][node]]:
        kwargs['next_visit'][kwargs['prev_visit'][node]] = node
        return

    kwargs['visited'][node] = True
    if not kwargs['visited'][kwargs['next_visit'][node]]:
        dfs(kwargs['next_visit'][node], **kwargs)

    for i in kwargs['graph'][node]:
        if not kwargs['visited'][i]:
            dfs(i, **kwargs)


if __name__ == '__main__':
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    print(solution(n, path, order))
