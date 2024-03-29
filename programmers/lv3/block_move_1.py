# [카카오] 블록 이동하기
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board):
    que = deque()
    visited = set()
    visited.add((0, 0, 0, 1))
    que.append((0, 0, 0, 1, 0, 0))
    while que:
        y1, x1, y2, x2, state, cnt = que.popleft()

        if (y1 == len(board) - 1 and x1 == len(board) - 1) or (
            y2 == len(board) - 1 and x2 == len(board) - 1
        ):
            return cnt

        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]

            if (
                ny1 < 0
                or ny1 >= len(board)
                or nx1 < 0
                or nx1 >= len(board)
                or ny2 < 0
                or ny2 >= len(board)
                or nx2 < 0
                or nx2 >= len(board)
            ):
                continue

            if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                continue

            if (ny1, nx1, ny2, nx2) not in visited:
                visited.add((ny1, nx1, ny2, nx2))
                que.append((ny1, nx1, ny2, nx2, state, cnt + 1))

            if state != i // 2:
                continue

            if (y1, x1, ny1, nx1) not in visited:
                visited.add((y1, x1, ny1, nx1))
                que.append((y1, x1, ny1, nx1, 1 - state, cnt + 1))

            if (ny2, nx2, y2, x2) not in visited:
                visited.add((ny2, nx2, y2, x2))
                que.append((ny2, nx2, y2, x2, 1 - state, cnt + 1))


if __name__ == "__main__":
    board = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    print(solution(board))
