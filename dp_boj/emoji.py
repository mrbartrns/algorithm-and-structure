# BOJ 14226
import sys
from collections import deque

si = sys.stdin.readline


def bfs(target):
    que = deque()
    que.append((1, 0, 0))
    while que:
        s, cnt, idx = que.popleft()
        if s == target:
            return cnt
        if dp[cnt][idx] > 0:
            que.append((dp[cnt][idx] + s, cnt + 1, 0))
            dp[cnt + 1][0] = dp[cnt][idx]
        que.append((s, cnt + 1, 1))
        dp[cnt + 1][1] = s
        que.append((s - 1, cnt + 1, 0))


dp = [[0 for _ in range(2)]] * 15
print(bfs(18))
