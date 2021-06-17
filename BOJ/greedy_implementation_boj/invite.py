# BOJ 9237
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
trees = list(map(int, si().split()))
trees.sort(reverse=True)
ans = 0
for i in range(1, n + 1):
    temp = i
    temp += trees[i - 1]
    ans = max(ans, temp)

ans += 1
print(ans)
