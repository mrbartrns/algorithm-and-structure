import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(y, x):
    if x == m:
        return 0
    if dp[y][x] > -1:
        return dp[y][x]

    dp[y][x] = graph[y][x]
    val = solve(y, x + 1)
    if y - 1 >= 0:
        val = max(val, solve(y - 1, x + 1))
    if y + 1 < n:
        val = max(val, solve(y + 1, x + 1))
    dp[y][x] += val
    return dp[y][x]


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    graph = []
    arr = list(map(int, si().split()))
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(arr[m * i + j])
        graph.append(temp)
    res = 0
    for i in range(n):
        res = max(res, solve(i, 0))
    print(res)
