# [카카오] 기둥과 보 설치
def solution(n, build_frame):
    """

    Args:
        n: size of board
        build_frame: [y, x, 0: 기둥 | 1: 보, 0: 삭제 | 1: 설치]

    Returns: state of board

    """
    answer = []
    board = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    for y, x, structure, op in build_frame:
        if op == 1 and check(y, x, structure, board):
            board[y][x][structure] = True
        elif op == 0:
            board[y][x][structure] = False
            for i in range(n + 1):
                for j in range(n + 1):
                    for k in range(2):
                        if not board[i][j][k]:
                            continue
                        if not check(i, j, k, board):
                            board[y][x][structure] = True
                            break

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i, j, k])
    return answer


def check(y, x, structure, graph):
    if structure == 0:
        if (
            x == 0
            or (x - 1 >= 0 and graph[y][x - 1][structure])
            or (y - 1 >= 0 and graph[y - 1][x][1 - structure])
            or graph[y][x][1 - structure]
        ):
            return True
    else:
        # 기둥이 있거나
        if (
            (x - 1 >= 0 and graph[y][x - 1][1 - structure])
            or (
                x - 1 >= 0 and y + 1 < len(graph) and graph[y + 1][x - 1][1 - structure]
            )
            or (
                y - 1 >= 0
                and y + 1 < len(graph)
                and graph[y - 1][x][structure]
                and graph[y + 1][x][structure]
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
