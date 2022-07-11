INF = 987654321


def solution(n, info):
    max_score = 0
    case = INF
    score_board = [0] * 11
    for i in range(1 << 11):
        count = 0
        for j in range(11):
            if (1 << j) & i:
                count += info[10 - j] + 1
        if count > n:
            continue
        next_score = calculate(info, i)
        next_score_board = transform(info, i)
        s = sum(next_score_board)
        if s < n:
            for i in range(10, -1, -1):
                if next_score_board[i] == 0:
                    next_score_board[i] += n - s
                    break
        if next_score > max_score:
            max_score = next_score
            case = i
            score_board = next_score_board[:]
        elif next_score == max_score:
            score_board = compare(score_board, next_score_board)
    if case == INF:
        return [-1]
    return score_board


def calculate(info, score_board):
    a, b = 0, 0
    for i in range(11):
        if (1 << i) & score_board:
            a += i
        elif info[10 - i] > 0:
            b += i
    return a - b


def transform(info, score_board):
    ret = [0] * 11
    for i in range(11):
        if (1 << i) & score_board:
            ret[10 - i] = info[10 - i] + 1
    return ret


def compare(prev, next):
    for i in range(10, -1, -1):
        if prev[i] > next[i]:
            return prev
        if prev[i] < next[i]:
            return next
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


n = 10
info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
print(solution(n, info))
