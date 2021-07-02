# [카카오] 블록 이동하기
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board):
    n = len(board)
    que = deque()
    visited = [[[False for _ in range(n)] for _ in range(n)] for _ in range(2)]
    visited[0][0][0], visited[0][0][1] = False, False
    que.append((0, 0, 0, 1, 0, 0))
    while que:
        y1, x1, y2, x2, cnt, t = que.popleft()
        if (y1 == n - 1 and x1 == n - 1) or (y2 == n - 1 and x2 == n - 1):
            return cnt

        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]

            if ny1 < 0 or ny1 >= n or nx1 < 0 or nx1 >= n or ny2 < 0 or ny2 >= n or nx2 < 0 or nx2 >= n:
                continue

            if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                continue

            if not visited[t][ny1][nx1] or not visited[t][ny2][nx2]:
                visited[t][ny1][nx1] = True
                visited[t][ny2][nx2] = True
                que.append((ny1, nx1, ny2, nx2, cnt + 1, t))

            if t != i // 2:
                continue

            if t == 0 and not visited[1][ny2][x1]:
                visited[1][y1][x1] = True
                visited[1][ny2][x1] = True
                que.append((y1, x1, ny2, x1, cnt + 1, 1))
            if t == 0 and not visited[1][ny1][x2]:
                visited[1][y2][x2] = True
                visited[1][ny1][x2] = True
                que.append((ny1, x2, y2, x2, cnt + 1, 1))
            if t == 1 and not visited[0][y1][nx2]:
                visited[0][y1][x1] = True
                visited[0][y1][nx2] = True
                que.append((y1, x1, y1, nx2, cnt + 1, 0))
            if t == 1 and not visited[0][y2][nx1]:
                visited[0][y2][x2] = True
                visited[0][y2][nx1] = True
                que.append((y2, nx1, y2, x2, cnt + 1, 0))


if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
