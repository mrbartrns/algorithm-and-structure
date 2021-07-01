# 카드 짝 맞추기
"""
카드 16장 -> 모든 카드를 없애기
큐에 집어넣어야 할 것 -> 현재 보드 상태, 현재 좌표, 누른 횟수
현재 위치가 0보다 크다면 누를수 있다는 뜻이므로, 누르는 경우에 대해서도 따로 처리가 필요
"""
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def remove_element(b, e):
    return b.replace(e, "0")


def solution(board, r, c):
    endpoint = ""
    for i in range(4):
        for j in range(4):
            endpoint += str(board[i][j])
    que = deque()
    visited = set()
    que.append((r, c, endpoint, 0, -1))
    while que:
        y, x, endpoint, cnt, enter = que.popleft()
        pos = y * 4 + x

        if endpoint.count("0") == 16:
            return cnt

        if (y, x, endpoint, enter) in visited:
            continue

        visited.add((y, x, endpoint, enter))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue
            que.append((ny, nx, endpoint, cnt + 1, enter))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while True:
                if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                    ny -= dy[i]
                    nx -= dx[i]
                    break

                if endpoint[ny * 4 + nx] != "0":
                    break

                ny += dy[i]
                nx += dx[i]
            que.append((ny, nx, endpoint, cnt + 1, enter))

        if endpoint[pos] != "0":
            if enter == -1:
                enter = pos
                que.append((y, x, endpoint, cnt + 1, enter))
            elif pos != enter and endpoint[pos] == endpoint[enter]:
                new_endpoint = remove_element(endpoint, endpoint[pos])
                que.append((y, x, new_endpoint, cnt + 1, -1))

    return -1


if __name__ == "__main__":
    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    r = 0
    c = 1
    print(solution(board, r, c))
