# BOJ 17140
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def get_new_arr(arr):
    numbers = set()
    values = [0] * 101
    q = []
    ret = []
    for i in range(len(arr)):
        num = arr[i]
        if num > 0:
            numbers.add(num)
            values[num] += 1

    for number in numbers:
        heapq.heappush(q, (values[number], number))

    while q:
        cnt, number = heapq.heappop(q)
        if len(ret) < 100:
            ret.append(number)
        if len(ret) < 100:
            ret.append(cnt)
    return ret


def custom_sort(row_size, col_size):
    new_row_cnt = row_size
    new_col_cnt = col_size
    line = 0

    if row_size >= col_size:  # 행의 수가 열의 수보다 많다면, 행에 대하여 연산 수행 -> 열의 길이가 바뀜
        for i in range(row_size):
            temp = []
            for j in range(col_size):
                temp.append(matrix[i][j])
            new_row = get_new_arr(temp)
            line = max(line, len(new_row))
            for j in range(100):
                if j < len(new_row):
                    matrix[i][j] = new_row[j]
                else:
                    matrix[i][j] = 0
        new_col_cnt = line
    else:
        for j in range(col_size):
            temp = []
            for i in range(row_size):
                temp.append(matrix[i][j])
            new_col = get_new_arr(temp)
            line = max(line, len(new_col))
            for i in range(100):
                if i < len(new_col):
                    matrix[i][j] = new_col[i]
                else:
                    matrix[i][j] = 0
        new_row_cnt = line
    return new_row_cnt, new_col_cnt


r, c, k = map(int, si().split())
matrix = [[0 for _ in range(100)] for _ in range(100)]
time = 0

for i in range(3):
    e1, e2, e3 = map(int, si().split())
    matrix[i][0], matrix[i][1], matrix[i][2] = e1, e2, e3

chk = False
row_cnt = 3
col_cnt = 3
while time <= 100:
    if matrix[r - 1][c - 1] == k:
        chk = True
        break
    row_cnt, col_cnt = custom_sort(row_cnt, col_cnt)
    time += 1

print(time if chk else -1)
