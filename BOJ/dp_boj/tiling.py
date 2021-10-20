# BOJ 1793 타일링
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dp = [0] * 251
dp[0], dp[1] = 1, 1
for i in range(2, 251):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]
while True:
    try:
        N = int(si())
        print(dp[N])
    except:
        break
