# BOJ 13302 리조트
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(100000)
INF = 987654321


def solve(n: int, coupon: int) -> int:
    if coupon < 0:
        return INF
    if n > N:
        return 0
    if cache[n][coupon] < INF:
        return cache[n][coupon]
    if busy[n]:
        cache[n][coupon] = solve(n + 1, coupon)
        return cache[n][coupon]
    cache[n][coupon] = min(
        cache[n][coupon],
        10000 + solve(n + 1, coupon),
        25000 + solve(n + 3, coupon + 1),
        37000 + solve(n + 5, coupon + 2),
        solve(n + 1, coupon - 3),
    )
    return cache[n][coupon]


N, M = map(int, input().split(" "))
busy = [False] * 101
arr = []
if M > 0:
    arr = list(map(int, input().split(" ")))
cache = [[INF for _ in range(101)] for _ in range(101)]
for i in range(M):
    busy[arr[i]] = True
solve(1, 0)
print(cache[1][0])
