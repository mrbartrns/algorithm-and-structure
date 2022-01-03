# BOJ 3372 보드 점프
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def memo(y, x):
    if y < 0 or y >= N or x < 0 or x >= N:
        return 0
    if y == N - 1 and x == N - 1:
        return 1
    if cache[y][x] > -1:
        return cache[y][x]
    cache[y][x] = 0
    cache[y][x] += memo(y + board[y][x], x) + memo(y, x + board[y][x])
    return cache[y][x]


N = int(si().strip())
board = []
for _ in range(N):
    arr = list(map(int, si().strip().split(" ")))
    board.append(arr)
cache = [[-1 for _ in range(N)] for _ in range(N)]
print(memo(0, 0))
