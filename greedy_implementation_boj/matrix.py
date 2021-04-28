# BOJ 1080
import sys

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline


def calculate(r, c):
    for y in range(r, r + 3):
        for x in range(c, c + 3):
            if a[y][x] == 1:
                a[y][x] = 0
            else:
                a[y][x] = 1


def check():
    for y in range(n):
        for x in range(n):
            if a[y][x] != b[y][x]:
                return False
    return True


n, m = map(int, si().split())
a = [list(map(int, list(si().strip()))) for _ in range(n)]
b = [list(map(int, list(si().strip()))) for _ in range(n)]

if n >= 3 and m >= 3:
    flag = False
    cnt = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if check():
                flag = True
                break

            if a[i][j] != b[i][j]:
                calculate(i, j)
            cnt += 1

    if check():
        flag = True

    print(cnt if flag else -1)
else:
    flag = True
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                flag = False
                break
    print(0 if flag else -1)

#
# for i in range(n):
#     print(a[i])
#
# for i in range(n):
#     print(b[i])
