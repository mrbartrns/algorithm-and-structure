# BOJ 14501
import sys

si = sys.stdin.readline


def solve(n):
    ans = 0

    for i in range(n, 0, -1):
        if i + t[i] > n + 1:
            arr[i] = arr[i + 1]
        else:
            arr[i] = max(arr[i + 1], arr[i] + arr[i + t[i]])
            ans = max(ans, arr[i])
    return ans


n = int(si())
t = [0] * 17
arr = [0] * 17

for i in range(1, n + 1):
    u, v = map(int, si().split())
    t[i] = u
    arr[i] = v

print(solve(n))
"""

n = 7
t = [0, 3, 5, 1, 1, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr = [0, 10, 20, 10, 20, 15, 40, 200, 0, 0, 0, 0, 0, 0, 0, 0]
ans = 0
for y in range(n, 0, -1):
    if y + t[y] > n + 1:
        arr[y] = arr[y + 1]
    else:
        arr[y] = max(arr[y + 1], arr[y] + arr[y + t[y]])
        ans = max(ans, arr[y])
print(ans)
# print(solve(n))
"""