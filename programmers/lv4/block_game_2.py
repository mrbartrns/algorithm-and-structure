# [카카오] 블록 게임
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

INF = 987654321

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


def can_remove(y, x, board):
    for i in range(y + 1):
        if board[i][x] != 0:
            return False
    return True


def bfs(sy, sx, k, visited, board):
    ret = []
    que = deque()
    visited[sy][sx] = True
    que.append((sy, sx))
    ret.append((sy, sx))

    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue

            if board[ny][nx] == k and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx))
                ret.append((ny, nx))

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
                zeros.append((y - min_y, x - min_x))
    for i in range(len(table)):
        if zeros[0] in table[i] and zeros[1] in table[i]:
            return min_y, min_x, max_y, max_x, i


def solution(board):
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    answer = 0
    blocks = {}
    for i in range(len(board)):
        for j in range(len(board)):
            if not visited[i][j] and board[i][j] > 0:
                blocks[board[i][j]] = bfs(i, j, board[i][j], visited, board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 0:
                min_y, min_x, max_y, max_x, t = blocks[board[i][j]]
                check = True
                for y, x in table[t]:
                    if not can_remove(min_y + y, min_x + x, board):
                        check = False
                        break
                if check:
                    for y in range(min_y, max_y + 1):
                        for x in range(min_x, max_x + 1):
                            board[y][x] = 0
                    answer += 1
    return answer


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