# BOJ 21610
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def move(location, direction, distance):
    for i in range(len(location)):
        y, x = location[i]
        ny = (y + dy[direction] * distance) % n
        nx = (x + dx[direction] * distance) % n
        location[i][0], location[i][1] = ny, nx


def spell(location):
    move_dir_y = [-1, -1, 1, 1]
    move_dir_x = [-1, 1, -1, 1]
    for i in range(len(location)):
        y, x = location[i]
        for d in range(4):
            ny = y + move_dir_y[d]
            nx = x + move_dir_x[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] > 0:
                graph[y][x] += 1


def make_cloud():
    new_cloud = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and graph[y][x] >= 2:
                new_cloud.append([y, x])
                graph[y][x] -= 2
    return new_cloud


def check_water():
    ans = 0
    for y in range(n):
        for x in range(n):
            ans += graph[y][x]
    return ans


n, m = map(int, si().split())
dy = [0, n - 1, n - 1, n - 1, 0, 1, 1, 1]
dx = [n - 1, n - 1, 0, 1, 1, 1, 0, n - 1]
graph = [list(map(int, si().split())) for _ in range(n)]
order = []
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
for _ in range(m):
    d, s = map(int, si().split())
    order.append((d - 1, s))

for i in range(m):
    visited = [[False for _ in range(n)] for _ in range(n)]
    d, s = order[i]
    move(cloud, d, s)
    for r, c in cloud:
        visited[r][c] = True
        graph[r][c] += 1
    # 물복사버그
    spell(cloud)
    cloud = make_cloud()
res = check_water()
print(res)
