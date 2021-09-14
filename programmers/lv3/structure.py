# [카카오] 기둥과 보 설치
def can_build(y, x, a, board):
    # check if can build pillar
    if a == 0:
        if x == 0:
            return True
        if y - 1 >= 0 and board[y - 1][x][1]:
            return True
        if board[y][x][1]:
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
            and y + 1 < len(board)
            and board[y - 1][x][1]
            and board[y + 1][x][1]
        ):
            return True
    return False


def solution(n, build_frame):
    answer = []
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for y, x, a, b in build_frame:
        # y, x: location
        # a: 기둥(0) or 보(1)
        # b: remove(0) or build(1)
        if b == 1:
            if can_build(y, x, a, board):
                board[y][x][a] = 1
        else:
            board[y][x][a] = 0
            for i in range(len(board)):
                for j in range(len(board)):
                    for k in range(2):
                        if not board[i][j][k]:
                            continue
                        if not can_build(i, j, k, board):
                            board[y][x][a] = 1
                            break

    for y in range(len(board)):
        for x in range(len(board)):
            for k in range(2):
                if board[y][x][k]:
                    answer.append([y, x, k])
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