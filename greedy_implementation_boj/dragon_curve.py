# BOJ 15685
import sys

si = sys.stdin.readline


def set_directions(directions: list, cnt: int) -> list:
    if cnt == 0:
        return directions
    temp = list(map(lambda x: (x + 1) % 4, directions))
    temp.reverse()
    return set_directions(directions + temp, cnt - 1)


def draw(directions, y, x):
    graph[y][x] = True
    directions_length = len(directions)
    for i in range(directions_length):
        d = directions[i]
        nx = x + dx[d]
        ny = y + dy[d]
        graph[ny][nx] = True
        x, y = nx, ny


def check():
    cnt = 0
    for y in range(1, 101):
        for x in range(1, 101):
            if graph[y][x] and graph[y - 1][x] and graph[y][x - 1] and graph[y - 1][x - 1]:
                cnt += 1
    return cnt


graph = [[False for _ in range(101)] for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(si())
for _ in range(n):
    init_x, init_y, d, g = map(int, si().split())
    init_directions = [d]
    dragon_curve = set_directions(init_directions, g)
    draw(dragon_curve, init_y, init_x)
ans = check()
print(ans)
