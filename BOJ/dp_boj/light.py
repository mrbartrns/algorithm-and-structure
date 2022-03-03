# BOJ 5527 전구 장식
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
cache = [[1 for _ in range(3)] for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        if arr[i] != arr[i - 1]:
            cache[i][j] = max(cache[i][j], 1 + cache[i - 1][j])
        if j == 0:
            continue
        if arr[i] == arr[i - 1]:
            cache[i][j] = max(cache[i][j], 1 + cache[i - 1][j - 1])
answer = 0
for i in range(N):
    for j in range(3):
        answer = max(answer, cache[i][j])
print(answer)
