# BOJ 2810
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
string = si().strip()
cnt = 0
for c in string:
    if c == "L":
        cnt += 1

ans = cnt // 2 - 1 if cnt > 0 else 0
print(n - ans)
