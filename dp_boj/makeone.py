# 재귀로 풀고 그다음 dp로


# sys.setrecursionlimit(10000)

# 탑다운 방식은 리미트가 있음
"""
def solve(n):
    # print("stack:", n)
    if n == 1:
        return memo[n]

    if memo[n] > 0:
        return memo[n]

    memo[n] = solve(n - 1) + 1
    if n % 5 == 0:
        memo[n] = min(memo[n], solve(n // 5) + 1)
    if n % 3 == 0:
        memo[n] = min(memo[n], solve(n // 3) + 1)
    if n % 2 == 0:
        memo[n] = min(memo[n], solve(n // 2) + 1)

    return memo[n]
"""

import sys


def dp(n):
    # 탑다운은 재귀함수에서 사용이 가능한 것과 달리 바텀업은 재귀에서 사용 불가
    # 바텀업 방식은 작은 문제를 먼저 해결후 그 답을 큰 문제에 해결하는데 사용하는 방식
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + 1
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)
        # if y % 5 == 0:
        #     memo[y] = min(memo[y], memo[y // 5] + 1)
    return memo[n]


n = int(sys.stdin.readline())

memo = [0] * (n + 1)

sys.stdout.write(str(dp(n)))
