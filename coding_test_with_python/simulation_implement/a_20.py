# BOJ 18428
import copy
import sys
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def check(board, teacher):
    y, x = teacher

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        while True:
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                break

            if board[ny][nx] == "O":
                break

            if board[ny][nx] == "S":
                return False

            ny += dy[i]
            nx += dx[i]
    return True


n = int(si())
graph = [list(si().strip().split(" ")) for _ in range(n)]
flag = False
blanks = []
teachers = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            blanks.append((i, j))
        elif graph[i][j] == "T":
            teachers.append((i, j))

comb = combinations(blanks, 3)
for new_walls in comb:
    chk = True
    maps = copy.deepcopy(graph)
    for i, j in new_walls:
        maps[i][j] = "O"

    for teacher in teachers:
        if not check(maps, teacher):
            chk = False
            break
    if chk:
        flag = True
        break

print("YES" if flag else "NO")
