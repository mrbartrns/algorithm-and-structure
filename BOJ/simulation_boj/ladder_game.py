# BOJ 15684
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 4

n, m, h = map(int, si().split())

ladder = [[False for _ in range(n - 1)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, si().split())
    ladder[a - 1][b - 1] = True

res = [INF]


def is_same_destination(idx):
    # idx는 보드의 인덱스(사다리의 인덱스가 아님)
    x = idx
    for y in range(h):
        if x - 1 >= 0 and ladder[y][x - 1]:
            x -= 1

        elif x < n - 1 and ladder[y][x]:
            x += 1

    return True if idx == x else False


def backtrack(cnt, max_cnt, idx):
    if cnt == max_cnt:
        for i in range(n):
            if not is_same_destination(i):
                return
        print(cnt)
        sys.exit(0)

    for i in range(idx, h):
        for j in range(n - 1):
            if not ladder[i][j]:
                if j - 1 >= 0 and ladder[i][j - 1]:
                    continue
                if j + 1 < n - 1 and ladder[i][j + 1]:
                    continue

                ladder[i][j] = True
                backtrack(cnt + 1, max_cnt, i)
                ladder[i][j] = False


for i in range(4):
    backtrack(0, i, 0)
print(-1)
