# BOJ 1495
import sys

si = sys.stdin.readline

n, s, m = map(int, si().split())
dp = [-1] * n
dp[0] = s
