# BOJ 10815
import sys
from bisect import bisect_left, bisect_right


si = sys.stdin.readline

m = int(si())
m_arr = list(map(int, si().split()))
n = int(si())
n_arr = list(map(int, si().split()))
"""
m = 10
n = 8
m_arr = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
n_arr = [10, 9, -5, 2, 3, 4, 5, -10]
"""
m_arr.sort()
res = [0] * n
for i in range(n):
    res[i] = bisect_right(m_arr, n_arr[i]) - bisect_left(m_arr, n_arr[i])

sys.stdout.write(" ".join(list(map(str, res))))
