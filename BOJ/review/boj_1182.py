# BOJ 1182
import sys

si = sys.stdin.readline


def dfs(s, idx, t):
    if idx == n:
        if s == t:
            cnt[0] += 1
        return
    dfs(s + arr[idx], idx + 1, t)
    dfs(s, idx + 1, t)


n, m = map(int, si().split())
arr = list(map(int, si().split()))
cnt = [0]
dfs(0, 0, m)
if m == 0:
    cnt[0] -= 1
print(cnt[0])