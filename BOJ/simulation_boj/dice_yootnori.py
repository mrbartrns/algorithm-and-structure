# BOJ 17825
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dice = list(map(int, si().split()))
"""
graph = [[0, 2, 4, 6, 8, 10],
         [10, 12, 14, 16, 18, 20],
         [22, 24, 26, 28, 30],
         [30, 32, 34, 36, 38, 40],
         [10, 13, 16, 19, 25],
         [20, 22, 24, 25],
         [30, 28, 27, 26, 25],
         [25, 30, 35, 40],
         [40, -1]]
location = [[0, 0], [0, 0], [0, 0], [0, 0]]
"""

value = 0
# graph = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
#          [10, 13, 16, 19, 25],
#          [20, 22, 24, 25],
#          [30, 28, 27, 26, 25],
#          [25, 30, 35, 40],
#          [40, 0]]
graph = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
         [10, 13, 16, 19, 25, 30, 35, 40, 0],
         [20, 22, 24, 25, 30, 35, 40, 0],
         [30, 28, 27, 26, 25, 30, 35, 40, 0]]

visited = [[False] * len(graph[i]) for i in range(len(graph))]


done = [False] * 4
horses = []


def move(horse, dice_number, location):
    """
    1. 먼저 현재 위치의 말의 visited를 False로 바꾼다.
    @param horse: 현재 말의 번호
    @param dice_number: 주사위를 굴릴 번호
    @param location: 말의 위치가 담긴 배열
    @return: None
    @rtype: None
    """
    y, x = location[horse]
    visited[y][x] = False


def backtrack(k):
    if k == 10:
        location = [[0, 0], [0, 0], [0, 0], [0, 0]]
        res = 0
        for i in range(10):
            horse = horses[i]
            dice_number = dice[i]
            if move(horse, dice_number, location):
                y, x = horses[i]
                res += graph[y][x]
        return

    for i in range(4):
        if not done[i]:
            horses.append(i)
            backtrack(k + 1)
            horses.pop()

# def move(horse, dice_number, location):
# y, x = location[horse]
# x += dice_number
# if x < len(graph[y]):
#     if y == 0:
#         if graph[y][x] == 10:
#             y, x = 1, 0
#         elif graph[y][x] == 20:
#             y, x = 2, 0
#         elif graph[y][x] == 30:
#             y, x = 3, 0
#         elif graph[y][x] == 40:
#             y, x = 5, 0
#     elif graph[y][x] == 25:
#         y, x = 4, 0
#
# elif x >= len(graph[y]):
#     if y == 0:
#         x -= len(graph[y]) + 1
#         y = 5
#     if y == 1 or y == 2 or y == 3:
#         x -= len(graph[y]) + 1
#         y = 4
#     if y == 4:
#         x -= len(graph[y]) + 1
#         y = 5
#     if y == 5:
#         done[horse] = True
#         y, x = 5, 1
#         location[horse] = [y, x]
#
# if not done[horse]:
#     pass
