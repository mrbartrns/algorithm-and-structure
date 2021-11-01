# 알고스팟 jumpgame
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def is_able_to_get_end(y, x):
    if y < 0 or y >= N or x < 0 or x >= N:
        return 0

    if y == N - 1 and x == N - 1:
        dp[y][x] = 1
        return dp[y][x]

    if dp[y][x] > -1:
        return dp[y][x]

    # 재귀 호출로 완전 탐색 알고리즘을 구현
    dp[y][x] = 0
    move = adj[y][x]
    dp[y][x] = max(
        dp[y][x], is_able_to_get_end(y + move, x), is_able_to_get_end(y, x + move)
    )
    return dp[y][x]


T = int(si())
for _ in range(T):
    N = int(si())
    adj = [list(map(int, si().strip().split(" "))) for _ in range(N)]
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    ret = is_able_to_get_end(0, 0)
    print("YES" if ret else "NO")
