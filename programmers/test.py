def solution(n, build_frame):
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for y, x, a, b in build_frame:
        if b == 1:  # install
            if check(y, x, a, board):
                board[y][x][a] = 1
        else:
            board[y][x][a] = 0
            for i in range(n + 1):
                for j in range(n + 1):
                    for k in range(2):
                        if board[i][j][k] and not check(i, j, k, board):
                            board[y][x][a] = 1

    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i, j, k])
    return answer


def check(y, x, frame, board):
    if frame == 0:  # 기둥
        if (
            x == 0
            or (x - 1 >= 0 and board[y][x - 1][frame])
            or (y - 1 >= 0 and board[y - 1][x][1 - frame])
            or board[y][x][1 - frame]
        ):
            return True
    else:
        if (
            (x - 1 >= 0 and board[y][x - 1][1 - frame])
            or (x - 1 >= 0 and y + 1 < len(board) and board[y + 1][x - 1][1 - frame])
            or (
                y - 1 >= 0
                and y + 1 < len(board)
                and board[y - 1][x][frame]
                and board[y + 1][x][frame]
            )
        ):
            return True
    return False


if __name__ == "__main__":
    n = 5
    build_frame = [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1],
    ]
    print(solution(n, build_frame))