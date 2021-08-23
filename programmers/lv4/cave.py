# [카카오]  동굴 탐험(Trie)
def solution(n, path, order):
    answer = True
    indegree = [0] * n
    graph = [[] for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for _, nxt in order:
        indegree[nxt] += 1
    visited = [False] * n
    print(dfs(0, visited, graph, indegree))
    return answer


def dfs(node, visited, graph, indegree):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt] and indegree[nxt] >= indegree[node]:
            dfs(nxt, visited, graph, indegree)
    visited[node] = False


if __name__ == '__main__':
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    print(solution(n, path, order))
