# BOJ 15966 군계일학
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N = int(si().strip())
arr = [0] + list(map(int, si().strip().split(" ")))
cache = [0] * (1000001)
for i in range(1, N + 1):
    cache[arr[i]] = max(cache[arr[i]], cache[arr[i] - 1] + 1)
print(max(cache))
