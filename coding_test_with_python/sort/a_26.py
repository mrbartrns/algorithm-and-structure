# BOJ 1715 (카드 정렬하기)
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
res = 0
q = []
for _ in range(n):
    heapq.heappush(q, int(si()))

while q:
    n1 = heapq.heappop(q)
    if q:
        n2 = heapq.heappop(q)
        heapq.heappush(q, (n1 + n2))
        res += n1 + n2
    else:
        print(res)
        break
