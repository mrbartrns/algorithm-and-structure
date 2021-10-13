# BOJ 13699 점화식
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
# t(1)=t(0)*t(0)=1
# t(2)=t(0)*t(1)+t(1)*t(0)=2
# t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
dp = [0] * 36
dp[0] = 1
for i in range(1, N + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]
print(dp[N])
