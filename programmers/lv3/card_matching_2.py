# 카드 짝 맞추기
"""
1. 주어진 그래프를 문자열 자료형으로 바꾼다.
2. bfs를 한다. 이때, 엔터를 눌렀는지 누르지 않았는지 체크하는 변수 필요하다.
"""
from collections import deque
from os import remove

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def remove_element(b, e):
    b = b.replace(e, "0")
    return b


def end_game(b):
    if b.count("0") == 16:
        return True
    return False


def solution(board, r, c):
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])

    que = deque()
    cnt = 0
    enter = -1
    que.append((r, c, b, cnt, enter))
    s = set()

    while que:
        y, x, b, c, e = que.popleft()
        pos = (4 * y) + x

        if (y, x, b, e) in s:
            continue

        s.add((y, x, b, e))

        if end_game(b):
            return c

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue

            que.append((ny, nx, b, c + 1, e))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while True:
                if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                    ny -= dy[i]
                    nx -= dx[i]
                    break
                if b[ny * 4 + nx] != "0":
                    break

                ny += dy[i]
                nx += dx[i]
            que.append((ny, nx, b, c + 1, e))

        if b[pos] != "0":
            if e == -1:
                n_e = pos
                que.append((y, x, b, c + 1, n_e))
            else:
                if e != pos and b[e] == b[pos]:
                    nb = remove_element(b, b[pos])
                    que.append((y, x, nb, c + 1, -1))
    # return answer


if __name__ == "__main__":
    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    print(solution(board, 0, 1))
