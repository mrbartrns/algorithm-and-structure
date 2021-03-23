# BOJ 2108
import sys
from functools import reduce
from bisect import bisect_left, bisect_right

si = sys.stdin.readline

n = int(si())
arr = [int(si()) for _ in range(n)]
arr.sort()
counts = [0] * 8001

# 산술평균
# // 기호를 쓰는것이 아닌 반올림을 해야함
ave = int(round(reduce(lambda acc, cur: acc + cur, arr, 0) / n, 0))
# 중앙값
mid = arr[n // 2]

# 최빈값
for i in range(n):
    counts[arr[i] + 4000] += 1

MAX = max(counts)
idx = counts.index(MAX)
for i in range(len(counts)):
    if MAX == counts[i] and idx < i:
        idx = i
        break

# 범위
coverage = arr[-1] - arr[0]

print(ave)
print(mid)
print(idx - 4000)
print(coverage)