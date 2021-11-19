# BOJ 1720 타일 코드
"""
1. 총 경우의 수 구하기
1개짜리가 하나의 경우가 있고, 두 개를 만드는 경우가 두 가지 경우가 존재하므로,
*** cache[i] = cache[i - 1] + 2 * cache[i - 2] (if i - 1 >= 0, i - 2 >= 0)
cache[i] = 1) 좌우가 대칭인 경우 + 2) 좌우가 대칭이 아닌 경우로 나눌 수 있음
2) 좌우가 대칭이 아닌 경우
다른 누군가와 무조건 겹치는 경우가 존재한다. 그 경우 하나로 취급하므로 절반을 나눈 경우를 구한다.
answer = 2) // 2 + 1)
answer = (cache[n] + 1)) // 2 처럼 바꿔 쓸 수 있다.

1) 자체적으로 좌우 대칭인 경우
1-1) N이 홀수인 경우: cache[N // 2]
1-2) N이 짝수인 경우: cache[N // 2] + cache[N // 2 - 1] * 2
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
cache = [0] * 31
cache[0] = 1
for i in range(1, N + 1):
    if i - 1 >= 0:
        cache[i] += cache[i - 1]
    if i - 2 >= 0:
        cache[i] += 2 * cache[i - 2]

if N % 2 == 1:
    print((cache[N] + cache[(N - 1) // 2]) // 2)
else:
    print((cache[N] + cache[N // 2] + cache[N // 2 - 1] * 2) // 2)
