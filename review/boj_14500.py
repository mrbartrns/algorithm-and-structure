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
                s = 0
                for y, x in table[0][0]:
                    s += graph[i + y][j + x]
                res = max(res, s)
            if i + 3 < n:
                s = 0
                for y, x in table[0][1]:
                    s += graph[i + y][j + x]
                res = max(res, s)
            if i + 1 < n and j + 1 < m:
                s = 0
                for y, x in table[1][0]:
                    s += graph[i + y][j + x]
                res = max(res, s)
            if i + 2 < n and j + 1 < m:
                s = 0
                for y, x in table[2][0]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][2]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][4]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][6]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[3][0]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[3][2]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[4][1]:
                    s += graph[i + y][j + x]
                res = max(res, s)
                s = 0
                for y, x in table[4][3]:
                    s += graph[i + y][j + x]
                res = max(res, s)

            if i + 1 < n and j + 2 < m:
                s = 0
                for y, x in table[2][1]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][3]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][5]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[2][7]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[3][1]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[3][3]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[4][0]:
                    s += graph[i + y][j + x]
                res = max(res, s)

                s = 0
                for y, x in table[4][2]:
                    s += graph[i + y][j + x]
                res = max(res, s)
    return res


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
print(get_max_value())
