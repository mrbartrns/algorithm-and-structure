# [카카오] 매출 하락 최소화
import sys

sys.setrecursionlimit(1000000)
INF = 987654321


def dfs(node, graph, dp, sales):
    leaf = True
    for child in graph[node]:
        leaf = False
        dfs(child, graph, dp, sales)

    if leaf:
        dp[node][0] = 0
        dp[node][1] = sales[node]
        return

    s = 0
    min_value = INF
    attend = True
    for child in graph[node]:
        s += min(dp[child][0], dp[child][1])
        if dp[child][0] >= dp[child][1]:
            attend = False
        min_value = min(min_value, abs(dp[child][1] - dp[child][0]))

    dp[node][1] = s + sales[node]
    if not attend:
        dp[node][0] = s
    else:
        dp[node][0] = s + min_value


def solution(sales, links):
    graph = [[] for _ in range(len(sales))]
    dp = [[0 for _ in range(2)] for _ in range(len(sales))]
    for a, b in links:
        graph[a - 1].append(b - 1)
    dfs(0, graph, dp, sales)
    return min(dp[0][0], dp[0][1])


if __name__ == "__main__":
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales, links))
