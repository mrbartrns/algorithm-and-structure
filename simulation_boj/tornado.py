# BOJ 20057
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
tornado = [[False for _ in range(n)] for _ in range(n)]
st = (n // 2, n // 2)


# 토네이도의 이동 먼저 구현
def move(start_point):
    y, x = start_point
    d = 0
    scale = 1
    while True:
        t = 0
        print(y, x)
        if y == 0 and x == 0:
            break

        if tornado[y][x]:
            break

        while t < scale:
            ny = y + dy[d]
            nx = x + dx[d]
            if tornado[ny][nx]:
                break
            y = ny
            x = nx
            t += 1

        d = (d + 1) % 4
        if d % 2 == 0:
            scale += 1


move(st)
