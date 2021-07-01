# floyd warshall 알고리즘을 이용한 미래도시
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

answer = 0
n, m = map(int, si().split())
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            dp[i][j] = 0

for _ in range(m):
    a, b = map(int, si().split())
    dp[a][b] = 1
    dp[b][a] = 1

x, k = map(int, si().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# floyd-warshall algorithm contains all information of path
answer = dp[1][k] + dp[k][x]
print(answer if answer < INF else -1)
