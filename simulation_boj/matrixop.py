# BOJ 17140
"""
크기가 3 * 3 인 배열이 있을때, 1초가 지날 때 마다 다음의 연산의 적용
R: 배열 A의 모든 행에 대하여 정렬 수행, 행의갯수 >= 열의 갯수인 경우에 적용
C: 배열 A의 모든 열에 대하여 정렬 수행, 행의갯수 < 열의 갯수인 경우에 적용
한 행 또는 열에있는 수를 정렬하려면, 각 수가 몇번 나왔는지 알아야함
"""
import heapq
import sys

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
            ret.append(counts_of_number)
    return ret


def operate(matrix, row_size, col_size):
    row = row_size
    col = col_size
    if row >= col:
        line = 0
        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(matrix[i][j])
            new_row = custom_sort(temp)
            line = max(line, len(new_row))  # new_row는 열의 크기가 바뀜
            for j in range(100):
                if j < len(new_row):
                    matrix[i][j] = new_row[j]
                else:
                    matrix[i][j] = 0
        return line
    else:
        line = 0
        for j in range(col):
            temp = []
            for i in range(row):
                temp.append(matrix[i][j])
            new_col = custom_sort(temp)
            line = max(line, len(new_col))  # nz은 행의 크기가 바뀜
            for i in range(100):
                if i < len(new_col):
                    matrix[i][j] = new_col[i]
                else:
                    matrix[i][j] = 0
        return line


r, c, k = map(int, si().split())
mat = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    x, y, z = map(int, si().split())
    mat[i][0], mat[i][1], mat[i][2] = x, y, z
cur_row = 3
cur_col = 3
time = 0
check = False
while time <= 100:
    if mat[r - 1][c - 1] == k:
        check = True
        break
    if cur_row >= cur_col:
        new_col_size = operate(mat, cur_row, cur_col)
        cur_col = new_col_size
    else:
        new_row_size = operate(mat, cur_row, cur_col)
        cur_row = new_row_size
    time += 1

print(time if check else -1)

