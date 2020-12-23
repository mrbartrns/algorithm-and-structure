room = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0],
]


def gravity(room: list) -> int:
    max_value = 0
    pre = -1
    for i in range(len(room)):
        zero_counter = 0
        for j in range(len(room[0]) - 1, -1, -1):
            if room[i][j] == 0:
                zero_counter += 1
            else:
                room[i][j], room[i][j + zero_counter] = (
                    room[i][j + zero_counter],
                    room[i][j],
                )
                if max_value < zero_counter:
                    max_value = zero_counter
                pre = i
        if pre != -1:
            break
    return max_value


print(gravity(room))