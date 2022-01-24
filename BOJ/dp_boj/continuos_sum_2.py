# BOJ 13398 연속합2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
cache = [[0, 0] for _ in range(N)]
cache[0][0] = arr[0]
cache[0][1] = -INF
for i in range(1, N):
    cache[i][0] = max(cache[i - 1][0] + arr[i], arr[i])
    cache[i][1] = max(cache[i - 1][1] + arr[i], cache[i - 1][0])
answer = -INF
for i in range(N):
    for j in range(2):
        answer = max(answer, cache[i][j])
print(answer)
