# [카카오] 경주로 건설
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

INF = 987654321


def bfs(sy, sx, sd, visited, board):
    que = deque()
    visited[sy][sx] = 100
    que.append((sy, sx, sd, 100))
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
            if d == i % 2:
                value += 100
            else:
                value += 600

            if visited[ny][nx] >= value:
                visited[ny][nx] = value
                que.append((ny, nx, i % 2, value))
    return visited[len(board) - 1][len(board) - 1]


def solution(board):
    visited = [[INF for _ in range(len(board))] for _ in range(len(board))]
    answer = INF
    visited[0][0] = 0
    for i in range(2):
        if board[i][1 - i] != 1:
            answer = min(answer, bfs(i, 1 - i, 1 - i, visited, board))
    return answer


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(solution(board))