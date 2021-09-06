# [카카오] 블록 게임
from collections import deque

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

table = [{(1, 0), (1, 1)}, {(1, 1), (2, 1)}, {(0, 1), (0, 2)}, {(0, 0), (1, 0)},
         {(1, 1), (1, 2)}, {(0, 1), (1, 1)}, {(0, 0), (0, 1)}, {(1, 0), (2, 0)},
         {(0, 0), (0, 2)}, {(0, 1), (2, 1)}, {(1, 0), (1, 2)}, {(0, 0), (2, 0)}]


def can_remove(y, x, board):
    for i in range(0, y + 1):
        if board[i][x] != 0:
            return False
    return True


def bfs(y, x, k, visited, board):
    que = deque()
    visited[y][x] = True
    ret = [(y, x)]
    que.append((y, x, k))
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
                que.append((ny, nx, k))
                ret.append((ny, nx))

    min_y, min_x, max_y, max_x = INF, INF, 0, 0
    zeros = []
    for y, x in ret:
        min_y = min(min_y, y)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        max_x = max(max_x, x)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if board[y][x] != k:
                zeros.append((y - min_y, x - min_x))

    for i in range(len(table)):
        if (zeros[0][0], zeros[0][1]) in table[i] and (zeros[1][0], zeros[1][1]) in table[i]:
            return min_y, min_x, max_y, max_x, i


def solution(board):
    answer = 0
    blocks = {}
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board)):
            if not visited[y][x] and board[y][x] > 0:
                blocks[board[y][x]] = bfs(y, x, board[y][x], visited, board)

    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] > 0:
                check = True
                min_y, min_x, max_y, max_x, t = blocks[board[y][x]]
                for i, j in table[t]:
                    if not can_remove(min_y + i, min_x + j, board):
                        check = False
                        break

                if check:
                    for i in range(min_y, max_y + 1):
                        for j in range(min_x, max_x + 1):
                            board[i][j] = 0
                    answer += 1
    return answer


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
    print(solution(board))
