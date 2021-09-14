# [카카오] 자물쇠와 열쇠
import copy


def check_key(board, key_size, lock_size):
    for i in range(lock_size):
        for j in range(lock_size):
            if board[key_size + i][key_size + j] != 1:
                return False
    return True


def rotate(key):
    ret = []
    for x in range(len(key)):
        temp = []
        for y in range(len(key) - 1, -1, -1):
            temp.append(key[y][x])
        ret.append(temp)
    return ret


def solution(key, lock):
    # make board set lock in center of the board
    key_size = len(key)
    lock_size = len(lock)
    board = [
        [0 for _ in range(key_size * 2 + lock_size)]
        for _ in range(key_size * 2 + lock_size)
    ]

    # draw lock on the board
    for i in range(lock_size):
        for j in range(lock_size):
            board[key_size + i][key_size + j] = lock[i][j]

    # check the key is fit with the board (rotate and start from 0, 0 to key_size + lock_size)
    for sy in range(key_size + lock_size):
        for sx in range(key_size + lock_size):
            for _ in range(4):
                key = rotate(key)
                cp = copy.deepcopy(board)
                for y in range(key_size):
                    for x in range(key_size):
                        cp[sy + y][sx + x] += key[y][x]
                if check_key(cp, key_size, lock_size):
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