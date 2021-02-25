# BOJ 1963
import sys
from collections import deque

si = sys.stdin.readline


def get_primes(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return set([i for i in range(1000, n) if sieve[i]])


def bfs(s, t):
    que = deque([(s, 0)])
    visited.add(s)
    while que:
        v, cnt = que.popleft()
        if v == t:
            return cnt

        str_v = str(v)
        for i in range(len(str_v)):
            for j in range(0 if i > 0 else 1, 10):
                new_ = str_v[:i] + str(j) + str_v[i + 1 :]
                new_number = int(new_)
                if new_number in primes and new_number not in visited:
                    visited.add(new_number)
                    que.append((new_number, cnt + 1))

    return -1


primes = get_primes(10000)
tc = int(si())

for _ in range(tc):
    s, t = map(int, si().split())
    visited = set()
    val = bfs(s, t)
    print(val if val > -1 else "Impossibe")
