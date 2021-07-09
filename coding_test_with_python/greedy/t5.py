import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))
dp = [0] * 11
answer = 0
for i in range(n):
    dp[arr[i]] += 1

for i in range(m):
    n -= dp[i]
    answer += dp[i] * n
print(answer)
