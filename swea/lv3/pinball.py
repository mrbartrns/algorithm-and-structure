# SWEA 5650 핀볼 게임
import sys

sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
blocks = [[], [2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]


def play(sy, sx, d):
    score = 0
    y, x, d = sy, sx, d
    y += dy[d]
    x += dx[d]
    while True:
        if y < 0 or y >= n or x < 0 or x >= n:
            score += 1
            d = (d + 2) % 4
            y += dy[d]
            x += dx[d]
            continue

        if y == sy and x == sx:
            break

        if board[y][x] == -1:
            break

        if 0 < board[y][x] <= 5:
            d = blocks[board[y][x]][d]
            score += 1

        elif 5 < board[y][x] <= 10:
            for u, v in holes[board[y][x]]:
                if y != u or x != v:
                    y, x = u, v
                    break

        y += dy[d]
        x += dx[d]
    return score


t = int(input())
for tc in range(t):
    answer = 0
    holes = [[] for _ in range(11)]
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # initialize
    for i in range(n):
        for j in range(n):
            if 6 <= board[i][j] <= 10:
                holes[board[i][j]].append((i, j))
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if board[i][j] == 0:
                    val = play(i, j, k)
                    if val > answer:
                        answer = val
    print(f'#{tc + 1} {answer}')
