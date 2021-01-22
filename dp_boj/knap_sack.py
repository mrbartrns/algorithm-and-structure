# 냅색 알고리즘
W = 5  # 배낭의 무게 한도
wt = [2, 3, 4, 5]  # 각 보석의 무게
val = [3, 4, 5, 6]  # 각 보석의 가격
n = 4  # 보석의 수

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]  # dp table을 0으로 초기화


def solve(n, w):
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            # 만약 보석의 무게가 가방의 무게보다 크다면, 이전 dp값을 저장한다.
            if wt[i - 1] <= j:  # 보석은 한번만 순회하기 때문에 i를 사용해야 한다. 즉 가방의 무게만 늘려나간다.
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][w]


print(solve(n, W))
