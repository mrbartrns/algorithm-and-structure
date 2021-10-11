# BOJ 16954
from collections import deque
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

INF = 987654321
dy = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dx = [0, -1, -1, -1, 0, 1, 1, 1, 0]


def get_new_maps(maps):
    """새로운 그래프를 반환하는 함수"""
    string = maps[:56]
    string = "........" + string
    return string


def make_string_graph(graph):
    """string graph를 만드는 함수"""
    string = ""
    for i in range(8):
        for j in range(8):
            string += graph[i][j]
    return string


def bfs(graph):
    """두 지점간 최소 거리를 탐색하는 함수"""
    # 그래프를 따로 처리하기로 했으면 visited는 어떻게 처리해야 할까?
    que = deque()
    visited[7][0] = True
    string_graph = make_string_graph(graph)
    que.append((7, 0, string_graph))
    while que:
        y, x, maps = que.popleft()

        if y == 0 and x == 7:
            return 1

        for i in range(9):
            ny = y + dy[i]
            nx = x + dx[i]

            pos = ny * 8 + nx

            if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
                continue

            if maps[pos] == "#":
                continue

            if not visited[ny][nx] or (ny == y and nx == x):
                # maps를 변화시킴
                new_maps = get_new_maps(maps)
                if new_maps[pos] == ".":
                    visited[ny][nx] = True
                    que.append((ny, nx, new_maps))
    return 0


graph = [list(si().strip()) for _ in range(8)]
# graph = [
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     ["#", ".", ".", ".", ".", ".", ".", "."],
#     [".", "#", ".", ".", ".", ".", ".", "."],
#     [".", "3", ".", ".", ".", ".", ".", "."],
# ]
visited = [[False for _ in range(8)] for _ in range(8)]
print(bfs(graph))
