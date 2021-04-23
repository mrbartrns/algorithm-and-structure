# BOJ 16917
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

a, b, c, x, y = map(int, si().split())

first = min(x, y)
ans = min(a * (x - first) + b * (y - first), c * 2 * max(x - first, y - first))
if a + b > c * 2:
    ans += first * c * 2
else:
    ans += a * first + b * first
print(ans)
