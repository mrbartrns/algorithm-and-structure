# [카카오] 기둥과 보 설치
def check(board, y, x, a):
    if a == 0:
        if x == 0:
            return True
        if y - 1 >= 0 and board[y - 1][x][1] or board[y][x][1]:
            return True
        if x - 1 >= 0 and board[y][x - 1][0]:
            return True
    else:
        if x - 1 >= 0 and board[y][x - 1][0]:
            return True
        if x - 1 >= 0 and y + 1 < len(board) and board[y + 1][x - 1][0]:
            return True
        if (
            y - 1 >= 0
            and board[y - 1][x][1]
            and y + 1 < len(board)
            and board[y + 1][x][1]
        ):
            return True
    return False


def solution(n, build_frame):
    answer = []
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for y, x, a, b in build_frame:
        if b == 1:
            if check(board, y, x, a):
                board[y][x][a] = 1
        else:
            board[y][x][a] = 0
            can_remove = True
            for i in range(len(board)):
                for j in range(len(board)):
                    for k in range(2):
                        if board[i][j][k] and not check(board, i, j, k):
                            can_remove = False
                            break
            if not can_remove:
                board[y][x][a] = 1
    for i in range(len(board)):
        for j in range(len(board)):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i, j, k])
    return answer


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
