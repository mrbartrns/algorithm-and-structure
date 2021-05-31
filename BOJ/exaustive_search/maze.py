import sys

"""
input: x, y => maze matrix에서 각각 행과 열을 나타냄
return: 1 또는 0을 더한 부분해
"""

"""
def count_route(x, y):
    print("x:", x, "y:", y)
    counts = 0
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return 0

    # 기저사례 1. maze[x][y]가 0이라면, 0을 반환한다. 더 이상 탐색할 필요가 없다.
    if maze[x][y] == 0:
        return counts

    # 기저사례 2. x, y가 행렬의 끝과 같다면, 1을 반환한다. 더이상 탐색할 필요가 없다. 단, 1차적으로 위에서 걸러져야 한다
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return 1

    # 나머지 반복해야 할 부분. 부분해를 받아 전체해를 구성하는 역할을 하고, 조건을 통해 규칙적으로 작업을 분할한다.
    val = 0
    for y in range(4):  # len(dx), len(dy)
        if not has_passed[x][y]:
            has_passed[x][y] = True
            next_x = x + dx[y]
            next_y = y + dy[y]
            temp = count_route(next_x, next_y)
            if val == 0 or (temp > 0 and val > temp):
                val = temp
            has_passed[x][y] = False
    if val > 0:
        counts = 1 + val
        return counts

    return counts


"""


def count_route(x, y):
    print("x:", x, "y:", y)
    counts = 0
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return 0

    # 기저사례 1. maze[x][y]가 0이라면, 0을 반환한다. 더 이상 탐색할 필요가 없다.
    if maze[x][y] == 0:
        return counts

    # 기저사례 2. x, y가 행렬의 끝과 같다면, 1을 반환한다. 더이상 탐색할 필요가 없다. 단, 1차적으로 위에서 걸러져야 한다
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return 1

    # 나머지 반복해야 할 부분. 부분해를 받아 전체해를 구성하는 역할을 하고, 조건을 통해 규칙적으로 작업을 분할한다.
    for i in range(4):  # len(dx), len(dy)
        if not has_passed[x][y]:
            has_passed[x][y] = True
            next_x = x + dx[i]
            next_y = y + dy[i]
            val = count_route(next_x, next_y)
            if val != 0:
                counts = 1 + val
                return counts
            has_passed[x][y] = False

    return counts


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
"""
n, m = map(int, sys.stdin.readline().split())
maze = []
for _ in range(n):
    string = sys.stdin.readline()
    column = [int(x) for x in string if x != "\n"]
    maze.append(column)
"""
# maze = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
# maze = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
# maze = [[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1]]
maze = [
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
]
# maze = [
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
# ]

has_passed = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
sys.stdout.write(str(count_route(0, 0)))
