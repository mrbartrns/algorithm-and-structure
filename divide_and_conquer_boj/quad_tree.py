# BOJ 1992
import sys

si = sys.stdin.readline
"""
n = 8
arr = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1],
]
"""
n = int(si())
arr = []
for _ in range(n):
    arr.append(list(map(int, si().strip())))

# 이 표현 완벽하게 익혀두기
def solve(x, y, n):
    if n == 1:
        return str(arr[x][y])

    temp = arr[x][y]
    string = ""
    flag = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != temp:
                flag = False
                break

    if flag:
        return str(temp)

    string += "("
    for i in range(2):
        for j in range(2):
            string += solve(x + i * (n // 2), y + j * (n // 2), n // 2)
    string += ")"
    return string


string = solve(0, 0, n)
print(string)
