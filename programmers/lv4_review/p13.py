# [카카오] 블록 게임
from collections import deque

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

table = [{(1, 0), (1, 1)}, {(1, 1), (2, 1)}, {(0, 1), (0, 2)}, {(0, 0), (1, 0)},
         {(1, 1), (1, 2)}, {(0, 1), (1, 1)}, {(0, 0), (0, 1)}, {(1, 0), (2, 0)},
         {(0, 0), (0, 2)}, {(0, 1), (2, 1)}, {(1, 0), (1, 2)}, {(0, 0), (2, 0)}]


def solution(board):
    blocks = {}
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    answer = 0

    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] > 0 and not visited[y][x]:
                min_y, min_x, max_y, max_x, block_type = bfs(y, x, board[y][x], visited, board)
                blocks[board[y][x]] = (min_y, min_x, max_y, max_x, block_type)
    # 블록타입 저장 후 해야 할 것 -> 다시 배열 돌면서 0이 아닌 블록 찾기
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] > 0:
                chk = True
                min_y, min_x, max_y, max_x, block_type = blocks[board[y][x]]
                for i, j in table[block_type]:
                    if not can_remove(min_y + i, min_x + j, board):
                        chk = False
                        break
                if chk:
                    for i in range(min_y, max_y + 1):
                        for j in range(min_x, max_x + 1):
                            board[i][j] = 0
                    answer += 1
    return answer


def can_remove(y, x, board):
    for i in range(y + 1):
        if board[i][x] > 0:
            return False
    return True


def bfs(y, x, k, visited, board):
    que = deque()
    ret = []
    visited[y][x] = True
    que.append((y, x, k))
    ret.append((y, x))
    while que:
        y, x, k = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(visited) or nx < 0 or nx >= len(visited):
                continue

            if board[ny][nx] != k:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, k))
                ret.append((ny, nx))

    zeros = []
    min_y, min_x, max_y, max_x = INF, INF, 0, 0
    for y, x in ret:
        min_y = min(min_y, y)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        max_x = max(max_x, x)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if board[y][x] != k:
                zeros.append((y, x))

    for i in range(len(table)):
        t_set = table[i]
        if (zeros[0][0] - min_y, zeros[0][1] - min_x) in t_set and (zeros[1][0] - min_y, zeros[1][1] - min_x) in t_set:
            return min_y, min_x, max_y, max_x, i


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
    print(solution(board))
