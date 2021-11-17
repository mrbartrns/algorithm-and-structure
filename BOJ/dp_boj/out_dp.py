# BOJ 15486 퇴사2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N = int(si())
t = [0] * (N + 1)
p = [0] * (N + 1)
for i in range(N, 0, -1):
    t[i], p[i] = map(int, si().split(" "))
cache = [0] * (N + 1)
cache[1] = p[1] if i - t[1] >= 0 else 0
for i in range(2, N + 1):
    cache[i] = max(cache[i - 1], p[i] + cache[i - t[i]] if i - t[i] >= 0 else 0)
print(cache[N])
