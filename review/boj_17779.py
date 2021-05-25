# BOJ 17779 (게리맨더링)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def make_boundary(y: int, x: int, d1: int, d2: int):
    """
    label "5" boundary on the maps.
    Args:
        y(int): current row of the matrix
        x(int): current column of the matrix
        d1(int): left distance
        d2(int): right distance

    Returns: None

    """
    idx = 0
    while idx <= d1:
        maps[y + idx][x - idx] = 5
        maps[y + d2 + idx][x + d2 - idx] = 5
        idx += 1

    idx = 0
    while idx <= d2:
        maps[y + idx][x + idx] = 5
        maps[y + d1 + idx][x - d1 + idx] = 5
        idx += 1


def fill_label_5(y: int, d1: int, d2: int) -> None:
    """
    fill 5 in the boundary.
    Args:
        y(int): row location of first 5 label
        d1(int): left distance
        d2(int): right distance
    Returns: None

    """
    for i in range(y + 1, y + d1 + d2):
        flag = False
        for j in range(n):
            if maps[i][j] == 5:
                flag = not flag
            if flag:
                maps[i][j] = 5


def fill_label(y, x, d1, d2):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 5:
                continue
            if i < y + d1 and j <= x:
                maps[i][j] = 1

            if i <= y + d2 and x < j < n:
                maps[i][j] = 2

            if y + d1 <= i < n and j < x - d1 + d2:
                maps[i][j] = 3

            if y + d2 < i < n and x - d1 + d2 <= j < n:
                maps[i][j] = 4


def elements() -> list:
    """
    get permutations of elements.

    Returns(list): list of tuple y, x, d1, d2

    """
    ret = []
    for y in range(n):
        for x in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if x - d1 < 0 or x + d2 >= n or y + d1 >= n or y + d2 >= n or y + d1 + d2 >= n:
                        continue
                    ret.append((y, x, d1, d2))
    return ret


def get_sum():
    """
    get sum of population of labeled area.
    Returns(int): diff between maximum population and minimum population

    """
    ret = [0] * 5
    for y in range(n):
        for x in range(n):
            label_number = maps[y][x]
            ret[label_number - 1] += graph[y][x]
    ret.sort()
    return ret[-1] - ret[0]


res = INF
n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

els = elements()
for i in range(len(els)):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    r, c, distance1, distance2 = els[i]
    make_boundary(r, c, distance1, distance2)
    fill_label_5(r, distance1, distance2)
    fill_label(r, c, distance1, distance2)
    s = get_sum()
    res = min(res, s)
print(res)
