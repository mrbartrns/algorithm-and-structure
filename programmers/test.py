import heapq

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
INF = 987654321


def solution(board):
    visited = [[INF for _ in range(len(board))] for _ in range(len(board))]
    visited[0][0] = 0
    for i in range(2):
        y = i
        x = 1 - i
        d = i
        if board[y][x] == 0:
            dijkstra(y, x, d, board, visited)
    return visited[len(board) - 1][len(board) - 1]


def dijkstra(y, x, d, board, visited):
    q = []
    visited[y][x] = 100
    heapq.heappush(q, (100, y, x, d))
    while q:
        cost, y, x, d = heapq.heappop(q)

        if visited[y][x] < cost:
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

            if value < visited[ny][nx]:
                visited[ny][nx] = value
                heapq.heappush(q, (value, ny, nx, i % 2))


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
    print(solution(board))
