# BOJ 1644
import sys

si = sys.stdin.readline


def get_prime_set_to(n):
    sieve = [True] * (n + 1)
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


n = int(si())
prime_set = get_prime_set_to(n)


def solve(arr, num):
    cnt = start = end = s = 0
    n = len(arr)
    while start < n:
        if s >= num:
            s -= arr[start]
            start += 1
        elif end == n:
            break
        else:
            s += arr[end]
            end += 1

        if s == num:
            cnt += 1
    return cnt


print(solve(prime_set, n))
