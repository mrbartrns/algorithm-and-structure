# BOJ 2688 줄어들지 않아
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

cache = [[0 for _ in range(10)] for _ in range(65)]
for i in range(10):
    cache[0][i] = 1

for i in range(1, 65):
    for j in range(10):
        cache[i][j] += sum(cache[i - 1][: j + 1])

T = int(si().strip())
for _ in range(T):
    N = int(si().strip())
    print(cache[N][9])
