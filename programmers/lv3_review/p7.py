# 순위
def solution(n, results):
    g1 = [set() for _ in range(n + 1)]
    g2 = [set() for _ in range(n + 1)]
    answer = 0
    for i in range(len(results)):
        p1, p2 = results[i]
        g1[p1].add(p2)
        g2[p2].add(p1)

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        chk = True
        dfs(g1, i, visited)
        dfs(g2, i, visited)

        for j in range(1, n + 1):
            if not visited[j]:
                chk = False
        if chk:
            answer += 1
    return answer


def dfs(graph, i, visited):
    visited[i] = True
    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))
