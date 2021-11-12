# 폴리오미노
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 10 * 1000 * 1000


def poly(n, first):
    # 모든 블록을 다 사용했다면 성공한 경우이므로 1을 반환한다.
    if n == first:
        return 1
    # 이미 방문했다면, 수를 반환한다.
    if cache[n][first] > -1:
        return cache[n][first]
    cache[n][first] = 0
    # 모든 경우에 대해서 완전 탐색한다.
    for second in range(1, n - first + 1):
        add = second + first - 1
        add *= poly(n - first, second)
        add %= MOD
        cache[n][first] += add
        cache[n][first] %= MOD
    return cache[n][first]


T = int(si())
cache = [[-1 for _ in range(101)] for _ in range(101)]
for _ in range(T):
    N = int(si())
    s = 0
    for first in range(1, N + 1):
        s += poly(N, first)
        # 다 더한후 MOD 나누는 것 잊지 않기
        s %= MOD
    print(s)
