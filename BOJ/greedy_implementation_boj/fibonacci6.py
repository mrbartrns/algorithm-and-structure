# BOJ 11444
import sys

si = sys.stdin.readline
MOD = 1000000007


def solve(n):
    if n == 1:
        matrix = [[1, 1], [1, 0]]
        return matrix
    mat = [[0, 0], [0, 0]]
    matrix = solve(n // 2)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat[i][j] += (matrix[i][k] * matrix[k][j]) % MOD
            mat[i][j] %= MOD
    if n % 2 == 1:
        mat_odd = [[0, 0], [0, 0]]
        unit = [[1, 1], [1, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    mat_odd[i][j] += (mat[i][k] * unit[k][j]) % MOD
                mat_odd[i][j] %= MOD
        return mat_odd
    return mat


n = int(si())
print(solve(n)[0][1])
