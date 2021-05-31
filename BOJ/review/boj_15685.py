# BOJ 15685 (드래곤 커브)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def make_directions(init_d, gen):
    curve = [init_d]
    for _ in range(gen):
        new_curve = list(map(lambda x: (x + 1) % 4, curve))
        new_curve.reverse()
        curve += new_curve
    return curve


def draw_curve(y, x, curve):
    visited[y][x] = 1
    ny, nx = y, x
    for d in curve:
        ny += dy[d]
        nx += dx[d]
        visited[ny][nx] = 1


def get_squares():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] == 1 and visited[i][j + 1] == 1 and visited[i + 1][j] == 1 and visited[i + 1][j + 1] == 1:
                cnt += 1
    return cnt


N = int(si())
visited = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for _ in range(N):
    c, r, d, g = map(int, si().split())
    dragon_curve = make_directions(d, g)
    draw_curve(r, c, dragon_curve)

print(get_squares())
