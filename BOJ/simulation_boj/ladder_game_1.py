# BOJ 15684
import sys
from itertools import permutations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def is_same_destination(idx, graph):
    # idx는 보드의 인덱스(사다리의 인덱스가 아님)
    x = idx
    for y in range(h):
        if x - 1 >= 0 and graph[y][x - 1]:
            x -= 1

        elif x < n - 1 and graph[y][x]:
            x += 1

    return True if idx == x else False


def backtrack(idx, location):
    if idx == -1:
        return -1

    is_same = True
    for i in range(n):
        if not is_same_destination(i, ladder):
            is_same = False
            break
    if is_same:
        return 3 - idx

    for y, x in location:
        if x - 1 >= 0 and ladder[y][x - 1]:
            continue
        if x + 1 < n - 1 and ladder[y][x + 1]:
            continue

        ladder[y][x] = True
        val = backtrack(idx - 1, location)
        if val > -1:
            return val
        ladder[y][x] = False
    return -1


n, m, h = map(int, si().split())

ladder = [[False for _ in range(n - 1)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, si().split())
    ladder[a - 1][b - 1] = True

same = False
loc = [(i, j) for i in range(h) for j in range(n - 1) if not ladder[i][j]]
locations = list(permutations(loc, 3))
print(locations)
for location in locations:
    res = backtrack(3, location)
    if res > -1:
        same = True
        print(res)
        break
if not same:
    print(-1)
