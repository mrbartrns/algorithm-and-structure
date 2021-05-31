# BOJ 16235
import sys

si = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    for y in range(n):
        for x in range(n):
            trees[y][x].sort(key=lambda t: t[0])
            tree = trees[y][x]
            size = len(tree)
            for i in range(size):
                if land[y][x] - tree[i][0] >= 0:
                    land[y][x] -= tree[i][0]
                    tree[i][0] += 1
                else:
                    tree[i][1] = True


def summer():
    for y in range(n):
        for x in range(n):
            tree = trees[y][x]
            size = len(tree)
            for _ in range(size):
                if tree[-1][1]:
                    land[y][x] += tree[-1][0] // 2
                    tree.pop()
                else:
                    break


def fall():
    for y in range(n):
        for x in range(n):
            tree = trees[y][x]
            size = len(tree)
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                for i in range(size):
                    if tree[i][0] % 5 == 0:
                        trees[ny][nx].append([1, False])


def winter():
    for y in range(n):
        for x in range(n):
            land[y][x] += fertilizer[y][x]


def check():
    cnt = 0
    for y in range(n):
        for x in range(n):
            tree = trees[y][x]
            size = len(tree)
            for i in range(size):
                if not tree[i][1]:
                    cnt += 1
    return cnt


n, m, k = map(int, si().split())
# n, m, k = 5, 2, 6
land = [[5 for _ in range(n)] for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
fertilizer = []
year = 0
for _ in range(n):
    fertilizer.append(list(map(int, si().split())))
# fertilizer = [[2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2], ]
# trees[1][0].append([3, False])
# trees[2][1].append([3, False])
for _ in range(m):
    r, c, y = map(int, si().split())
    trees[r - 1][c - 1].append([y, False])

while year < k:
    year += 1
    spring()
    summer()
    fall()
    winter()
print(check())
