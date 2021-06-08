# 모두 0으로 만들기
import sys

sys.setrecursionlimit(1000000)


def dfs(i, graph, visited, answer, arr):
    visited[i] = True
    ans = arr[i]
    for j in graph[i]:
        if not visited[j]:
            ans += dfs(j, graph, visited, answer, arr)
    answer[0] += abs(ans)
    return ans


def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = [[] for _ in range(len(a))]
    visited = [False] * len(a)
    for i in range(len(edges)):
        p, q = edges[i]
        graph[p].append(q)
        graph[q].append(p)
    answer = [0]
    dfs(0, graph, visited, answer, a)

    return answer[0]


if __name__ == "__main__":
    a = [-5, 0, 2, 1, 2]
    edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
    print(solution(a, edges))
