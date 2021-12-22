# BOJ 17212 달나라 토끼를 위한 구매대금 지불 도우미
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N = int(si().strip())
coins = [1, 2, 5, 7]
cache = [INF] * (N + 1)
cache[0] = 0
for i in range(4):
    for j in range(1, N + 1):
        if j - coins[i] >= 0:
            cache[j] = min(cache[j], 1 + cache[j - coins[i]])
print(cache[N])
