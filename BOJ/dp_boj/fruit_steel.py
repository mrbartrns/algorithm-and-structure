# BOJ 17213 과일 서리
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_case(n, m):
    # 1) 과일의 수는 충족되었지만 모든 과일을 가져오지 못한 경우
    if m >= M and n < N:
        return 0
    # 2) 인덱스 범위를 벗어난 경우
    if m > M or n > N:
        return 0
    # 3) 조건을 만족하는 경우
    if m == M and n == N:
        cache[n][m] = 1
        return 1
    if cache[n][m] > -1:
        return cache[n][m]
    cache[n][m] = 0
    for i in range(1, M + 1):
        cache[n][m] += get_case(n + 1, m + i)
    return cache[n][m]


N = int(si().strip())
M = int(si().strip())
cache = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
print(get_case(0, 0))
