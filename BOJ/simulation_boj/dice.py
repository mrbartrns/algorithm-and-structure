# BOJ 14499
import sys

"""
크기가 N * M인 지도가 존재한다.
지도의 오른쪽은 동쪽, 위쪽은 북쪽 -> 이 지도의 위에 주사위가 하나 놓여져 있음
주사위는 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있음
지도의 각 칸에는 정수가 하나씩 쓰여져있음 -> 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
0이 아닌 경우, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여있는 수는 9이 됨
주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여져 있는 값 구하기
"""
si = sys.stdin.readline


def roll(d):
    d1, d2, d3 = dice[1], dice[2], dice[3]
    d4, d5, d6 = dice[4], dice[5], dice[6]

    # d가 0일 경우 동쪽으로 이동하므로
    if d == 0:
        dice[1] = d4
        dice[4] = d6
        dice[6] = d3
        dice[3] = d1
    # d가 1이면 서쪽으로 이동
    elif d == 1:
        dice[1] = d3
        dice[4] = d1
        dice[6] = d4
        dice[3] = d6
    # d가 2이면 북쪽으로 이동
    elif d == 2:
        dice[1] = d5
        dice[2] = d1
        dice[5] = d6
        dice[6] = d2
    # d가 3이면 남쪽으로 이동
    elif d == 3:
        dice[1] = d2
        dice[2] = d6
        dice[5] = d1
        dice[6] = d5


def play(i: int, j: int) -> None:
    x, y = i, j  # location of dice
    for d in orders:
        nx: int = x + dx[d]
        ny: int = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        roll(d)
        # 윗면을 항상 1이라고 고정하면 6은 항상 아랫면이 된다
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[1])
        x, y = nx, ny


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, sx, sy, o = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
orders = list(map(int, si().split()))
orders = list(map(lambda x: (x - 1), orders))

# 다이스 배열을 1차원으로 선언
dice = [0] * 7

play(sx, sy)
