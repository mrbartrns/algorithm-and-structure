# 여행 경로
import sys

sys.setrecursionlimit(10001)


def solution(tickets):
    graph = {}
    visited = {}
    for start, end in tickets:
        graph[start] = graph.get(start, []) + [end]
        visited[start] = visited.get(start, []) + [False]
    for key in graph:
        graph[key].sort()
    s = set(graph.keys())
    return dfs("ICN", graph, visited, s)


def dfs(city: str, graph: dict, visited: dict, s) -> list:
    ret = [city]

    if city in s:
        for i in range(len(graph[city])):
            if not visited[city][i]:
                visited[city][i] = True
                ret += dfs(graph[city][i], graph, visited, s)
    return ret


if __name__ == "__main__":
    tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"],
               ["BOO", "ICN"], ["COO", "BOO"]]

    print(solution(tickets))
