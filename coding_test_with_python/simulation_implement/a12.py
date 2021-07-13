def solution(n, build_frame):
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for y, x, a, b in build_frame:
        if b == 1:
            if check(y, x, a, board):
                board[y][x][a] = 1
        else:
            board[y][x][a] = 0
            for i in range(len(board)):
                for j in range(len(board)):
                    for k in range(2):
                        if board[i][j][k] and not check(i, j, k, board):
                            board[y][x][a] = 1
                            break
        for i in range(len(board)):
            print(board[i])
        print()
    ret = []
    for y in range(n + 1):
        for x in range(n + 1):
            for k in range(2):
                if board[y][x][k]:
                    ret.append([y, x, k])
    return ret


def check(y, x, structure, board):
    if structure == 0:
        if (
            x == 0
            or (x - 1 >= 0 and board[y][x - 1][structure])
            or (board[y][x][1 - structure])
            or (y - 1 >= 0 and board[y - 1][x][1 - structure])
        ):
            return True

    if structure == 1:
        if (
            (x - 1 >= 0 and board[y][x - 1][1 - structure])
            or (
                x - 1 >= 0 and y + 1 < len(board) and board[y + 1][x - 1][1 - structure]
            )
            or (
                y - 1 >= 0
                and board[y - 1][x][structure]
                and y + 1 < len(board)
                and board[y + 1][x][structure]
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
