# BOJ 11000
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

arr = []
q = []
n = int(si())
for _ in range(n):
    a, b = map(int, si().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[0], x[1]))
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    st = arr[i][0]
    if q and q[0] <= st:
        heapq.heappop(q)
    heapq.heappush(q, arr[i][1])

print(len(q))
