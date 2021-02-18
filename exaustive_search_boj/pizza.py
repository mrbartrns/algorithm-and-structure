# BOJ 2632
import sys

si = sys.stdin.readline

target = int(si())
a, b = map(int, si().split())
left = [int(si()) for _ in range(a)]
right = [int(si()) for _ in range(b)]
lsum, rsum = [0] * 2000001, [0] * 2000001
lsum[0] = rsum[0] = 1

for i in range(a):
    s = 0
    for j in range(a):
        s += left[(i + j) % a]
        if s > target:
            break
        else:
            lsum[s] += 1

for i in range(b):
    s = 0
    for j in range(b):
        s += right[(i + j) % b]
        if s > target:
            break
        else:
            rsum[s] += 1

lsum[sum(left)] = rsum[sum(right)] = 1

ans = 0
for i in range(target + 1):
    ans += lsum[i] * rsum[target - i]

print(ans)
