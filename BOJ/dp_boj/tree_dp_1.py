# BOJ 15681 트리와 쿼리
# visited 를 이용하지 않고 트리의 성질만을 이용하여 dfs하기
import sys

sys.setrecursionlimit(100000)

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def dfs(cur_node, root, dp):
    dp[cur_node] += 1
    for next_node in graph[cur_node]:
        if next_node != root:
            dp[cur_node] += dfs(next_node, cur_node, dp)
    return dp[cur_node]


n, r, q = map(int, si().split())
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r, -1, dp)
for _ in range(q):
    print(dp[int(si())])
