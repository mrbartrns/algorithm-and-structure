# BOJ 1660 캡틴 이다솜
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


number = 1
cnt = 2
arr = []
while number <= 300000:
    arr.append(number)
    number += cnt
    cnt += 1
memo = []
memo.append(arr[0])
for i in range(1, len(arr)):
    if memo[-1] > 300000:
        break
    memo.append(memo[-1] + arr[i])
INF = 987654321
N = int(si())
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    for j in range(len(memo)):
        if i - memo[j] < 0:
            break
        dp[i] = min(dp[i], dp[i - memo[j]] + 1)
print(dp[N])
