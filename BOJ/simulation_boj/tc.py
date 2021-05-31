n = 8
y, x = 3, 4

dy = [0, n - 1, n - 1, n - 1, 0, 1, 1, 1]
dx = [n - 1, n - 1, 0, 1, 1, 1, 0, n - 1]
for i in range(8):
    print((y + dy[i] * 4) % n, end=' ')
    print((x + dx[i] * 4) % n)
