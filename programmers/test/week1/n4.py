"""
캐릭터 A와 캐릭터 B가 정사각형 격자 위에 서있다.
캐릭터는 상하좌우 방향으로 움직일 수 있다.
한번 움직이면, 다시는 해당 위치로 이동이 불가능하다.
"""

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board: list[list[int]], aloc: list[int], bloc: list[int]):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


def in_range(board: list[list[int]], y: int, x: int):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return False
    return True


def is_finished(board: list[list[int]], y: int, x: int):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True


def solve(board, y1, x1, y2, x2):
    # can_win, turn
    if is_finished(board, y1, x1):
        return [False, 0]

    # 서로 두 위치가 같을 때 이번 턴에 움직이면 무조건 이기므로
    if y1 == y2 and x1 == x2:
        return [True, 1]

    min_turn = INF
    max_turn = 0
    can_win = False

    # dfs
    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue

        board[y1][x1] = 0
        result = solve(board, y2, x2, ny, nx)  # 차례가 바뀌기 때문에 위치를 바꿔준다.
        board[y1][x1] = 1

        # 이 시점에서는 result[0]이 False여야만 현재 턴에서 내가 이길 수 있다.
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])

    turn = min_turn if can_win else max_turn

    return [can_win, turn + 1]


board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
# board = [[1, 1, 1, 1, 1]]
# aloc = [0, 0]
# bloc = [0, 4]
print(solution(board, aloc, bloc))
