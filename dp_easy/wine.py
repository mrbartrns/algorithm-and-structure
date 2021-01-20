import sys

input = sys.stdin.readline


def solve(n):
    memo[2] = max(memo[1], memo[0] + wines[2], wines[1] + wines[2])
    for i in range(3, n):
        memo[i] = max(
            memo[i - 1], memo[i - 2] + wines[i], memo[i - 3] + wines[i - 1] + wines[i]
        )

    print(memo)
    return memo[n - 1]


# tc
"""
wines = [6, 10, 13, 9, 8, 1]
memo = [0] * len(wines)
memo[0] = wines[0]
n = len(wines)
print(solve(n))

"""
n = int(input())
wines = []
for _ in range(n):
    wine = int(input())
    wines.append(wine)
memo = [0] * n
memo[0] = wines[0]
if n > 1:
    memo[1] = wines[1] + wines[0]
print(solve(n) if n > 2 else memo[n - 1])