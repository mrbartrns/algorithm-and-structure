"""
부분합 계산하기
"""


def partial_sum(arr):
    ret = [0] * len(arr)
    ret[0] = arr[0]
    for i in range(1, len(arr)):
        ret[i] = ret[i - 1] + arr[i]
    return ret


def range_sum(psum, a, b):
    if a == 0:
        return psum[b]
    return psum[b] - psum[a - 1]


def matrix_psum(matrix):
    ret = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i - 1 >= 0:
                ret[i][j] += ret[i - 1][j]
            if j - 1 >= 0:
                ret[i][j] += ret[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                ret[i][j] -= ret[i - 1][j - 1]
            ret[i][j] += matrix[i][j]
    return ret


def grid_sum(psum, y1, x1, y2, x2):
    ret = psum[y2][x2]
    if y1 > 0:
        ret -= psum[y1 - 1][x2]
    if x1 > 0:
        ret -= psum[y2][x1 - 1]
    if y1 > 0 and x1 > 0:
        ret += psum[y1 - 1][x1 - 1]


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    print(matrix_psum(matrix))
