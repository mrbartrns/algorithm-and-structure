# 활주로 건설
import sys

sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def check_col():
    steps = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    for j in range(n):
        height = board[0][j]
        check = True
        for i in range(n):
            if height == board[i][j]:
                continue

            if abs(height - board[i][j]) > 1:
                check = False
                break

            if board[i][j] > height:
                if i - x < 0:
                    check = False
                    break

                for k in range(i - x, i):
                    if board[k][j] != height:
                        check = False
                        break
                    if steps[k][j] > 0:
                        check = False
                        break
                    steps[k][j] += 1
            else:
                if i + x > n:
                    check = False
                    break
                height -= 1
                for k in range(i, i + x):
                    if board[k][j] != height:
                        check = False
                        break
                    if steps[k][j] > 0:
                        check = False
                        break
                    steps[k][j] += 1
            height = board[i][j]
        if check:
            answer += 1
    return answer


def check_row():
    steps = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    for i in range(n):
        height = board[i][0]
        check = True
        for j in range(n):
            if height == board[i][j]:
                continue

            if abs(height - board[i][j]) > 1:
                check = False
                break

            if board[i][j] > height:
                if j - x < 0:
                    check = False
                    break

                for k in range(j - x, j):
                    if board[i][k] != height:
                        check = False
                        break
                    if steps[i][k] > 0:
                        check = False
                        break
                    steps[i][k] += 1
            else:
                if j + x > n:
                    check = False
                    break

                height -= 1
                for k in range(j, j + x):
                    if board[i][k] != height:
                        check = False
                        break
                    if steps[i][k] > 0:
                        check = False
                        break
                    steps[i][k] += 1
            height = board[i][j]
        if check:
            answer += 1
    return answer


t = int(input())
for tc in range(t):
    answer = 0
    n, x = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer += check_row()
    answer += check_col()
    print(f'#{tc + 1} {answer}')
