# BOJ 1256 사전
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, M, K = map(int, si().strip().split(" "))
cache = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

cache[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 and j == 0:
            continue
        cache[i][j] += cache[i - 1][j] if i - 1 >= 0 else 0
        cache[i][j] += cache[i][j - 1] if j - 1 >= 0 else 0
string = ""
n, m, k = N, M, K
if k > cache[n][m]:
    print(-1)
else:
    while n > 0 and m > 0:
        if k <= cache[n - 1][m]:
            string += "a"
            n -= 1
        else:
            k -= cache[n - 1][m]
            string += "z"
            m -= 1
    while n > 0:
        n -= 1
        string += "a"
    while m > 0:
        m -= 1
        string += "z"
    print(string)
