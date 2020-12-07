maze = [
    [1, 3, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 2, 1],
]

zeros = []

issued = [
    [True, False, True, False, True],
    [True, False, True, False, True],
    [True, False, True, False, True],
    [True, False, True, False, True],
    [True, False, False, False, True],
]

counts = 0


def get_route(arr, x, y):
    global zeros, issued, counts
    if arr[x][y] == 3:
        if counts != 0 or counts > len(zeros):
            counts = len(zeros)
        return
    elif x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0]):
        return
    else:
        if not issued[x][y]:
            issued[x][y] = True
            if arr[x][y] == 0:
                zeros.append(0)

            if arr[x][y - 1] != 1:
                get_route(arr, x, y - 1)
            if arr[x - 1][y] != 1:
                get_route(arr, x - 1, y)
            if arr[x][y + 1] != 1:
                get_route(arr, x, y + 1)
            if arr[x + 1][y] != 1:
                get_route(arr, x + 1, y)

            if arr[x][y] == 0:
                zeros.pop()
            issued[x][y] = False


get_route(maze, 4, 3)
print(counts)