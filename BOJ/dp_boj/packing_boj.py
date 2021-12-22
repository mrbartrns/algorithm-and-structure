# BOJ 12865 평범한 배낭
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N, V = map(int, si().strip().split(" "))
cache = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
prefer = []
volume = []
for i in range(N):
    a, b = map(int, si().strip().split(" "))
    volume.append(a)
    prefer.append(b)
for i in range(1, N + 1):
    for j in range(1, V + 1):
        if j - volume[i - 1] >= 0:
            cache[i][j] = max(
                cache[i - 1][j], cache[i - 1][j - volume[i - 1]] + prefer[i - 1]
            )
        else:
            cache[i][j] = cache[i - 1][j]
answer = 0
for i in range(1, N + 1):
    answer = max(cache[i])
print(answer)
