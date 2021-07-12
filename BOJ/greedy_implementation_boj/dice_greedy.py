# BOJ 1041
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321


def solve(n, arr):
    if n > 1:
        s1 = 5 * (n - 2) ** 2 + 4 * (n - 2)
        s2 = 8 * (n - 2) + 4
        s3 = 4

        ans = 0
        ans += min(arr) * s1
        s = INF
        for a, b in t2:
            s = min(s, arr[a] + arr[b])
        ans += s2 * s

        s = INF
        for a, b, c in t3:
            s = min(s, arr[a] + arr[b] + arr[c])
        ans += s3 * s
        return ans
    else:
        return sum(arr) - max(arr)


t2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
t3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]

n = int(si())
arr = list(map(int, si().split()))
print(solve(n, arr))
