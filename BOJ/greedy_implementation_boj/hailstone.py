# BOJ 3943
import sys

si = sys.stdin.readline
t = int(si())
for _ in range(t):
    n = int(si())
    max_value = n
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            new_ = n * 3 + 1
            n = new_
            max_value = max(n, max_value)
    print(max_value)
