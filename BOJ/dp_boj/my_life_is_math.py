# BOJ 17265 나의 인생에는 수학과 함께
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def operate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    if operator == "-":
        return operand1 - operand2
    return operand1 * operand2


N = int(si().strip())

arr = [list(si().strip().split(" ")) for _ in range(N)]
cache_max = [[-INF for _ in range(N + 1)] for _ in range(N)]
cache_min = [[INF for _ in range(N + 1)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            cache_max[i][j] = int(arr[i][j])
            cache_min[i][j] = int(arr[i][j])
            continue
        if arr[i][j].isdigit():
            if i - 1 >= 0:
                cache_max[i][j] = max(
                    cache_max[i][j],
                    operate(cache_max[i - 1][j], int(arr[i][j]), arr[i - 1][j]),
                )
                cache_min[i][j] = min(
                    cache_min[i][j],
                    operate(cache_min[i - 1][j], int(arr[i][j]), arr[i - 1][j]),
                )
            if j - 1 >= 0:
                cache_max[i][j] = max(
                    cache_max[i][j],
                    operate(cache_max[i][j - 1], int(arr[i][j]), arr[i][j - 1]),
                )
                cache_min[i][j] = min(
                    cache_min[i][j],
                    operate(cache_min[i][j - 1], int(arr[i][j]), arr[i][j - 1]),
                )
        else:
            if i - 1 >= 0:
                cache_max[i][j] = cache_max[i - 1][j]
                cache_min[i][j] = cache_min[i - 1][j]
            if j - 1 >= 0:
                cache_max[i][j] = max(cache_max[i][j], cache_max[i][j - 1])
                cache_min[i][j] = min(cache_min[i][j], cache_min[i][j - 1])

print(cache_max[N - 1][N - 1], cache_min[N - 1][N - 1])
