# BOJ 1695 팰린드롬 만들기
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(10000000)
si = sys.stdin.readline
INF = 987654321

N = int(si().strip())
arr: list[int] = list(map(int, si().strip().split(" ")))
cache = [[INF for _ in range(N)] for _ in range(N)]


def palindrome(y, x):
    if y >= x:
        return 0
    if cache[y][x] < INF:
        return cache[y][x]
    if arr[y] == arr[x]:
        cache[y][x] = min(cache[y][x], palindrome(y + 1, x - 1))
    else:
        cache[y][x] = min(cache[y][x], 1 + palindrome(y + 1, x))
        cache[y][x] = min(cache[y][x], 1 + palindrome(y, x - 1))
    return cache[y][x]


palindrome(0, N - 1)
print(cache[0][N - 1])
