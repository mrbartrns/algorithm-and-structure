# BOJ 1963
import sys
from collections import deque

si = sys.stdin.readline

# n, m = map(int, si().split())


def get_prime_number(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i + i, n, i):
            if sieve[j]:
                sieve[j] = False
    return set([i for i in range(2, n) if sieve[i]])


prime_list = get_prime_number(10000)


def bfs(n, m):
    cnt = 0
    que = deque([n])
    visited.add(n)
    while que:
        size = len(que)
        for _ in range(size):
            v = que.popleft()
            if v == m:
                return cnt
            str_v = str(v)
            for i in range(len(str_v)):
                for j in range(0 if i > 0 else 1, 10):
                    new_ = str_v[:i] + str(j) + str_v[i + 1 :]
                    new_number = int(new_)
                    if new_number in prime_list and new_number not in visited:
                        visited.add(new_number)
                        que.append(new_number)
        cnt += 1
    return -1


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    visited = set()
    res = bfs(n, m)
    print(res if res > -1 else "Impossible")