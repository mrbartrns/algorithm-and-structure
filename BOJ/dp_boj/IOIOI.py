# BOJ 5525
import sys

si = sys.stdin.readline

n = int(si())
m = int(si())
s: str = si().strip()
dp = [0] * (len(s) + 2)
idx = 0
cnt = 0

"""
연속된 IOI의 길이를 구하기
"""
while True:
    check = s.find("IOI", idx)
    if check <= -1:
        break
    else:
        dp[check + 2] = dp[check] + 1
        idx = check + 2

for i in range(len(dp)):
    if dp[i] >= n:
        cnt += 1
print(cnt)
