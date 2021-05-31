# BOJ 13458
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

N = int(si())
test = list(map(int, si().split()))
B, C = map(int, si().split())
ans = N

test = list(map(lambda x: x - B, test))
for i in range(N):
    if test[i] <= 0:
        continue
    ans += test[i] // C
    if test[i] % C > 0:
        ans += 1

print(ans)
