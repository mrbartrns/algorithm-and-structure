# BOJ 1695 팰린드롬 만들기 (dp)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N = int(si().strip())
arr = list(map(int, si().strip().split(" ")))
cache = [[0 for _ in range(N)] for _ in range(N)]

for jump in range(N):
    for i in range(N - jump):
        j = i + jump
        cache[i][j] = INF
        if arr[i] == arr[j]:
            cache[i][j] = min(
                cache[i][j], cache[i + 1][j - 1] if i + 1 < N and j - 1 >= 0 else 0
            )
        else:
            cache[i][j] = min(cache[i][j], 1 + cache[i + 1][j] if i + 1 < N else 0)
            cache[i][j] = min(cache[i][j], 1 + cache[i][j - 1] if j - 1 >= 0 else 0)
print(cache[0][N - 1])
