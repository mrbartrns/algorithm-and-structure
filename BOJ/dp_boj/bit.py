# BOJ 2698 인접한 비트의 개수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

cache = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
cache[1][0][0] = 1
cache[1][0][1] = 1

for k in range(100):
    for i in range(2, 101):
        cache[i][k][1] += cache[i - 1][k][0]
        if k - 1 >= 0:
            cache[i][k][1] += cache[i - 1][k - 1][1]
        cache[i][k][0] += cache[i - 1][k][0] + cache[i - 1][k][1]

T = int(si().strip())
for _ in range(T):
    a, b = map(int, si().strip().split(" "))
    print(cache[a][b][0] + cache[a][b][1])
