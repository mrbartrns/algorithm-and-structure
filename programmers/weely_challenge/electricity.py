# 전력망을 둘로 나누기
from collections import deque

INF = 987654321


def bfs(node, a1, a2, visited, graph):
    que = deque()
    s = {a1, a2}
    visited[node] = True
    que.append(node)
    cnt = 1
    while que:
        cur = que.popleft()

        for nxt in graph[cur]:
            if visited[nxt]:
                continue

            if cur in s and nxt in s:
                continue

            visited[nxt] = True
            que.append(nxt)
            cnt += 1
    return cnt


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    ret = INF
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        visited = [False] * (n + 1)
        temp = []
        for i in range(1, n + 1):
            if not visited[i]:
                temp.append(bfs(i, a, b, visited, graph))
        ret = min(ret, abs(temp[0] - temp[1]))
    return ret


if __name__ == "__main__":
    n = 7
    wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
    print(solution(n, wires))
