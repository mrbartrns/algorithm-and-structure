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


# tc
sudoku = [
    [1, 0, 3, 0, 0, 0, 5, 0, 9],  # 5
    [0, 0, 2, 1, 0, 9, 4, 0, 0],  # 5
    [0, 0, 0, 7, 0, 4, 0, 0, 0],  # 7
    [3, 0, 0, 5, 0, 2, 0, 0, 6],  # 5
    [0, 6, 0, 0, 0, 0, 0, 5, 0],  # 7
    [7, 0, 0, 8, 0, 3, 0, 0, 4],  # 5
    [0, 0, 0, 4, 0, 1, 0, 0, 0],  # 7
    [0, 0, 9, 2, 0, 5, 8, 0, 0],  # 5
    [8, 0, 4, 0, 0, 0, 1, 0, 7],  # 5
]
rows = [
    [1, 3, 5, 9],
    [2, 1, 9, 4],
    [7, 4],
    [3, 5, 2, 6],
    [6, 5],
    [7, 8, 3, 4],
    [4, 1],
    [9, 2, 5, 8],
    [8, 4, 1, 7],
]
cols = [
    [1, 3, 7, 8],
    [6],
    [3, 2, 9, 4],
    [1, 7, 5, 8, 4, 2],
    [],
    [9, 4, 2, 3, 1, 5],
    [5, 4, 8, 1],
    [5],
    [9, 6, 4, 7],
]
squares = [
    [[1, 3, 2], [1, 9, 7, 4], [5, 4, 9]],
    [[3, 6, 7], [5, 2, 8, 3], [6, 5, 4]],
    [[9, 8, 4], [4, 1, 2, 5], [8, 1, 7]],
]

zero_locations = [
    [0, 1],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 7],
    [1, 0],
    [1, 1],
    [1, 4],
    [1, 7],
    [1, 8],
    [2, 0],
    [2, 1],
    [2, 2],
    [2, 4],
    [2, 6],
    [2, 7],
    [2, 8],
    [3, 1],
    [3, 2],
    [3, 4],
    [3, 6],
    [3, 7],
    [4, 0],
    [4, 2],
    [4, 3],
    [4, 4],
    [4, 5],
    [4, 6],
    [4, 8],
    [5, 1],
    [5, 2],
    [5, 4],
    [5, 6],
    [5, 7],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 4],
    [6, 6],
    [6, 7],
    [6, 8],
    [7, 0],
    [7, 1],
    [7, 4],
    [7, 7],
    [7, 8],
    [8, 1],
    [8, 3],
    [8, 4],
    [8, 5],
    [8, 7],
]
has_passed = [
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
]
zero_count = 51
print(solve(zero_count))