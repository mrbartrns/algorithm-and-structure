# [카카오] 카드 짝 맞추기
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(board, r, c):
    que = deque()
    # visited must check whether clicked enter btn or not
    visited = set()  # (r, c, maps, enter)
    string = ""
    for i in range(4):
        for j in range(4):
            string += str(board[i][j])
    que.append((r, c, string, -1, 0))
    visited.add((r, c, string, -1))
    while que:
        y, x, maps, enter, cnt = que.popleft()
        pos = y * 4 + x

        if maps.count("0") == 16:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # move 1 block
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue

            if (ny, nx, maps, enter) not in visited:
                visited.add((ny, nx, maps, enter))
                que.append((ny, nx, maps, enter, cnt + 1))

            # move several blocks
            while True:
                if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                    ny -= dy[i]
                    nx -= dx[i]
                    break
                if maps[ny * 4 + nx] != "0":
                    break
                ny += dy[i]
                nx += dx[i]

            if (ny, nx, maps, enter) not in visited:
                visited.add((ny, nx, maps, enter))
                que.append((ny, nx, maps, enter, cnt + 1))

        # enter
        if enter == -1 and maps[pos] != "0":
            if (y, x, maps, pos) not in visited:
                visited.add((y, x, maps, pos))
                que.append((y, x, maps, pos, cnt + 1))
        elif maps[pos] == maps[enter] and pos != enter:
            new_maps = maps.replace(maps[enter], "0")
            if (y, x, new_maps, -1) not in visited:
                visited.add((y, x, new_maps, -1))
                que.append((y, x, new_maps, -1, cnt + 1))


if __name__ == "__main__":
    board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
    r = 1
    c = 0
    print(solution(board, r, c))