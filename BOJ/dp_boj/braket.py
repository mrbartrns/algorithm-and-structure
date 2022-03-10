import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000007

cache = [0] * 10010
cache[0] = 1
cache[2] = 1
for i in range(4, 10010, 2):
    for j in range(0, i, 2):
        cache[i] += cache[j] * cache[i - j - 2]
        cache[i] %= MOD
T = int(si().strip())
for _ in range(T):
    a = int(si().strip())
    print(cache[a])
