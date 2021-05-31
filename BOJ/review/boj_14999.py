# BOJ 14999
import sys

si = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def roll(direction: int) -> None:
    """
    @d1: int
    @d2: int
    @d3: int
    @d4: int
    @d5: int
    @d6: int
    @return: None
    """
    d1, d2, d3 = dice[1], dice[2], dice[3]
    d4, d5, d6 = dice[4], dice[5], dice[6]
    if direction == 0:
        dice[1] = d4
        dice[3] = d1
        dice[4] = d6
        dice[6] = d3
    elif direction == 1:
        dice[1] = d3
        dice[3] = d6
        dice[4] = d1
        dice[6] = d4
    elif direction == 2:
        dice[1] = d5
        dice[2] = d1
        dice[5] = d6
        dice[6] = d2
    elif direction == 3:
        dice[1] = d2
        dice[2] = d6
        dice[5] = d1
        dice[6] = d5


def play(start_x: int, start_y: int) -> None:
    x = start_x
    y = start_y
    for d in orders:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        roll(d)  # 주사위 굴리기
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[1])
        x, y = nx, ny


dice = [0] * 7
n, m, sx, sy, o = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
orders = list(map(int, si().split()))
orders = list(map(lambda x: x - 1, orders))
play(sx, sy)
