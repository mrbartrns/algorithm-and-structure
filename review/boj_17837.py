# BOJ 17837 (새로운 게임 2)
import sys
from collections import deque

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def change_direction(y, x, direction):
    """
    change horse's direction.
    Args:
        y(int): row of horse
        x(int): column of horse

    Returns(tuple): new location of horse and direction (y, x, direction)

    """
    if direction == 0:
        direction = 1
    elif direction == 1:
        direction = 0
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 2
    ny = y + dy[direction]
    nx = x + dx[direction]

    return ny, nx, direction


def move(idx: int) -> None:
    """
    move horse by index.
    Args:
        idx(int): index of horses

    Returns: None

    """
    que = deque()
    y, x = locations[idx]
    direction = directions[idx]
    stack = maps[y][x]
    while stack[-1] != idx:
        el = stack.pop()
        que.appendleft(el)
    el = stack.pop()
    que.appendleft(el)

    ny = y + dy[direction]
    nx = x + dx[direction]
    # 현재 큐가 채워진 상태

    if (ny < 0 or ny >= n or nx < 0 or nx >= n) or graph[ny][nx] == 2:
        ny, nx, direction = change_direction(y, x, direction)
        directions[idx] = direction

    # ny, nx가 맵 밖이거나 2일때는 현재 위치에 다시 집어넣기
    if (ny < 0 or ny >= n or nx < 0 or nx >= n) or graph[ny][nx] == 2:
        while que:
            el = que.popleft()
            maps[y][x].append(el)
    elif graph[ny][nx] == 0:
        while que:
            el = que.popleft()
            locations[el] = [ny, nx]
            maps[ny][nx].append(el)
    elif graph[ny][nx] == 1:
        while que:
            el = que.pop()
            locations[el] = [ny, nx]
            maps[ny][nx].append(el)


n, k = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
maps = [[[] for _ in range(n)] for _ in range(n)]
locations = [[0, 0] for _ in range(k)]
directions = [0] * k

time = 1
chk = False
for i in range(k):
    r, c, d = map(int, si().split())
    locations[i] = [r - 1, c - 1]
    directions[i] = d - 1
    maps[r - 1][c - 1].append(i)

while time <= 1000:
    for i in range(k):
        move(i)
        cur_r, cur_c = locations[i]
        if len(maps[cur_r][cur_c]) >= 4:
            chk = True
            break
    if chk:
        break
    time += 1
print(time if chk else -1)

if __name__ == "__main__":
    print("hello")
