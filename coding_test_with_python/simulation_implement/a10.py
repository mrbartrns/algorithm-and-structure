# [카카오] 자물쇠와 열쇠
import copy


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    board = [[0 for _ in range(2 * key_size + lock_size)] for _ in range(2 * key_size + lock_size)]
    for i in range(lock_size):
        for j in range(lock_size):
            board[key_size + i][key_size + j] = lock[i][j]
    for sy in range(key_size + lock_size):
        for sx in range(key_size + lock_size):
            for _ in range(4):
                maps = copy.deepcopy(board)
                key = rotate(key)
                for y in range(key_size):
                    for x in range(key_size):
                        maps[sy + y][sx + x] += key[y][x]

                if check(maps, key_size, lock_size):
                    return True
    return False


def check(board, key_size, lock_size):
    for y in range(lock_size):
        for x in range(lock_size):
            if board[key_size + y][key_size + x] != 1:
                return False
    return True


def rotate(key):
    ret = []
    for j in range(len(key)):
        temp = []
        for i in range(len(key) - 1, -1, -1):
            temp.append(key[i][j])
        ret.append(temp)
    return ret


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
