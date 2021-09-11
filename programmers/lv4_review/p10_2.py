# [카카오] 동굴 탐험
"""
    1) 적어도 모든 방을 한번씩 방문해야 한다 -> visited로 관리
    2) 특정 방을 먼저 방문한다 -> 현재 node보다 먼저 방문할 배열 저장
    3) 탐색순서를 빠르게 하기 위하여 다음에 방문할 node 저장하기

    ** 여러번 방문하는 것도 visited를 이용하여 한번에 처리 후, prev 또는 next 배열을 활용하여 재 방문 할 수 있도록 함
"""
import sys

sys.setrecursionlimit(1000000)


def dfs(node, visited, prev_visit, next_visit, graph):
    if not visited[prev_visit[node]]:
        next_visit[prev_visit[node]] = node
        return

    visited[node] = True
    if not visited[next_visit[node]]:
        dfs(next_visit[node], visited, prev_visit, next_visit, graph)

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, visited, prev_visit, next_visit, graph)


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
    dfs(0, visited, prev_visit, next_visit, graph)
    cnt = 0
    for i in range(len(visited)):
        if visited[i]:
            cnt += 1
    return cnt == len(visited)


if __name__ == "__main__":
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[4, 1], [8, 7], [6, 5]]
    print(solution(n, path, order))
