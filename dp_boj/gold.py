import sys


def solve(n):  # n은 열의 크기 -1
    for j in range(1, len(memo[0])):
        for i in range(len(memo)):
            val1 = memo[i - 1][j - 1] if i - 1 >= 0 else -1
            val2 = memo[i][j - 1]
            val3 = memo[i + 1][j - 1] if i + 1 < len(memo) else -1
            memo[i][j] = max(val1, val2, val3) + golds[i][j]

    biggest = -1
    for i in range(len(memo)):
        if memo[i][n] > biggest:
            biggest = memo[i][n]
    return biggest


# golds = [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]
# memo = [[0 for _ in range(len(golds[0]))] for _ in range(len(golds))]
# # memo 초기화
# for y in range(len(golds)):
#     memo[y][0] = golds[y][0]
# print(solve(3))
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    golds = [[0 for _ in range(m)] for _ in range(n)]
    memo = golds[:]

    numbers = list(map(int, sys.stdin.readline().split()))
    for i in range(len(numbers)):
        golds[i // m][i % m] = numbers[i]
    for i in range(len(golds)):
        memo[i][0] = golds[i][0]
    print(solve(m - 1))