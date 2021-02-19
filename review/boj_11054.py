# BOJ 11054
import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
arr_re = arr[:]
arr_re.reverse()
dp1 = [1] * n
dp2 = [1] * n


def solve(n):
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

            if arr_re[i] > arr_re[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp2.reverse()
    dp = [dp1[i] + dp2[i] for i in range(n)]
    return max(dp) - 1


print(solve(n))