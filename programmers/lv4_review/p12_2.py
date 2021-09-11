# [카카오] 매출 하락 최소화
import sys

sys.setrecursionlimit(300001)
INF = 987654321


def dfs(dp, node, sales, graph):
    leaf = True
    for nxt in graph[node]:
        leaf = False
        dfs(dp, nxt, sales, graph)

    if leaf:
        dp[node][0] = 0
        dp[node][1] = sales[node]
        return

    attend = True
    s = 0
    min_value = INF
    for child in graph[node]:
        s += min(dp[child][0], dp[child][1])
        if dp[child][0] >= dp[child][1]:
            attend = False
        min_value = min(min_value, dp[child][1] - dp[child][0])

    dp[node][1] = s + sales[node]
    if not attend:
        dp[node][0] = s
    else:
        dp[node][0] = s + min_value


def solution(sales, links):
    dp = [[0 for _ in range(2)] for _ in range(len(sales))]
    graph = [[] for _ in range(len(sales))]
    for a, b in links:
        graph[a - 1].append(b - 1)
    dfs(dp, 0, sales, graph)
    return min(dp[0][0], dp[0][1])


if __name__ == "__main__":
    sales = [5, 6, 5, 1, 4]
    links = [[2, 3], [1, 4], [2, 5], [1, 2]]
    print(solution(sales=sales, links=links))