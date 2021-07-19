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
                key = rotate(key)
                maps = copy.deepcopy(board)
                for y in range(key_size):
                    for x in range(key_size):
                        maps[sy + y][sx + x] += key[y][x]
                if check(maps, key_size, lock_size):
                    return True
    return False


def rotate(key):
    ret = []
    for x in range(len(key)):
        temp = []
        for y in range(len(key) - 1, -1, -1):
            temp.append(key[y][x])
        ret.append(temp)
    return ret


def check(maps, key_size, lock_size):
    for y in range(lock_size):
        for x in range(lock_size):
            if maps[key_size + y][key_size + x] != 1:
                return False
    return True


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
