# 자물쇠와 열쇠
import copy


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    board = [[0 for _ in range(lock_size + 2 * key_size)] for _ in range(lock_size + 2 * key_size)]
    print_lock(lock, key_size, lock_size, board)
    # 4개의 방향을 모두 실행해야함
    for _ in range(4):
        # key의 크기를 고려하여 그 만큼 빼줘야 함
        for sy in range(lock_size + key_size):
            for sx in range(lock_size + key_size):
                board_copy = copy.deepcopy(board)
                print_key(key, board_copy, sy, sx)
                if check(board_copy, key_size, lock_size):
                    return True
        key = rotate(key)
    return False


def print_lock(lock, key_size, lock_size, board):
    """
    자물쇠를 보드 한 가운데에 배치하는 함수
    @param lock: original array of lock
    @param key_size: length of key array
    @param lock_size: length of lock array
    @param board: board array
    @return:
    """
    for y in range(lock_size):
        for x in range(lock_size):
            board[key_size + y][key_size + x] = lock[y][x]


def print_key(key, board, sy, sx):
    """
    키를 보드에 배치하는 함수
    키는 sy, sx에서 시작하여 키의 크기만큼 배열을 순회함
    @param key:
    @param board:
    @param sy:
    @param sx:
    @return:
    """
    for y in range(len(key)):
        for x in range(len(key)):
            board[sy + y][sx + x] += key[y][x]


def check(board, key_size, lock_size):
    for y in range(lock_size):
        for x in range(lock_size):
            if board[key_size + y][key_size + x] == 0 or board[key_size + y][key_size + x] >= 2:
                return False
    return True


def rotate(key):
    """
    시계방향으로 90도 회전하는 함수
    @param key:
    @return:
    """
    new_key = []
    for x in range(len(key)):
        temp = []
        for y in range(len(key) - 1, -1, -1):
            temp.append(key[y][x])
        new_key.append(temp)
    return new_key


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
