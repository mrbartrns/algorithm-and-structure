# 섬 연결하기

INF = 987654321


def solution(n, costs):
    answer = INF
    graph = [[] for _ in range(n)]
    for i in range(len(costs)):
        s, e, cost = costs[i]
        q1 = graph[s]
        q2 = graph[e]
        q1.append((e, cost))
        q2.append((s, cost))
    for i in range(n):
        graph[i].sort(key=lambda x: (x[1]))
    for i in range(n):
        visited = [INF] * n
        visited[i] = 0
        dfs(i, visited, graph)
        answer = min(answer, sum(visited))
    return answer


def dfs(node, visited, graph):
    for v, cost in graph[node]:
        if visited[v] < INF:
            continue
        visited[v] = cost
        dfs(v, visited, graph)
        break


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))
