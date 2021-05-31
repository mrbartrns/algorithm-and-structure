# BOJ 가장 긴 증가하는 부분 수열 4
import sys

si = sys.stdin.readline
n = int(si())
dp1 = [1] * n
arr = list(map(int, si().split()))
dp2 = [[] for _ in range(n)]
for i in range(n):
    dp2[i] = [arr[i]]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
            if len(dp2[i]) < len(dp2[j]):
                dp2[i] = dp2[j] + [arr[i]]
            else:
                dp2[i] = dp2[i]

print(dp1[n - 1])
print(" ".join(list(map(str, dp2[n - 1]))))
