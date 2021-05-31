# BOJ 17140 (2차원 배열과 연산)
# 주의: 0일때 break 하면 안됨
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

matrix = [[0 for _ in range(100)] for _ in range(100)]


def custom_sort(arr: list) -> list:
    """
    sort array by customised rule.
    rule: sort counts of numbers first, value of numbers second
    Args:
        arr(list): row or column of matrix

    Returns(list): sorted array
    """
    ret = []

    q = []
    counts = [0] * 101
    numbers = set()

    for number in arr:
        numbers.add(number)
        counts[number] += 1

    for number in numbers:
        heapq.heappush(q, (counts[number], number))

    while q:
        cnt, num = heapq.heappop(q)
        if len(ret) < 100:
            ret.append(num)
        if len(ret) < 100:
            ret.append(cnt)
    return ret


def operate(row: int, col: int) -> tuple:
    """
    operate matrix.
    Args:
        row: maximum length of matrix's row (except 0)
        col: maximum length of matrix's column (except 0)

    Returns(tuple<int, int>): new row, new column maximum length

    """
    if row >= col:
        new_row, new_col = row, 0
        for y in range(row):
            temp = []
            # 배열을 돌면서 0이 아닌 숫자들을 넣고 반환받기
            for x in range(col):
                if matrix[y][x] == 0:
                    continue
                temp.append(matrix[y][x])
            ret = custom_sort(temp)
            new_col = max(new_col, len(ret))
            # 반환받은 숫자를 현재 배열로 갱신한다.
            for x in range(100):
                if x >= len(ret):
                    matrix[y][x] = 0
                else:
                    matrix[y][x] = ret[x]
        return new_row, new_col
    else:
        new_row, new_col = 0, col
        for x in range(col):
            temp = []
            for y in range(row):
                if matrix[y][x] == 0:
                    continue
                temp.append(matrix[y][x])
            ret = custom_sort(temp)
            new_row = max(new_row, len(ret))

            for y in range(100):
                if y >= len(ret):
                    matrix[y][x] = 0
                else:
                    matrix[y][x] = ret[y]
        return new_row, new_col


r, c, k = map(int, si().split())
for i in range(3):
    a1, a2, a3 = map(int, si().split())
    matrix[i][0], matrix[i][1], matrix[i][2] = a1, a2, a3

time = 0
chk = False
cur_row, cur_col = 3, 3
while time <= 100:
    if matrix[r - 1][c - 1] == k:
        chk = True
        break
    cur_row, cur_col = operate(cur_row, cur_col)
    time += 1

print(time if chk else -1)
