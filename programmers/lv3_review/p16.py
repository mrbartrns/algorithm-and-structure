# 경주로 건설
from collections import deque

INF = 987654321
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def solution(board):
    size = len(board)
    visited = [[INF for _ in range(size)] for _ in range(size)]
    answer = INF
    visited[0][0] = 0
    for i in range(2):
        y, x = i, 1 - i
        if board[y][x] == 0:
            answer = min(answer, bfs(y, x, i, board, visited))
    return answer


def bfs(y, x, d, board, visited):
    que = deque()
    que.append((y, x, d, 100))
    visited[y][x] = 100
    size = len(board)
    while que:
        y, x, d, cost = que.popleft()
        if y == size - 1 and x == size - 1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= size or nx < 0 or nx >= size:
                continue

            if board[ny][nx] == 1:
                continue

            if d % 2 == i % 2:
                nxt_value = cost + 100
            else:
                nxt_value = cost + 600

            if nxt_value <= visited[ny][nx]:
                visited[ny][nx] = nxt_value
                que.append((ny, nx, i, nxt_value))
    return visited[size - 1][size - 1]


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
    print(solution(board))
