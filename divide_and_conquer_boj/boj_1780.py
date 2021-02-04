# BOJ 1780
n = 9
paper = [
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 1, -1, 0, 1, -1],
    [0, -1, 1, 0, 1, -1, 0, 1, -1],
    [0, 1, -1, 1, 0, -1, 0, 1, -1],
]
ans = [0, 0, 0]


def divide(x, y, n):
    if n == 1:
        ans[paper[x][y] + 1] += 1
        return

    start = paper[x][y]
    same = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != paper[i][j]:
                same = False
                break

    if same:
        ans[start + 1] += 1
        return

    for i in range(3):
        for j in range(3):
            divide(x + i * (n // 3), y + j * (n // 3), n // 3)


divide(0, 0, n)
print("\n".join(list(map(str, ans))))
