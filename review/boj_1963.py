# BOJ 1963
import sys
from collections import deque

si = sys.stdin.readline


def get_prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return set([i for i in range(1000, n) if sieve[i]])


def bfs(start, end):
    que = deque([(start, 0)])
    visited.add(start)
    while que:
        v, cnt = que.popleft()
        if v == end:
            return cnt
        for i in range(4):
            str_v = str(v)
            for j in range(0 if i > 0 else 1, 10):
                new_ = str_v[:i] + str(j) + str_v[i + 1 :]
                new_number = int(new_)
                if new_number in primes and new_number not in visited:
                    que.append((new_number, cnt + 1))
                    visited.add(new_number)
                    # break를 할 필요가 없다. 너비 우선탐색이란, 우선 조건에 맞는 모든것들을 큐에 집어넣어서 확인하는것이다.


t = int(si())
primes = get_prime_list(10000)
for _ in range(t):
    n, m = map(int, si().split())
    visited = set()
    print(bfs(n, m))