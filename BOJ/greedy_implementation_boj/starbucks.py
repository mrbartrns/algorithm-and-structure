# BOJ 1758 알바생 강호
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
q = []
ret = 0
for _ in range(N):
    heapq.heappush(q, -int(si()))

for i in range(1, N + 1):
    number = -heapq.heappop(q)
    if number - i + 1 <= 0:
        break
    ret += number - i + 1
print(ret)
