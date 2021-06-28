# [카카오] 자물쇠와 열쇠
import copy


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    board = [[0 for _ in range(key_size * 2 + lock_size)] for _ in range(key_size * 2 + lock_size)]

    for y in range(lock_size):
        for x in range(lock_size):
            board[key_size + y][key_size + x] = lock[y][x]

    for _ in range(4):
        for sy in range(key_size + lock_size + 1):
            for sx in range(key_size + lock_size + 1):
                maps = copy.deepcopy(board)
                print_key(sy, sx, key, maps)
                if is_correct_key(len(key), lock_size, maps):
                    return True
        key = rotate(key)
    return False


def print_key(sy, sx, key, board):
    key_size = len(key)
    for y in range(key_size):
        for x in range(key_size):
            board[sy + y][sx + x] += key[y][x]


def is_correct_key(key_size, lock_size, board):
    for y in range(lock_size):
        for x in range(lock_size):
            if board[key_size + y][key_size + x] != 1:
                return False
    return True


def rotate(arr):
    ret = []
    size = len(arr)
    for x in range(size):
        temp = []
        for y in range(size - 1, -1, -1):
            temp.append(arr[y][x])
        ret.append(temp)
    return ret


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(rotate(arr))
    print(solution(key, lock))
