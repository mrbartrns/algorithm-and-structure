# [카카오] 매출 하락 최소화
INF = 987654321


def solution(sales, links):
    graph = [[] for _ in range(len(sales))]
    dp = [[INF for _ in range(2)] for _ in range(len(sales))]
    for a, b in links:
        graph[a - 1].append(b - 1)

    dfs(0, dp, graph, sales)
    return min(dp[0][0], dp[0][1])


def dfs(cur, dp, graph, sales):
    # leaf로부터 거슬러 올라옴
    leaf = True
    for nxt in graph[cur]:
        leaf = False
        dfs(nxt, dp, graph, sales)

    if leaf:
        dp[cur][0] = 0
        dp[cur][1] = sales[cur]
        return

    s = 0
    min_cost = INF
    attend = True
    for child in graph[cur]:
        s += min(dp[child][0], dp[child][1])
        if dp[child][0] >= dp[child][1]:
            attend = False
        min_cost = min(min_cost, dp[child][1] - dp[child][0])

    dp[cur][1] = sales[cur] + s
    if not attend:
        dp[cur][0] = s
    else:
        dp[cur][0] = s + min_cost


if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales, links))
