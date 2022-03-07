# BOJ 5721 사탕 줍기 대회
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

while True:
    ROW, COL = map(int, si().strip().split(" "))
    if (ROW, COL) == (0, 0):
        break
    arr = []
    for _ in range(ROW):
        arr.append(list(map(int, si().strip().split(" "))))
    cache = [[0 for _ in range(COL)] for _ in range(ROW)]
    for i in range(ROW):
        for j in range(COL):
            cache[i][j] = arr[i][j]
            if j - 2 >= 0:
                cache[i][j] = max(cache[i][j - 1], cache[i][j - 2] + arr[i][j])
            elif j - 1 >= 0:
                cache[i][j] = max(cache[i][j - 1], cache[i][j])
    for i in range(1, ROW):
        cache[i][j] = max(
            cache[i - 1][COL - 1],
            cache[i][COL - 1] + cache[i - 2][COL - 1]
            if i - 2 >= 0
            else cache[i][COL - 1],
        )
    print(cache[ROW - 1][COL - 1])
