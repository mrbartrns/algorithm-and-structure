# BOJ 14728 벼락치기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N, T = map(int, si().strip().split(" "))
scores = [0]
times = [0]
cache = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, si().strip().split(" "))
    times.append(a)
    scores.append(b)
for i in range(1, N + 1):
    for j in range(T + 1):
        cache[i][j] = cache[i - 1][j]
        if j - times[i] >= 0:
            cache[i][j] = max(cache[i][j], cache[i - 1][j - times[i]] + scores[i])

print(cache[N][T])
