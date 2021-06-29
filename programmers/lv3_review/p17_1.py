import sys

sys.setrecursionlimit(10001)


def solution(tickets):
    graph = {}
    visited = {}
    ret = []
    for start, destination in tickets:
        graph[start] = graph.get(start, []) + [destination]
        visited[start] = visited.get(start, []) + [False]
    dfs("ICN", graph, visited, ["ICN"], ret, len(tickets))
    ret.sort()
    return ret[0]


def dfs(city, graph, visited, temp, ret, size):
    if len(temp) == size + 1:
        ret.append(temp[:])
        return

    if city in graph.keys():
        for i in range(len(graph[city])):
            if not visited[city][i]:
                visited[city][i] = True
                temp.append(graph[city][i])
                dfs(graph[city][i], graph, visited, temp, ret, size)
                temp.pop()
                visited[city][i] = False


if __name__ == "__main__":
    tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"],
               ["BOO", "ICN"], ["COO", "BOO"]]
    print(solution(tickets))
