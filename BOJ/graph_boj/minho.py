# BOJ 1507 궁금한 민호
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


# 문제에서 주어진 입력 조건
N = int(si())
dp = [list(map(int, si().split(" "))) for _ in range(N)]
ret = 0

# validate input if it is valid
flag = True
for i in range(N):
    for j in range(i + 1, N):
        check = True
        for k in range(N):
            # pass when i == k or k == j
            if k == i or k == j:
                continue
            # if dp[i][k] + dp[k][j] == dp[i][j], it is not an unique route
            if dp[i][j] == dp[i][k] + dp[k][j]:
                check = False
                break
            # if dp[i][j] > dp[i][k] + dp[k][j], it is invalid graph.
            elif dp[i][j] > dp[i][k] + dp[k][j]:
                flag = False
                break
        if check:
            ret += dp[i][j]
print(ret if flag else -1)
