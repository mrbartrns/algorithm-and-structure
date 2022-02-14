# BOJ 2226 이진수
import sys

# sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si().strip())
cache = [0] * 1001
cache[0], cache[1], cache[2] = 1, 0, 1

for i in range(3, N + 1):
    if i % 2 == 1:
        cache[i] = cache[i - 1] * 2 - 1
    else:
        cache[i] = cache[i - 1] * 2 + 1
print(cache[N])
