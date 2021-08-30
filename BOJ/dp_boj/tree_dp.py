# BOJ 15681 트리와 쿼리
import sys

sys.setrecursionlimit(100000)

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def get_subtree_count(node, parent):
    dp[node] = 1
    for child in graph[node]:
        if child != parent:
            dp[node] += get_subtree_count(child, node)
    return dp[node]


n, r, q = map(int, si().split())
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

get_subtree_count(r, -1)
for _ in range(q):
    print(dp[int(si())])
