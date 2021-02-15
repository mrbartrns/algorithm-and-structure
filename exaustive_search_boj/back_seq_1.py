# BOJ 1182
import sys

si = sys.stdin.readline


def dfs(idx, s):
    if idx > 0 and s == m:
        counts[0] += 1
        return

    if idx == n:
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, s + seq[i])
            visited[i] = False


n, m = map(int, si().split())
seq = list(map(int, si().split()))
counts = [0]
visited = [False] * n
dfs(0, 0)
print(counts[0])