# [카카오] 블록 게임
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board):
    answer = 0
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    table = [
        {(1, 0), (1, 1)},
        {(1, 1), (2, 1)},
        {(0, 1), (0, 2)},
        {(0, 0), (1, 0)},
        {(1, 1), (1, 2)},
        {(0, 1), (1, 1)},
        {(0, 0), (0, 1)},
        {(1, 0), (2, 0)},
        {(0, 0), (0, 2)},
        {(0, 1), (2, 1)},
        {(1, 0), (1, 2)},
        {(0, 0), (2, 0)},
    ]
    info = {}
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] != 0 and not visited[y][x]:
                info[board[y][x]] = bfs(y, x, board[y][x], board, visited, table)

    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] > 0:
                sy, sx, ey, ex, t = info[board[y][x]]
                chk = True
                for i, j in table[t]:
                    ny = sy + i
                    nx = sx + j
                    for u in range(ny + 1):
                        if board[u][nx] != 0:
                            chk = False
                            break
                if chk:
                    for i in range(sy, ey + 1):
                        for j in range(sx, ex + 1):
                            board[i][j] = 0
                    answer += 1

    return answer


def bfs(y, x, k, board, visited, table):
    ret = []
    que = deque()
    visited[y][x] = True
    que.append((y, x, k))
    ret.append((y, x))
    while que:
        y, x, k = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue

            if board[ny][nx] != k:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                ret.append((ny, nx))
                que.append((ny, nx, k))

    min_y, min_x, max_y, max_x = INF, INF, 0, 0
    for y, x in ret:
        min_y = min(min_y, y)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        max_x = max(max_x, x)

    zeros = []
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if board[y][x] != k:
                zeros.append((y, x))

    for i in range(len(table)):
        if (zeros[0][0] - min_y, zeros[0][1] - min_x) in table[i] and (
                zeros[1][0] - min_y,
                zeros[1][1] - min_x,
        ) in table[i]:
            return min_y, min_x, max_y, max_x, i


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
        [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 5],
    ]
    print(solution(board))
