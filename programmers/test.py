def solution(tickets):
    answer = []
    graph = {}
    visited = {}
    for a, b in tickets:
        graph[a] = graph.get(a, []) + [b]
        visited[a] = visited.get(a, []) + [False]
    dfs("ICN", ["ICN"], answer, graph, visited, tickets)
    answer.sort()
    return answer[0]


def dfs(city, ret, answer, graph, visited, tickets):
    if len(ret) == len(tickets) + 1:
        answer.append(ret[:])
        return

    if city in graph:
        for i in range(len(graph[city])):
            if not visited[city][i]:
                visited[city][i] = True
                ret.append(graph[city][i])
                dfs(graph[city][i], ret, answer, graph, visited, tickets)
                ret.pop()
                visited[city][i] = False


if __name__ == "__main__":
    tickets = [
        ["ICN", "SFO"],
        ["ICN", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "ICN"],
        ["ATL", "SFO"],
    ]
    print(solution(tickets))