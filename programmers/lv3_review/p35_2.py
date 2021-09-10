# [카카오] 블록 이동하기
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board):
    que = deque()
    visited = [
        [
            [
                [[False for _ in range(len(board))] for _ in range(len(board))]
                for _ in range(len(board))
            ]
            for _ in range(len(board))
        ]
        for _ in range(2)
    ]
    que.append((0, 0, 0, 1, 0, 0))  # y1, x1, y2, x2, d, cnt
    visited[0][0][0][0][1] = True

    while que:
        y1, x1, y2, x2, d, cnt = que.popleft()

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

            if not visited[d][ny1][nx1][ny2][nx2]:
                visited[d][ny1][nx1][ny2][nx2] = True
                que.append((ny1, nx1, ny2, nx2, d, cnt + 1))

            if d != i // 2:
                continue

            if not visited[1 - d][y1][x1][ny1][nx1]:
                visited[1 - d][y1][x1][ny1][nx1] = True
                que.append((y1, x1, ny1, nx1, 1 - d, cnt + 1))

            if not visited[1 - d][y2][x2][ny2][nx2]:
                visited[1 - d][y2][x2][ny2][nx2] = True
                que.append((y2, x2, ny2, nx2, 1 - d, cnt + 1))


if __name__ == "__main__":
    board = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    print(solution(board))