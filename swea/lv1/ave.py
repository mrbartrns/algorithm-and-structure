# SWEA 2072
from functools import reduce

t = int(input())

for tc in range(t):
    arr = list(map(int, input().split()))
    s = reduce(lambda acc, cur: acc + cur, arr, 0)
    ave = s / len(arr)
    ans = int(round(ave, 0))
    print("#" + str(tc + 1), str(ans))