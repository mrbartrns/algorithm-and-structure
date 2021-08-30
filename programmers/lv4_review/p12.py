# [카카오] 매출 하락 최소화
import sys

sys.setrecursionlimit(300001)
INF = 987654321


def solution(sales, links):
    graph = [[] for _ in range(len(sales))]
    for a, b in links:
        graph[a - 1].append(b - 1)
    dp = [[0 for _ in range(2)] for _ in range(len(sales))]
    dfs(0, graph, dp, sales=sales)
    return min(dp[0][0], dp[0][1])


def dfs(node, graph, dp, **kwargs):
    leaf = True
    for i in graph[node]:
        leaf = False
        dfs(i, graph, dp, **kwargs)

    if leaf:
        dp[node][0] = 0
        dp[node][1] = kwargs['sales'][node]
        return

    s = 0
    min_value = INF
    attend = True
    for i in graph[node]:
        s += min(dp[i][0], dp[i][1])
        if dp[i][0] >= dp[i][1]:
            attend = False
        min_value = min(dp[i][1] - dp[i][0], min_value)

    dp[node][1] = s + kwargs['sales'][node]
    if not attend:
        dp[node][0] = s
    else:
        dp[node][0] = s + min_value


if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales, links))
