# BOJ 1912번
import sys

# 음수가 껴있어도 최대 연속 합을 만들수 있는것에 주의해야 함
input = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        if seq[i - 1] > 0:
            memo[i] = memo[i - 1] + seq[i]
        else:
            memo[i] = max(memo[i - 1] + seq[i], seq[i])
    # print(memo)
    return max(memo)


"""
n = 10
seq = [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
memo = [0] * n
memo[0] = seq[0]
print(solve(n))
"""

n = int(input())
seq = list(map(int, input().split()))
memo = [0] * n
memo[0] = seq[0]
print(solve(n))