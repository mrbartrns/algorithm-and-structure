# 블록 이동하기
from collections import deque


def solution(board):
    answer = bfs(board)

    return answer


def bfs(board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    que = deque()
    size = len(board)
    visited = [[[False for _ in range(size)] for _ in range(size)] for _ in range(2)]
    que.append((0, 0, 0, 1, 0, 0))
    table = [(-1, 0, -1, 0, 0), (1, 0, 1, 0, 0), (0, -1, 0, -1, 1), (0, 1, 0, 1, 1)]
    while que:
        y1, x1, y2, x2, cnt, t = que.popleft()
        if (y1 == size - 1 and x1 == size - 1) or (y2 == size - 1 and x2 == size - 1):
            return cnt

        # move
        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]
            if (
                ny1 < 0
                or ny1 >= size
                or nx1 < 0
                or nx1 >= size
                or ny2 < 0
                or ny2 >= size
                or nx2 < 0
                or nx2 >= size
            ):
                continue

            if board[ny1][nx1] != 1 and board[ny2][nx2] != 1:
                if not visited[t][ny1][nx1] or not visited[t][ny2][nx2]:
                    visited[t][ny1][nx1] = True
                    visited[t][ny2][nx2] = True
                    que.append((ny1, nx1, ny2, nx2, cnt + 1, t))
            # rotation
        for i in range(4):
            dy1, dx1, dy2, dx2, direction = table[i]
            ny1 = y1 + dy1
            nx1 = x1 + dx1
            ny2 = y2 + dy2
            nx2 = x2 + dx2
            if (
                ny1 < 0
                or ny1 >= size
                or nx1 < 0
                or nx1 >= size
                or ny2 < 0
                or ny2 >= size
                or nx2 < 0
                or nx2 >= size
            ):
                continue
            if t != direction:
                continue

            if t == 0 and board[ny1][nx1] != 1 and board[ny2][nx2] != 1:
                if not visited[1][ny1][x1]:
                    visited[1][ny1][x1] = True
                    que.append((y1, x1, ny1, x1, cnt + 1, 1))
                if not visited[1][ny2][x2]:
                    visited[1][ny2][x2] = True
                    que.append((y2, x2, ny2, x2, cnt + 1, 1))
            elif t == 1 and board[ny1][nx1] != 1 and board[ny2][nx2] != 1:
                if not visited[0][y1][nx1]:
                    visited[0][y1][nx1] = True
                    que.append((y1, x1, y1, nx1, cnt + 1, 0))
                if not visited[0][y2][nx2]:
                    visited[0][y2][nx2] = True
                    que.append((y2, x2, y2, nx2, cnt + 1, 0))


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(solution(board))
