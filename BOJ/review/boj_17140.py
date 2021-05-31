# BOJ 17140 (2차원 배열과 연산)
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def custom_sort(arr):
    counts = [0] * 10000
    numbers = set()
    q = []
    ret = []
    for n in arr:
        if n > 0:
            counts[n] += 1
            numbers.add(n)

    for number in numbers:
        heapq.heappush(q, (counts[number], number))
    while q:
        counts_of_number, number = heapq.heappop(q)
        if len(ret) < 100:
            ret.append(number)
        if len(ret) < 100:
            ret.append(counts_of_number)
    return ret


def operate(matrix, row_size, col_size):
    if row_size >= col_size:
        line = 0
        for i in range(row_size):
            temp = []
            for j in range(col_size):
                temp.append(matrix[i][j])
            new_row = custom_sort(temp)
            line = max(line, len(new_row))
            for j in range(100):
                if j < len(new_row):
                    matrix[i][j] = new_row[j]
                else:
                    matrix[i][j] = 0
        return line

    else:
        line = 0
        for j in range(col_size):
            temp = []
            for i in range(row_size):
                temp.append(matrix[i][j])
            new_col = custom_sort(temp)
            line = max(line, len(new_col))
            for i in range(100):
                if i < len(new_col):
                    matrix[i][j] = new_col[i]
                else:
                    matrix[i][j] = 0
        return line


r, c, k = map(int, si().split())
matrix = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    p, q, r = map(int, si().split())
    matrix[i][0], matrix[i][1], matrix[i][2] = p, q, r

cur_row = 3
cur_col = 3
time = 0
chk = False
while time <= 100:
    if matrix[r - 1][c - 1] == k:
        chk = True
        break

    if cur_row >= cur_col:
        cur_col = operate(matrix, cur_row, cur_col)
    else:
        cur_col = operate(matrix, cur_row, cur_col)
    time += 1

print(time if chk else -1)
