# 경주로 건설
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
INF = 987654321


def solution(board):
    answer = INF
    size = len(board)
    visited = [[INF for _ in range(size)] for _ in range(size)]
    visited[0][0] = 0
    for i in range(2):
        y, x = i, 1 - i
        if board[y][x] == 0:
            answer = min(answer, bfs(board, visited, y, x, i))

    return answer


def bfs(board, visited, r, c, d):
    que = deque()
    que.append((r, c, 100, d))
    visited[r][c] = 100
    size = len(board)
    while que:
        y, x, value, d = que.popleft()

        if y == size - 1 and x == size - 1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= size or nx < 0 or nx >= size:
                continue

            if board[ny][nx] == 1:
                continue

            if i % 2 == d % 2:
                next_value = value + 100
            else:
                next_value = value + 600

            if next_value <= visited[ny][nx]:
                visited[ny][nx] = next_value
                que.append((ny, nx, next_value, i))

    # for i in range(size):
    #     print(visited[i])
    return visited[size - 1][size - 1]


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
    print(solution(board))
