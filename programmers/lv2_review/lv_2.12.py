# 소수 찾기
def solution(numbers):
    def solve(s, n, k):
        if k == n:
            res.add(int(s))
            return

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                solve(s + numbers[i], n, k + 1)
                visited[i] = False

    cnt = 0

    visited = [False] * len(numbers)
    res = set()
    for i in range(1, len(numbers) + 1):
        solve("", i, 0)
    primes = get_prime_list(10000000)
    for i in res:
        if i in primes:
            cnt += 1

    return cnt


def get_prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return set([i for i in range(2, n) if sieve[i]])


print(get_prime_list(10000000))