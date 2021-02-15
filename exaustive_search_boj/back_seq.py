# BOJ 1182
import sys

si = sys.stdin.readline
"""
부분수열
1234
12
13
14
123
134
23
24
234
34
1
2
3
4

"""


def backtrack(idx, s, t):
    if idx == n:
        return

    if s + seq[idx] == t:
        cnt[0] += 1

    # 브루트포스 방식의 dfs
    backtrack(idx + 1, s, t)
    backtrack(idx + 1, s + seq[idx], t)


cnt = [0]
n, m = map(int, si().split())
seq = list(map(int, si().split()))
seq.sort()
visited = [False] * n
sub = []
backtrack(0, 0, m)
print(cnt[0])