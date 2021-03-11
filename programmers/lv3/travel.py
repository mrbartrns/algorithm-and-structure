# 여행경로
import sys

sys.setrecursionlimit(10001)


def solution(tickets):
    def dfs(node):
        if len(temp) == len(tickets) + 1:
            answer.append(temp[:])
            return

        if node in graph.keys():
            for i in range(len(graph[node])):
                if not visited[node][i]:
                    visited[node][i] = True
                    temp.append(graph[node][i])
                    dfs(graph[node][i])
                    temp.pop()
                    visited[node][i] = False

    answer = []
    temp = ["ICN"]
    graph = {}
    visited = {}
    for i in range(len(tickets)):
        graph[tickets[i][0]] = graph.get(tickets[i][0], []) + [tickets[i][1]]
        visited[tickets[i][0]] = visited.get(tickets[i][0], []) + [False]
    dfs("ICN")
    answer.sort()
    return answer[0]


tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
print(solution(tickets))