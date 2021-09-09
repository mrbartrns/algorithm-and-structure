# 경사로
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def check_row():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        check = True
        last = board[i][0]
        for j in range(n):
            if board[i][j] == last:
                continue
            if abs(board[i][j] - last) > 1:
                check = False
                break
            if board[i][j] > last:
                if j - l < 0:
                    check = False
                    break
                for k in range(j - l, j):
                    if board[i][k] != last:
                        check = False
                        break
                    if visited[i][k]:
                        check = False
                        break
                    visited[i][k] = 1
            else:
                if j + l > n:
                    check = False
                    break
                last -= 1
                for k in range(j, j + l):
                    if board[i][k] != last:
                        check = False
                        break
                    if visited[i][k]:
                        check = False
                        break
                    visited[i][k] = 1
            last = board[i][j]
        if check:
            cnt += 1
    return cnt


def check_col():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        check = True
        last = board[0][j]
        for i in range(n):
            if board[i][j] == last:
                continue
            if abs(board[i][j] - last) > 1:
                check = False
                break
            if board[i][j] > last:
                if i - l < 0:
                    check = False
                    break
                for k in range(i - l, i):
                    if board[k][j] != last:
                        check = False
                        break
                    if visited[k][j]:
                        check = False
                        break
                    visited[k][j] = 1
            else:
                if i + l > n:
                    check = False
                    break
                last -= 1
                for k in range(i, i + l):
                    if board[k][j] != last:
                        check = False
                        break
                    if visited[k][j]:
                        check = False
                        break
                    visited[k][j] = 1

            last = board[i][j]
        if check:
            cnt += 1
    return cnt


n, l = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
print(check_row() + check_col())