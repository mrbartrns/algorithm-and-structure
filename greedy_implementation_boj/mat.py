# BOJ 10830
import sys

si = sys.stdin.readline
mod = 1000


def solve(matrix: list, b: int) -> list:
    if b == 1:
        ret = []
        for i in range(n):
            ret.append(list(map(lambda x: x % 1000, matrix[i])))
        return ret
    mat = [[0 for _ in range(n)] for _ in range(n)]
    ret = solve(matrix, b // 2)
    for r in range(n):
        for c in range(n):
            for k in range(n):
                mat[r][c] += (ret[r][k] * ret[k][c]) % mod
            mat[r][c] = mat[r][c] % mod
    if b % 2 == 1:
        odd = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                for k in range(n):
                    odd[r][c] += (mat[r][k] * matrix[k][c]) % mod
                odd[r][c] = odd[r][c] % mod
        return odd
    return mat


n, b = map(int, si().split())
arr = [list(map(int, si().split())) for _ in range(n)]
calculated = solve(arr, b)
for i in range(n):
    print(" ".join(list(map(str, calculated[i]))))
