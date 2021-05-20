# BOJ 14500 (테트로미노)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

table = [[[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],
         [[(0, 0), (0, 1), (1, 0), (1, 1)]],
         [[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 2), (1, 2), (1, 1), (1, 0)],
          [(0, 1), (1, 1), (2, 1), (2, 0)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)]],
         [[(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 1), (0, 2), (1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0), (2, 0)],
          [(0, 0), (0, 1), (1, 1), (1, 2)]],
         [[(0, 0), (0, 1), (0, 2), (1, 1)], [(1, 0), (0, 1), (1, 1), (2, 1)], [(0, 1), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (1, 0), (2, 0), (1, 1)]]]


def get_sum(sy, sx, ty, tx):
    s = 0
    for y, x in table[ty][tx]:
        s += graph[sy + y][sx + x]
    return s


def get_max_value():
    res = 0
    for i in range(n):
        for j in range(m):
            if j + 3 < m:
                res = max(res, get_sum(i, j, 0, 0))
            if i + 3 < n:
                res = max(res, get_sum(i, j, 0, 1))
            if i + 1 < n and j + 1 < m:
                res = max(res, get_sum(i, j, 1, 0))
            if i + 2 < n and j + 1 < m:
                for k in range(0, 8, 2):
                    res = max(res, get_sum(i, j, 2, k))
                for k in range(0, 4, 2):
                    res = max(res, get_sum(i, j, 3, k))
                    res = max(res, get_sum(i, j, 4, k + 1))

            if i + 1 < n and j + 2 < m:
                for k in range(0, 8, 2):
                    res = max(res, get_sum(i, j, 2, k + 1))
                for k in range(0, 4, 2):
                    res = max(res, get_sum(i, j, 3, k + 1))
                    res = max(res, get_sum(i, j, 4, k))
    return res


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
print(get_max_value())
