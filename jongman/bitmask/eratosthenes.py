"""
비트마스크를 활용한 에라토스테네스의 체
"""
MAX_N = 20
sieve = [255 for _ in range((MAX_N + 7) // 8 + 1)]


def set_composite(k):
    sieve[k >> 3] &= ~(1 << (k & 7))


def is_prime(k):
    return True if sieve[k >> 3] & (1 << (k & 7)) else False


set_composite(0)
set_composite(1)

for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime(i):
        for j in range(i * i, MAX_N + 1, i):
            set_composite(j)

for i in range(MAX_N + 1):
    print(is_prime(i))
