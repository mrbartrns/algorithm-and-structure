def solution(n, build_frame):
    board = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    answer = []
    # (y, x), a: {0: 기둥, 1: 보}, b: {0: 삭제, b: 설치}
    for y, x, a, b in build_frame:
        if b == 1 and check(y, x, a, board):
            board[y][x][a] = True
        else:
            board[y][x][a] = False
            for i in range(n + 1):
                for j in range(n + 1):
                    for k in range(2):
                        if board[i][j][k] and not check(i, j, k, board):
                            board[y][x][a] = True
                            break
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i, j, k])
    return answer


def check(y, x, structure, board):
    if structure == 0:
        if (
            x == 0
            or (x - 1 >= 0 and board[y][x - 1][structure])
            or (y - 1 >= 0 and board[y - 1][x][1 - structure])
            or (board[y][x][1 - structure])
        ):
            return True
    if structure == 1:
        if (
            (x - 1 >= 0 and board[y][x - 1][1 - structure])
            or (x - 1 >= 0 and y + 1 < len(board))
            and board[y + 1][x - 1][1 - structure]
            or (
                y + 1 < len(board)
                and board[y + 1][x][structure]
                and y - 1 >= 0
                and board[y - 1][x][structure]
            )
        ):
            return True
    return False


if __name__ == "__main__":
    n = 5
    build_frame = [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1],
    ]
    print(solution(n, build_frame))
