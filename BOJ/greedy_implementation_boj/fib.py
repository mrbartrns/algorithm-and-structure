# BOJ 9009 피보나치
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


cache = [0] * 51
cache[1] = 1
for i in range(2, 51):
    cache[i] = cache[i - 1] + cache[i - 2]
T = int(si())
for _ in range(T):
    N = int(si())
    answer = []
    s = 0
    for i in range(50, 0, -1):
        if s + cache[i] <= N:
            s += cache[i]
            answer.append(cache[i])
            if s == N:
                print(" ".join(list(map(str, reversed(answer)))))
