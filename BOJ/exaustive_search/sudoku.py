import sys


def solve(zero_count):
    string = ""

    if zero_count == 0:
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                string += str(sudoku[i][j])
            if i < len(sudoku) - 1:
                string += "\n"
        return string

    x = y = 0
    idx = -1
    for i in range(len(zero_locations)):
        if not has_passed[i]:
            x = zero_locations[i][0]
            y = zero_locations[i][1]
            idx = i
            break

    if not has_passed[idx]:
        has_passed[idx] = True
        for j in range(1, 10):
            if (
                j not in rows[x]
                and j not in cols[y]
                and j not in squares[x // 3][y // 3]
            ):
                sudoku[x][y] = j
                rows[x].append(j)
                cols[y].append(j)
                squares[x // 3][y // 3].append(j)
                val = solve(zero_count - 1)
                if val:
                    string += val
                    return string
                sudoku[x][y] = 0
                rows[x].pop()
                cols[y].pop()
                squares[x // 3][y // 3].pop()
        has_passed[idx] = False

    return string


"""
def solve(zero_count):
    string = ""
    zero_found = False
    zero_i = 0
    zero_j = 0

    if zero_count == 0:
        for y in range(len(sudoku)):
            for x in range(len(sudoku[0])):
                string += str(sudoku[y][x])
            if y < len(sudoku) - 1:
                string += "\n"
        return string

    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):
            if sudoku[y][x] == 0:
                zero_i = y
                zero_j = x
                zero_found = True
                break
        if zero_found:
            break

    # 0을 찾은 후 분리하는것이 키 포인트였다!
    if zero_found:
        for k in range(1, 10):
            if (
                k not in rows[zero_i]
                and k not in cols[zero_j]
                and k not in squares[zero_i // 3][zero_j // 3]
            ):
                sudoku[zero_i][zero_j] = k
                rows[zero_i].append(k)
                cols[zero_j].append(k)
                squares[zero_i // 3][zero_j // 3].append(k)
                val = solve(zero_count - 1)
                if val:
                    string += val
                    return string
                sudoku[zero_i][zero_j] = 0
                rows[zero_i].pop()
                cols[zero_j].pop()
                squares[zero_i // 3][zero_j // 3].pop()
    return string
"""


sudoku = []
rows = [[], [], [], [], [], [], [], [], []]
cols = [[], [], [], [], [], [], [], [], []]
squares = [[[], [], []], [[], [], []], [[], [], []]]
zero_locations = []
zero_count = 0
SUDOKU_SIZE = 9

# make sudoku board and zero_count
for i in range(SUDOKU_SIZE):
    row = sys.stdin.readline()
    temp = []
    for c in row:
        if c != "\n":
            temp.append(c)
    raw_row = list(map(int, temp))
    sudoku.append(raw_row)
    for i in raw_row:
        if i == 0:
            zero_count += 1


# make rows, make squares, zero_locations
for i in range(len(sudoku)):
    for j in range(len(sudoku[0])):
        if sudoku[i][j] != 0:
            rows[i].append(sudoku[i][j])
            squares[i // 3][j // 3].append(sudoku[i][j])
        else:
            zero_locations.append([i, j])

# make cols
for j in range(len(sudoku[0])):
    for i in range(len(sudoku)):
        if sudoku[i][j] != 0:
            cols[j].append(sudoku[i][j])

has_passed = [False for _ in range(len(zero_locations))]

# print(solve(zero_count))
sys.stdout.write(solve(zero_count))
# print(zero_locations, has_passed)
