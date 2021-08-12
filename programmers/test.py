from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board):
    visited = [[INF for _ in range(len(board))] for _ in range(len(board))]
    for i in range(2):
        y = i
        x = 1 - i
        d = 1 - i
        if board[y][x] == 0:
            bfs(y, x, d, visited, board)
    return visited[len(board) - 1][len(board) - 1]


def bfs(y, x, d, visited, board):
    que = deque()
    visited[y][x] = 100
    que.append((y, x, d, 100))

    while que:
        y, x, d, cost = que.popleft()

        if y == len(board) - 1 and x == len(board) - 1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board):
                continue

            if board[ny][nx] == 1:
                continue

            value = cost
            if d == i // 2:
                value += 100
            else:
                value += 600

            if value <= visited[ny][nx]:
                visited[ny][nx] = value
                que.append((ny, nx, i // 2, value))


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(board))
