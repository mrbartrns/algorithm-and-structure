# BOJ 2705 팰린드롬 파티션
import sys

# sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def palindrome(n):
    if n <= 1:
        return 1
    if cache[n] > -1:
        return cache[n]
    cache[n] = 1
    for i in range(n):
        if (n - i) % 2 == 1:
            continue
        cache[n] += palindrome((n - i) // 2)
    return cache[n]


cache = [-1 for _ in range(1001)]
T = int(si().strip())
for _ in range(T):
    N = int(si().strip())
    print(palindrome(N))
