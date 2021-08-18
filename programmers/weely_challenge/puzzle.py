# 퍼즐 조각 채우기
import copy
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

INF = 987654321


def solution(game_board, table):
    blanks, _ = get_cubes(game_board, 0)
    blocks, counts = get_cubes(table, 1)
    answer = []
    visited = [False] * len(blocks)
    for i in range(len(blanks)):
        check = False
        for j in range(len(blocks)):
            if visited[j]:
                continue
            block = blocks[j]
            for _ in range(4):
                block = rotate(block)
                if can_cover(blanks[i], block):
                    answer.append(j)
                    check = True
                    visited[j] = True
                    break
            if check:
                break
    return get_count(answer, counts)


def get_cubes(board, t):
    ret = []
    counts = []
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == t and not visited[y][x]:
                cube, cnt = bfs(y, x, visited, board)
                ret.append(cube)
                counts.append(cnt)
    return ret, counts


def bfs(y, x, visited, board):
    res = []
    n = board[y][x]
    min_y, min_x, max_y, max_x = INF, INF, 0, 0
    que = deque()
    que.append((y, x, n))
    visited[y][x] = True
    res.append((y, x))
    while que:
        y, x, v = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue

            if board[ny][nx] != v:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, v))
                res.append((ny, nx))

    for y, x in res:
        min_y = min(min_y, y)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        max_x = max(max_x, x)

    ret = [[1 - n for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for y, x in res:
        ret[y - min_y][x - min_x] = n
    return ret, len(res)


def rotate(block):
    ret = []
    for j in range(len(block[0])):
        temp = []
        for i in range(len(block) - 1, -1, -1):
            temp.append(block[i][j])
        ret.append(temp)
    return ret


def can_cover(blank, block):
    if len(block) != len(blank) or len(block[0]) != len(blank[0]):
        return False

    ret = copy.deepcopy(blank)
    for y in range(len(block)):
        for x in range(len(block[0])):
            ret[y][x] += block[y][x]

    for y in range(len(blank)):
        for x in range(len(blank[0])):
            if ret[y][x] != 1:
                return False
    return True


def get_count(result, counts):
    ret = 0
    for block in result:
        ret += counts[block]
    return ret


if __name__ == "__main__":
    game_board = [
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
    ]
    table = [
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
    ]
    print(solution(game_board, table))
