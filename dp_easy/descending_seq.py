import sys

input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        for j in range(i):
            if sequence[i] < sequence[j]:
                memo[i] = max(memo[i], memo[j] + 1)
    print(memo)
    return max(memo)


"""
n = int(input())
sequence = list(map(int, input().split()))
memo = [1] * n

"""
n = 10
sequence = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
memo = [1] * n
print(solve(n))
