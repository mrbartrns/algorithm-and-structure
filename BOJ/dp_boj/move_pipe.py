# BOJ 17069 파이프 옮기기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def move(pipe_type, y, x):
    if y >= N or x >= N:
        return 0
    if graph[y][x]:
        return 0
    if pipe_type == 1 and (graph[y - 1][x] or graph[y][x - 1]):
        return 0
    if y == N - 1 and x == N - 1:
        return 1
    if cache[pipe_type][y][x] > -1:
        return cache[pipe_type][y][x]
    cache[pipe_type][y][x] = 0
    if abs(pipe_type - 0) < 2:
        cache[pipe_type][y][x] += move(0, y, x + 1)
    if abs(pipe_type - 1) < 2:
        cache[pipe_type][y][x] += move(1, y + 1, x + 1)
    if abs(pipe_type - 2) < 2:
        cache[pipe_type][y][x] += move(2, y + 1, x)
    return cache[pipe_type][y][x]


N = int(si().strip())
graph = [list(map(int, si().strip().split(" "))) for _ in range(N)]
cache = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(3)]
move(0, 0, 1)
print(cache[0][0][1])
