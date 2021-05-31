# BOJ 2096
import sys

si = sys.stdin.readline

n = int(si())
# graph = [list(map(int, si().split())) for _ in range(n)]
MAX = 1e9
max_dp = [-1, -1, -1]
min_dp = max_dp[:]
for _ in range(n):
    a, b, c = map(int, si().split())
    if max_dp[0] == max_dp[1] == max_dp[2] == -1:
        max_dp[0] = a
        max_dp[1] = b
        max_dp[2] = c
    elif max_dp[0] > -1 and max_dp[1] > -1 and max_dp[2] > -1:
        a1 = a + max(max_dp[0], max_dp[1])
        b1 = b + max(max_dp[0], max_dp[1], max_dp[2])
        c1 = c + max(max_dp[1], max_dp[2])
        max_dp[0], max_dp[1], max_dp[2] = a1, b1, c1

    if min_dp[0] == min_dp[1] == min_dp[2] == -1:
        min_dp[0] = a
        min_dp[1] = b
        min_dp[2] = c
    elif min_dp[0] > -1 and min_dp[1] > -1 and min_dp[2] > -1:
        a1 = a + min(min_dp[0], min_dp[1])
        b1 = b + min(min_dp[0], min_dp[1], min_dp[2])
        c1 = c + min(min_dp[1], min_dp[2])
        min_dp[0], min_dp[1], min_dp[2] = a1, b1, c1

print(max(max_dp), end=" ")
print(min(min_dp))

"""
dp = [graph[0][0], graph[0][1], graph[0][2]]
# MAX
for y in range(1, n):
    dp[0] += max(graph[y][0], graph[y][1])
    dp[1] += max(graph[y][0], graph[y][1], graph[y][2])
    dp[2] += max(graph[y][1], graph[y][2])

print(max(dp))

dp = [graph[0][0], graph[0][1], graph[0][2]]

# MIN
for y in range(1, n):
    dp[0] += min(graph[y][0], graph[y][1])
    dp[1] += min(graph[y][0], graph[y][1], graph[y][2])
    dp[2] += min(graph[y][1], graph[y][2])

print(min(dp))
"""
"""
def solve(n):
    max_dp = [graph[0][0], graph[0][1], graph[0][2]]
    min_dp = max_dp[:]
    for y in range(1, n):
        max_dp[0] += max(graph[y][0], graph[y][1])
        min_dp[0] += min(graph[y][0], graph[y][1])
        max_dp[1] += max(graph[y][0], graph[y][1], graph[y][2])
        min_dp[1] += min(graph[y][0], graph[y][1], graph[y][2])
        max_dp[2] += max(graph[y][1], graph[y][2])
        min_dp[2] += min(graph[y][1], graph[y][2])
    return max_dp, min_dp
"""