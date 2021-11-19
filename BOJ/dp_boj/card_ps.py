# BOJ 16194 카드 구매하기 2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N = int(si())
cache = [INF] * (N + 1)
cache[0] = 0
arr = list(map(int, si().split(" ")))
for j in range(1, N + 1):
    for i in range(1, N + 1):
        if i - j >= 0:
            cache[i] = min(cache[i], cache[i - j] + arr[j - 1])
    print(cache[N])
