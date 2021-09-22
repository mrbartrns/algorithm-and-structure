# [카카오] 크레인 인형뽑기 게임


def pick(board, idx):
    ret = 0
    for y in range(len(board)):
        if board[y][idx] > 0:
            ret = board[y][idx]
            board[y][idx] = 0
            break
    return ret


def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        idx = move - 1
        picked = pick(board, idx)
        if picked == 0:
            continue
        stack.append(picked)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            for _ in range(2):
                stack.pop()
            answer += 2
    return answer


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
