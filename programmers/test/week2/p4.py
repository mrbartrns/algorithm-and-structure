"""
건물은 파괴되었다가 회복 스킬을 받아 내구도가 1 이상이 되면 파괴되지 않은 상태가 된다.
최종적으로 파괴되지 않은 건물들의 개수를 구한다.

누적합을 이용한다.
- 누적합은 시간 복잡도를 줄일 수 있다.
- 해당 범위 내에서 동일한 변화량을 가져야한다.
- 크기 + 1을 해야만 원하는 누적합을 구할 수 있다.
- 2차원 누적합 역시 동일한 방식으로 동작한다.
"""


def accumulate(board):
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            board[i][j] += board[i][j - 1]
    for i in range(1, len(board)):
        for j in range(len(board[0])):
            board[i][j] += board[i - 1][j]


def point_score(board, r1, c1, r2, c2, score):
    board[r1][c1] += score
    board[r1][c2 + 1] -= score
    board[r2 + 1][c1] -= score
    board[r2 + 1][c2 + 1] += score


def solution(board: list[list[int]], skill: list[list[int]]):
    answer = 0
    accumulated_board = [[0 for _ in range(1001)] for _ in range(1001)]

    # point score on the accumulate board
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        score = degree
        if t == 1:
            score = -degree
        point_score(accumulated_board, r1, c1, r2, c2, score)

    # accumulate
    accumulate(accumulated_board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += accumulated_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
print(solution(board, skill))
