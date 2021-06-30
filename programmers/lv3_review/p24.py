# 모두 0으로 만들기

def solution(a, edges):
    answer = [0]
    if sum(a) != 0:
        return -1
    graph = [[] for _ in range(len(a))]
    visited = [False] * len(a)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    dfs(0, graph, visited, answer, a)
    return answer[0]


def dfs(idx, graph, visited, answer, arr):
    visited[idx] = True
    ans = arr[idx]
    for nxt in graph[idx]:
        if not visited[nxt]:
            ans += dfs(nxt, graph, visited, answer, arr)
    answer[0] += abs(ans)
    return ans


if __name__ == "__main__":
    a = [-5, 0, 2, 1, 2]
    edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
    print(solution(a, edges))
