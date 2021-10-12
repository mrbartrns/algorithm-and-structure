# BOJ 17086 아기상어2
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def get_max_safe_length(graph, sharks):
    answer = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                continue
            ret = INF
            for sy, sx in sharks:
                length = get_length(y, x, sy, sx)
                ret = min(ret, length)
            answer = max(answer, ret)
    return answer


def get_location(graph):
    ret = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ret.append((i, j))
    return ret


def get_length(y1, x1, y2, x2):
    return abs(y2 - y1) + abs(x2 - x1) - min(abs(y2 - y1), abs(x2 - x1))


N, M = map(int, si().split(" "))
graph = [list(map(int, si().split(" "))) for _ in range(N)]
sharks = get_location(graph)
answer = get_max_safe_length(graph, sharks)
print(answer)
