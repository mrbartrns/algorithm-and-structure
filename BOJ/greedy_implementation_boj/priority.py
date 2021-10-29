# BOJ 2012 순위
"""
1 1 2 3 5
1 2 3 4 5
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N = int(si())
arr = [int(si()) for _ in range(N)]
arr.sort()
ret = 0
for i in range(1, N + 1):
    ret += abs(arr[i - 1] - i)
print(ret)
