# BOJ 11399 ATM
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
arr.sort()
s = 0
for i in range(n):
    s += arr[i] * (n - i)
print(s)
