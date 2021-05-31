
def get_color_count(matrix):
    different_color_count = 0
    for i in range(len(matrix)):
        for j in range(len((matrix[0]))):
            if matrix[i][j] == 3:
                different_color_count += 1
    return different_color_count

def get_new_matrix(matrix, x1, y1, x2, y2, color):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if matrix[i][j] != 0 and matrix[i][j] != color:
                matrix[i][j] = 3
            else:
                matrix[i][j] = color
    return matrix



t = int(input())
for i in range(t):
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    counts = 0
    # 색칠 횟수
    n = int(input())
    for j in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        matrix = get_new_matrix(matrix, x1, y1, x2, y2, color)
    counts = get_color_count(matrix)
    print(f'#{i + 1} {counts}')

