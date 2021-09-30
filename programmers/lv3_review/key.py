# [카카오] 자물쇠와 걸쇠
import copy


def check(board, key_size, lock_size):
    for y in range(lock_size):
        for x in range(lock_size):
            if board[key_size + y][key_size + x] != 1:
                return False
    return True


def display_on_board(board, key, sy, sx):
    for y in range(len(key)):
        for x in range(len(key)):
            board[sy + y][sx + x] += key[y][x]


def setting_on_board(board, lock, key_size):
    for i in range(len(lock)):
        for j in range(len(lock)):
            board[key_size + i][key_size + j] = lock[i][j]


def rotate(key):
    ret = []
    for j in range(len(key)):
        temp = []
        for i in range(len(key) - 1, -1, -1):
            temp.append(key[i][j])
        ret.append(temp)
    return ret


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    board = [
        [0 for _ in range(2 * key_size + lock_size)]
        for _ in range(2 * key_size + lock_size)
    ]
    setting_on_board(board, lock, key_size)
    for sy in range(key_size + lock_size):
        for sx in range(key_size + lock_size):
            for _ in range(4):
                key = rotate(key)
                board_copy = copy.deepcopy(board)
                display_on_board(board_copy, key, sy, sx)
                if check(board_copy, key_size, lock_size):
                    return True
    return False


if __name__ == "__main__":
    key = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 1],
    ]
    lock = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    print(solution(key, lock))
